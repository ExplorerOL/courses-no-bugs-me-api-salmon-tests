import requests

from support.reporters.base_reporter import BaseReporter


class HTTPSessionWithReporting(requests.Session):
    def __init__(self, reporter: BaseReporter):
        self.__reporter = reporter
        super().__init__()

    def send(self, request, **kwargs):
        """Отправка HTTP-запроса"""
        with self.__reporter.step(f'Отправка HTTP-запроса {request.method} на URL {request.url}'):
            self.__reporter.attach_text(
                name='Запрос',
                text=f'Метод: {request.method},\nURL: {request.url},\nЗаголовки:  {request.headers}\nТело: {request.body}',
            )
            response = super().send(request, **kwargs)
            self.__reporter.attach_text(
                name='Ответ',
                text=f'Код: {response.status_code},\nТело: {response.text!r}',
            )
            return response
