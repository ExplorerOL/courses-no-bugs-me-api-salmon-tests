from abc import ABC

from support.reporters.allure.reporter_metaclasses import (
    ClassABCMetaWithMethodReporting,
    MetaclassWithMethodReporting,
)


class ClassWithMethodReporting(metaclass=MetaclassWithMethodReporting):
    pass


class ABCWithMethodReporting(ABC, metaclass=ClassABCMetaWithMethodReporting):
    pass
