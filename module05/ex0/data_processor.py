import abc
import typing


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
        # 1. Comprobamos si el dato es un diccionario
        if isinstance(data, dict):
            # Recorremos el diccionario para ver si todo es texto
            for clave, valor in data.items():
                if not isinstance(clave, str) or not isinstance(valor, str):
                    return False
            return True
            
        # 2. Comprobamos si es una lista (puede ser una lista de diccionarios)
        elif isinstance(data, list):
            for item in data:
                # Si el elemento de la lista NO es un diccionario, rechazamos
                if not isinstance(item, dict):
                    return False
                
                # Recorremos el diccionario por dentro
                for clave, valor in item.items():
                    if not isinstance(clave, str) or not isinstance(valor, str):
                        return False
            return True
            
        # Si no es ni diccionario ni lista, a la calle
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        # 1. Si es un diccionario suelto
        if isinstance(data, dict):
            # TU MISION:
            # Crea un texto con formato (f-string) uniendo el nivel y el mensaje.
            # Pista: para sacar un valor del dict usas data['nombre_de_la_clave']
            # log_str: str = f"{...}: {...}"
            
            # Luego lo guardas en self._data con su _rank_counter y sumas 1 al contador
            pass
            
        # 2. Si es una lista de diccionarios
        elif isinstance(data, list):
            for item in data:
                # TU MISION:
                # Lo mismo, pero para cada 'item' de la lista.
                # Creas el texto formateado, lo guardas y sumas 1 al contador.
                pass

def main() -> None:
    print("=== Code Nexus Data Processor ===")

    # --- PRUEBAS DEL NUMERIC PROCESSOR ---
    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    
    # Comprobamos validaciones
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    # Forzamos un error a posta para ver si salta la excepcion
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # OJO: MyPy se quejara de esto, el PDF dice que es correcto
    except Exception as error:
        print(f"Got exception: {error}")

    # Metemos datos buenos y los sacamos
    lista_numeros: list = [1, 2, 3, 4, 5]
    print(f"Processing data: {lista_numeros}")
    num_proc.ingest(lista_numeros)

    print("Extracting 3 values...")
    for _ in range(3):
        rango, valor = num_proc.output()
        print(f"Numeric value {rango}:\n{valor}")


    # --- PRUEBAS DEL TEXT PROCESSOR ---
    print("\nTesting Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")
    
    lista_textos: list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {lista_textos}")
    text_proc.ingest(lista_textos)

    print("Extracting 1 value...")
    rango, valor = text_proc.output()
    print(f"Text value {rango}: {valor}")


    # --- PRUEBAS DEL LOG PROCESSOR ---
    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    lista_diccionarios: list = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!!'}
    ]
    print(f"Processing data: {lista_diccionarios}")
    log_proc.ingest(lista_diccionarios)

    print("Extracting 2 values...")
    for _ in range(2):
        rango, valor = log_proc.output()
        print(f"Log entry {rango}: {valor}")


if __name__ == "__main__":
    main()
