from config.config_general import config_general
from support.assertions.assert_soft import assert_soft
from support.assertions.custom_assertions import CustomAssertions
from support.operations.operations_posts import OperationsPosts


class BaseTest:
    assert_soft = assert_soft
    assertions = CustomAssertions
    operations_posts = OperationsPosts

    def ARRANGE(self, msg: str = ''):
        return config_general.reporter.ARRANGE(msg=msg)

    def ACT(self, msg: str = ''):
        return config_general.reporter.ACT(msg=msg)

    def ASSERT(self, msg: str = ''):
        return config_general.reporter.ASSERT(msg=msg)
