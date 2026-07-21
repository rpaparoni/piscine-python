import abc
import typing


class ExportPlugin(typing.Protocol):
    """
    Este es el molde (Protocol). Obliga a cualquier clase que actúe como plugin
    a tener exactamente este método.
    """
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        # Extraemos solo el texto (índice 1 de la tupla) de cada elemento
        values: list[str] = [item[1] for item in data]

        # Unimos todos los textos con una coma y un espacio
        csv_string: str = ", ".join(values)
        print(csv_string)


class JsonExport:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        json_parts: list[str] = []

        # Recorremos la lista de tuplas desempaquetando el rango y el valor
        for rank, value in data:
            # Construimos la estructura clave-valor a mano
            json_parts.append(f'"item_{rank}": "{value}"')

        # Unimos todo con comas y lo envolvemos en llaves
        json_string: str = "{" + ", ".join(json_parts) + "}"
        print(json_string)


class DataStream:
    def __init__(self) -> None:
        self.registered_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            procesado: bool = False

            for proc in self.registered_processors:
                if proc.validate(item):
                    proc.ingest(item)
                    procesado = True
                    break
            if not procesado:
                print(f"DataStream error: Can't process element in stream: {item}")

    def print_processors_stats(self) -> None:
        if len(self.registered_processors) == 0:
            print("No processor found, no data")
        else:
            for proc in self.registered_processors:
                proc_name: str = type(proc).__name__.replace("Processor", " Processor")
                total_processed: int = proc._rank_counter
                remaining: int = len(proc._data)

                print(f"{proc_name}: total {total_processed} items processed, remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        # 1. Recorremos todos los procesadores registrados
        for proc in self.registered_processors:
            data_to_export: list[tuple[int, str]] = []

            # 2. Intentamos sacar 'nb' elementos de cada uno
            for _ in range(nb):
                # Comprobamos que queden datos en la memoria para no causar un error
                if len(proc._data) > 0:
                    data_to_export.append(proc.output())
                else:
                    # Si ya no quedan datos, rompemos este bucle interno
                    break

            # 3. Si hemos conseguido sacar datos, se los mandamos al plugin
            if data_to_export:
                plugin.process_output(data_to_export)


class DataProcessor(abc.ABC):

    def __init__(self) -> None:
        self._data: list = []
        self._rank_counter: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self._data) == 0:
            raise Exception("No data left to output")

        oldest_item = self._data.pop(0)
        return (oldest_item[0], oldest_item[1])


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")

        if isinstance(data, (int, float)):
            data_str: str = str(data)
            self._data.append((self._rank_counter, data_str))
            self._rank_counter += 1
        elif isinstance(data, list):
            for item in data:
                item_str: str = str(item)
                self._data.append((self._rank_counter, item_str))
                self._rank_counter += 1


class TextProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, str):
            self._data.append((self._rank_counter, data))
            self._rank_counter += 1
        elif isinstance(data, list):
            for item in data:
                self._data.append((self._rank_counter, item))
                self._rank_counter += 1


class LogProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True

        elif isinstance(data, list):
            for item in data:
                if not isinstance(item, dict):
                    return False

                for key, value in item.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True

        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        if isinstance(data, dict):
            log_str: str = f"{data['log_level']}: {data['log_message']}"

            self._data.append((self._rank_counter, log_str))
            self._rank_counter += 1

        elif isinstance(data, list):
            for item in data:

                log_str: str = f"{item['log_level']}: {item['log_message']}"
                self._data.append((self._rank_counter, log_str))
                self._rank_counter += 1


def main() -> None:
    print("=== Code Nexus Data Pipeline ===")

    # 1. Preparamos el terreno
    stream = DataStream()
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    # 2. Creamos una buena comanda variada
    batch: list = [
        'First text',
        42,
        {'log_level': 'INFO', 'log_message': 'System started'},
        [1, 2, 3],
        ['Second text', 'Third text'],
        [{'log_level': 'ERROR', 'log_message': 'Crash'}]
    ]

    print("--- Processing stream ---")
    stream.process_stream(batch)
    stream.print_processors_stats()

    # 3. Contratamos a nuestros dos exportadores
    csv_plugin = CsvExport()
    json_plugin = JsonExport()

    # 4. Ponemos a prueba la pipeline sacando 2 elementos de cada maquina
    print("\n--- Exporting 2 elements per processor via CSV ---")
    # Pasamos '2' como cantidad y le damos nuestro plugin de CSV
    stream.output_pipeline(2, csv_plugin)

    print("\n== DataStream statistics after CSV export ==")
    stream.print_processors_stats()

    print("\n--- Exporting 2 elements per processor via JSON ---")
    # Volvemos a pedir '2', pero esta vez le damos el plugin de JSON
    stream.output_pipeline(2, json_plugin)

    print("\n== Final DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
