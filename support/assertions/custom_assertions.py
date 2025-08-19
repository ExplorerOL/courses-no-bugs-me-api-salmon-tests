from contextlib import nullcontext
from typing import Any

from config.config_general import config_general
from support.assertions.assert_soft import assert_soft
from support.reporters.allure.reporting_classes import ClassWithMethodReporting


class CustomAssertions(ClassWithMethodReporting):
    @staticmethod
    def verify_is_equal(actual_value: Any, expected_value: Any, soft: bool = True) -> None:
        """Проверка на равенство фактического и ожидаемого значений."""
        with assert_soft if soft else nullcontext():
            config_general.reporter.attach_text(
                f'Фактическое значение: {actual_value!r}\n\nОжидаемое значение: {expected_value!r}'
            )
            assert actual_value == expected_value, (
                f'Фактическое значение {actual_value!r} не равно ожидаемому {repr(expected_value).replace("<", "&#60")}!'
            )
