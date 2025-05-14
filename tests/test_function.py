from time import time
from asyncio import run

from emptylog import MemoryLogger

from supertime import supersleep


def test_simple_sync_sleep():
    sleep_time = 0.001

    before = time()
    supersleep(sleep_time)
    after = time()

    assert after - before >= sleep_time


def test_simple_async_sleep():
    sleep_time = 0.001

    before = time()
    run(supersleep(sleep_time))
    after = time()

    assert after - before >= sleep_time


def test_logging_when_sync_sleep():
    sleep_time = 0.001
    logger = MemoryLogger()

    supersleep(sleep_time, logger=logger)

    assert len(logger.data) == len(logger.data.info) == 2
    assert [x.message for x in logger.data.info] == [
        f'Run sync sleep {sleep_time} sec...',
        'The end of sync sleeping.',
    ]


def test_logging_when_async_sleep():
    sleep_time = 0.001
    logger = MemoryLogger()

    run(supersleep(sleep_time, logger=logger))

    assert len(logger.data) == len(logger.data.info) == 2
    assert [x.message for x in logger.data.info] == [
        f'Run async sleep {sleep_time} sec...',
        'The end of async sleeping.',
    ]
