import sys
import weakref
from typing import Union, Dict, Any
from collections.abc import Coroutine
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep

if sys.version_info <= (3, 10):  # pragma: no cover
    from typing_extensions import TypeAlias
else:  # pragma: no cover
    from typing import TypeAlias

from emptylog import LoggerProtocol
from displayhooks import not_display


if sys.version_info >= (3, 9):  # pragma: no cover
    CoroutineClass: TypeAlias = Coroutine[Any, Any, None]
else:  # pragma: no cover
    CoroutineClass = Coroutine

class UsageTracer(CoroutineClass):
    def __init__(self, number: Union[int, float], logger: LoggerProtocol) -> None:
        self.flags: Dict[str, bool] = {}
        self.coroutine = self.async_sleep_option(number, self.flags, logger)
        weakref.finalize(self, self.sync_sleep_option, number, self.flags, self.coroutine, logger)

    def __await__(self) -> Any:  # pragma: no cover
        return self.coroutine.__await__()

    def send(self, value: Any) -> Any:
        return self.coroutine.send(value)

    def throw(self, exception_type: Any, value: Any = None, traceback: Any = None) -> None:  # pragma: no cover
        pass

    def close(self) -> None:  # pragma: no cover
        pass

    @staticmethod
    def sync_sleep_option(number: Union[int, float], flags: Dict[str, bool], wrapped_coroutine: CoroutineClass, logger: LoggerProtocol) -> None:
        if not flags.get('used', False):
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
