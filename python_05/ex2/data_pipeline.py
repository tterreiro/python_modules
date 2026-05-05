#!/usr/bin/env python3
from typing import Any, Protocol
from abc import ABC, abstractmethod


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        processed_data = [item[1] for item in data]
        print("CSV Output:")
        print(*processed_data, sep=",")


class JSONPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = ", ".join(f'"item_{rank}": "{item}"' for rank, item in data)
        print("JSON Output:")
        print("{" + items + "}")


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, Any]] = []
        self.rank: int = 0
        self.total_proc: int = 0
        self.remaining = len(self.storage)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise IndexError("No data available in processor")
        return (self.storage.pop(0))

    @abstractmethod
    def get_stats(self) -> list[Any]:
        ...


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if data.__class__ == list:
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        elif isinstance(data, (int, float)):
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if data.__class__ == list:
            for item in data:
                processed_str = str(item)
                self.storage.append((self.rank, processed_str))
                self.rank += 1
                self.total_proc += 1
        else:
            processed_str = str(data)
            self.storage.append((self.rank, processed_str))
            self.rank += 1
            self.total_proc += 1

    def get_stats(self) -> list[Any]:
        self.remaining = len(self.storage)
        return ['Numeric Processor', self.remaining]


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if data.__class__ == list:
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        elif data.__class__ == str:
            return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if data.__class__ == list:
            for item in data:
                self.storage.append((self.rank, item))
                self.rank += 1
                self.total_proc += 1
        else:
            self.storage.append((self.rank, data))
            self.rank += 1
            self.total_proc += 1

    def get_stats(self) -> list[Any]:
        self.remaining = len(self.storage)
        return ['Text Processor', self.remaining]


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if data.__class__ == list:
            for item in data:
                if item.__class__ != dict:
                    return False
                level = item.get("log_level")
                msg = item.get("log_message")

                if not isinstance(level, str) or not isinstance(msg, str):
                    return False
            return True
        if data.__class__ == dict:
            level = data.get("log_level")
            msg = data.get("log_message")
            if isinstance(level, str) and isinstance(msg, str):
                return True
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        items = data if isinstance(data, list) else [data]
        for item in items:
            processed_str = f"{item['log_level']}: {item['log_message']}"
            self.storage.append((self.rank, processed_str))
            self.rank += 1
            self.total_proc += 1

    def get_stats(self) -> list[Any]:
        self.remaining = len(self.storage)
        return ['Log Processor', self.remaining]


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc not in self.processors:
            self.processors.append(proc)
        else:
            print("Processor is already registered!")

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            for proc in self.processors:
                if proc.validate(data) is True:
                    proc.ingest(data)
                    break
            else:
                print("DataStream error - Can't process element in stream:",
                      data)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
        else:
            for processor in self.processors:
                stats = processor.get_stats()
                print(
                    f"{stats[0]}: "
                    f"total {processor.total_proc} items processed,"
                    f" remaining {stats[1]} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if not self.processors:
            print("No processor, no data")
        else:
            for processor in self.processors:
                data = []
                for _ in range(nb):
                    try:
                        data.append(processor.output())
                    except IndexError:
                        break
                if data:
                    plugin.process_output(data)


def data_pipeline() -> None:
    print("=== Code Nexus - Data Pipeline ===\n")
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {'log_level': 'WARNING',
             'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO',
             'log_message': 'User wil is connected'}
        ],
        42,
        ['Hi', 'five']]
    batch2 = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()]
    data_stream = DataStream()
    print("Initialize Data Stream...")
    data_stream.print_processors_stats()
    print("\nRegistering Processors\n")
    for processor in processors:
        data_stream.register_processor(processor)
    print(f"Send first batch of data on stream: {batch}")
    data_stream.process_stream(batch)
    data_stream.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    data_stream.output_pipeline(3, CSVPlugin())
    data_stream.print_processors_stats()
    print(f"Send another batch of data on stream: {batch2}")
    data_stream.process_stream(batch2)
    data_stream.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    data_stream.output_pipeline(5, JSONPlugin())
    data_stream.print_processors_stats()


if __name__ == "__main__":
    data_pipeline()
