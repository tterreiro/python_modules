#!/usr/bin/env python3
import pandas
import requests
import matplotlib
import numpy
import sys
import importlib


def check_dependency(package: str) -> bool:
    try:
        importlib.import_module(package)
        return True
    except Exception:
        return False


def ft_loading() -> None:
    


if __name__ == "__main__":
    ft_loading()
