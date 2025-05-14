import sys
import weakref
from typing import Union, Dict, Type, Any, Optional
from types import TracebackType
from collections.abc import Coroutine
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep

from emptylog import LoggerProtocol
from displayhooks import not_display


class UsageTracer(Coroutine):
    def __init__(self, number: Union[int, float], logger: LoggerProtocol) -> None:
        self.flags: Dict[str, bool] = {}
        self.coroutine = self.async_sleep_option(number, self.flags, logger)
        weakref.finalize(self, self.sync_sleep_option, number, self.flags, self.coroutine, logger)

    def __await__(self):
        return self.coroutine.__await__()

    def send(self, value: Any) -> None:
        return self.coroutine.send(value)

    def throw(self, exception_type: Optional[Type[BaseException]], value: Optional[BaseException] = None, traceback: Optional[TracebackType] = None) -> None:
        pass

    def close(self) -> None:
        pass

    @staticmethod
    def sync_sleep_option(number: Union[int, float], flags: Dict[str, bool], wrapped_coroutine: Coroutine, logger: LoggerProtocol) -> None:
        if not flags.get('used', False):
            if sys.getrefcount(wrapped_coroutine) < 5:
                wrapped_coroutine.close()
                logger.info(f'Run sync sleep {number} sec...')
                sync_sleep(number)
                logger.info('The end of sync sleeping.')

    @staticmethod
    async def async_sleep_option(number: Union[int, float], flags: Dict[str, bool], logger: LoggerProtocol) -> None:
        flags['used'] = True
        logger.info(f'Run async sleep {number} sec...')
        await async_sleep(number)
        logger.info('The end of async sleeping.')


not_display(UsageTracer)
