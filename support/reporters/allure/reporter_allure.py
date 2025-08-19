from functools import wraps

import allure

from support.reporters.base_reporter import BaseReporter


class ReporterAllure(BaseReporter):
    def ARRANGE(self, msg: str):
        return allure.step(f'ARRANGE: {msg}')

    def ACT(self, msg: str):
        return allure.step(f'ACT: {msg}')

    def ASSERT(self, msg: str):
        return allure.step(f'ASSERT: {msg}')

    def step(self, name: str):
        return allure.step(name)

    def attach_text(self, text: str, name: str = 'Info'):
        return allure.attach(text, name=name, attachment_type=allure.attachment_type.TEXT)

    def step_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            first_line_from_docstring = str(func.__doc__).split('\n')[0] if func.__doc__ else ''
            step_self = args[0]
            with self.step(
                f'Step: {first_line_from_docstring} | {step_self.__module__} -> {step_self.__class__.__name__} -> {func.__name__}'
            ):
                self.attach_text(text=f'Args: {args}\nKwargs: {kwargs}', name='Arguments')
                return func(*args, **kwargs)

        return wrapper

    def static_step_decorator(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            first_line_from_docstring = str(func.__doc__).split('\n')[0] if func.__doc__ else ''
            with allure.step(
                f'Step: {first_line_from_docstring} | {func.__module__} -> {func.__class__.__name__} -> {func.__name__}'
            ):
                self.attach_text(text=f'Args: {args}\nKwargs: {kwargs}', name='Arguments')
                return func(*args, **kwargs)

        return wrapper

    def set_parent_suite(self, parent_suite_name: str):
        return allure.dynamic.parent_suite(parent_suite_name=parent_suite_name)

    def set_suite(self, suite_name: str):
        return allure.dynamic.suite(suite_name=suite_name)

    def set_sub_suite(self, sub_suite_name: str):
        return allure.dynamic.sub_suite(sub_suite_name=sub_suite_name)
