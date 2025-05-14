from typing import Union

from emptylog import EmptyLogger, LoggerProtocol

from supertime.tracer import UsageTracer


def supersleep(number: Union[int, float], logger: LoggerProtocol = EmptyLogger()) -> UsageTracer:
    return UsageTracer(number, logger)
