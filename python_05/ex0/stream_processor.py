#!/usr/bin/env python3
from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            raise ValueError("Validation failed: closing program...")
        return (
            f"Processed {len(data)} numeric values, "
            f"sum={sum(data)}, avg={(sum(data)/len(data)):.1f}")

    def validate(self, data: Any) -> bool:
        for i in data:
            if i.__class__ != int:
                return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)

    def execute_all(self, data: Any) -> None:
        process = self.process(data)
        print("Validation: Numeric data verified")
        print(self.format_output(process))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            raise ValueError("Validation failed!")
        return (
            f"Processed text: {len(data)} characters, "
            f"{len(data.split())} words")

    def validate(self, data: Any) -> bool:
        if data.__class__ != str:
            return False
        if data.startswith("ERROR:") or data.startswith("INFO:"):
            return False
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)

    def execute_all(self, data: Any) -> None:
        process = self.process(data)
        print("Validation: Text data verified")
        print(self.format_output(process))


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def process(self, data: Any) -> str:
        if self.validate(data) is False:
            raise ValueError("Validation failed!")
        if "ERROR" in data:
            return (
                f"[ALERT] ERROR level detected:{data[6:]}")
        elif "INFO" in data:
            return (
                f"[INFO] INFO level detected:{data[5:]}")

    def validate(self, data: Any) -> bool:
        if data.__class__ == str:
            if "ERROR" in data or "INFO" in data:
                return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)

    def execute_all(self, data: Any) -> None:
        self.process(data)
        process = self.process(data)
        print("Validation: Log entry verified")
        print(self.format_output(process))


def stream_processor() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        print("Initializing Numeric Processor...")
        data = [1, 2, 3, 4, 5]
        print(f"Processing Data: {data}")
        numeric = NumericProcessor()
        numeric.execute_all(data)
    except ValueError as e:
        print(e)

    try:
        print("\nInitializing Text Processor...")
        data = "Hello Nexus World"
        print(f"Processing Data: {data}")
        text = TextProcessor()
        text.execute_all(data)
    except ValueError as e:
        print(e)

    try:
        print("\nInitializing Log Processor...")
        data = "ERROR: Connection timeout"
        print(f'Processing Data: "{data}"')
        log = LogProcessor()
        log.execute_all(data)
    except ValueError as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    test_data = [
        [1, 2, 5, 6, 7],
        "Hello World",
        "INFO: System ready"
        ]
    i = 0
    for test in test_data:
        for processor in processors:
            if processor.validate(test):
                result = processor.process(test)
                i += 1
                print(f"Result {i}: {result}")


if __name__ == "__main__":
    stream_processor()
