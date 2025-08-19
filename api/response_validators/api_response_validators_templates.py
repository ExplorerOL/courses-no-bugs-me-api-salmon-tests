from http import HTTPStatus

from api.response_validators.api_response_validator import APIResponseValidator


class APIResponseValidatorsTemplates:
    status_ok = APIResponseValidator(
        expected_staus_code=HTTPStatus.OK,
    )
    status_ok_body_curly_brakets = APIResponseValidator(
        expected_staus_code=HTTPStatus.OK,
        expected_body='{}',
    )
    status_created = APIResponseValidator(
        expected_staus_code=HTTPStatus.CREATED,
    )
    status_not_found_body_curly_brackets = APIResponseValidator(
        expected_staus_code=HTTPStatus.NOT_FOUND,
        expected_body='{}',
    )
    staus_not_found = APIResponseValidator(
        expected_staus_code=HTTPStatus.NOT_FOUND,
    )
