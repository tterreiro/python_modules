#!/usr/bin/env python3
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.storage: list[tuple[int, Any]] = []
        self.rank: int = 0

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
        else:
            processed_str = str(data)
            self.storage.append((self.rank, processed_str))
            self.rank += 1


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
        else:
            self.storage.append((self.rank, data))
            self.rank += 1


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


def data_processor():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        print("Testing Numeric Processor...")
        numeric = NumericProcessor()
        print(f"Trying to validate input '42': {numeric.validate(42)}")
        print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
        print(
            "Test invalid ingestion of string 'foo' without prior validation:")
        try:
            numeric.ingest("foo")
        except ValueError as e:
            print(f"Got exception: {e}")
        data = [1, 2, 3, 4, 5]
        print(f"Processing Data: {data}")
        numeric.ingest(data)
        print("Extracting 3 values...")
        for _ in range(3):
            index, value = numeric.output()
            print(f"Numeric value {index}: {value}")
    except ValueError as e:
        print(e)

    try:
        print("\nInitializing Text Processor...")
        text = TextProcessor()
        print(f"Trying to validate input '42': {text.validate(42)}")
        data = ['Hello', 'Nexus', 'World']
        print(f"Processing Data: {data}")
        text.ingest(data)
        print("Extracting 1 values...")
        for _ in range(1):
            index, value = text.output()
            print(f"Text value {index}: {value}")
    except ValueError as e:
        print(e)

    try:
        print("\nInitializing Log Processor...")
        log = LogProcessor()
        print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
        data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
        print(f'Processing Data: "{data}"')
        print("Extracting 2 values...")
        log.ingest(data)
        for _ in range(2):
            index, value = log.output()
            print(f"Log entry {index}: {value}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    data_processor()
