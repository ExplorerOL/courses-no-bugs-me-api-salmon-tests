from abc import abstractmethod
from typing import Any

from support.reporters.allure.reporting_classes import ABCWithMethodReporting


class CRUDInterface(ABCWithMethodReporting):
    @abstractmethod
    def create(self, data: Any) -> Any: ...

    @abstractmethod
    def read(self, id: int) -> Any: ...

    @abstractmethod
    def update(self, id: int, data: Any) -> Any: ...

    @abstractmethod
    def delete(self, id: int) -> Any: ...
