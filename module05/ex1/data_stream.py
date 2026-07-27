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

                log_str = f"{item['log_level']}: {item['log_message']}"
                self._data.append((self._rank_counter, log_str))
                self._rank_counter += 1


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
                print(
                    "DataStream error: Can't"
                    f"  process element in stream: {item}"
                    )

    def print_processors_stats(self) -> None:
        if len(self.registered_processors) == 0:
            print("No processor found, no data\n")
        else:
            for proc in self.registered_processors:
                proc_name: str = type(proc).__name__.replace("Processor",
                                                             " Processor")
                total_processed: int = proc._rank_counter
                remaining: int = len(proc._data)

                print(f"{proc_name}: total {total_processed} "
                      f"items processed, remaining {remaining} on processor")


def main() -> None:
    print("=== Code Nexus Data Stream ===\n")
    print("Initialize Data Stream...")

    stream = DataStream()

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("Registering Numeric Processor\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)

    batch_1: list = [
        'Hello world',
        [3.14, 1, 2.71],
        [{'log_level': 'WARNING', 'log_message':
          'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print(f"Send first batch of data on stream: {batch_1}")
    stream.process_stream(batch_1)

    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nRegistering other data processors...")
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    stream.register_processor(text_proc)
    stream.register_processor(log_proc)

    print("Send the same batch again...")
    stream.process_stream(batch_1)
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nConsume some elements from the data "
          "processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    for _ in range(1):
        log_proc.output()

    print("== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
