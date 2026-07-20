import abc
import typing


class DataStream():
    def __init__(self):
        self.registered_processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.registered_processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for i in stream:
            for j in self.registered_processors:
                if j.validate(i):
                    j.ingest(i)
                    print(f"me comi {i}")

    def print_processors_stats(self) -> None:
        pass


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
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")

    lista = ['hola', 'tete']
    maquina = TextProcessor()
    test = DataStream()
    test.register_processor(maquina)
    test.process_stream(lista)


if __name__ == "__main__":
    main()
