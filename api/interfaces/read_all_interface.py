from abc import abstractmethod
from typing import Any

from support.reporters.allure.reporting_classes import ABCWithMethodReporting


class ReadAllInterface(ABCWithMethodReporting):
    @abstractmethod
    def read_all(self) -> Any: ...
