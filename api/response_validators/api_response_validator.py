from contextlib import nullcontext

import requests

from support.assertions.assert_soft import assert_soft
from support.assertions.custom_assertions import CustomAssertions
from support.reporters.allure.reporting_classes import ClassWithMethodReporting


class APIResponseValidator(ClassWithMethodReporting):
    def __init__(
        self,
        expected_staus_code: int | None = None,
        expected_body: str | dict | None = None,
        expected_headers: dict[str, str] | None = None,
    ):
        self.__expected_status_code = expected_staus_code
        self.__expected_body = expected_body
        self.__expected_headers = expected_headers

    def __validate_status_code(self, actual_status_code: int, soft: bool = False) -> None:
        if self.__expected_status_code:
            CustomAssertions.verify_is_equal(
                actual_value=actual_status_code,
                expected_value=self.__expected_status_code,
                soft=soft,
            )

    def __validate_body(self, actual_body: str, soft: bool = False) -> None:
        if self.__expected_body is not None:
            CustomAssertions.verify_is_equal(
                actual_value=actual_body,
                expected_value=self.__expected_body,
                soft=soft,
            )

    def __validate_headers(self, actual_headers: dict[str, str], soft: bool = False) -> None:
        if self.__expected_headers is not None:
            with assert_soft if soft else nullcontext():
                for header_name, expected_header_value in self.__expected_headers.items():
                    actual_header_value = actual_headers.get(header_name)
                    CustomAssertions.verify_is_equal(
                        actual_value=actual_header_value,
                        expected_value=expected_header_value,
                        soft=soft,
                    )

    def validate_response(self, response: requests.Response, soft: bool = False) -> None:
        """Проверка ответа на соответствие ожидаемым значениям статус кода, тела и заголовков."""
        self.__validate_status_code(actual_status_code=response.status_code, soft=soft)
        self.__validate_body(actual_body=response.text, soft=soft)
        self.__validate_headers(actual_headers=dict(response.headers), soft=soft)
