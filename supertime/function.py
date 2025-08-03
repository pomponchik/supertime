from typing import Union, NoReturn
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep

from transfunctions import superfunction, sync_context, async_context, await_it


@superfunction(tilde_syntax=False)
def supersleep(number):
    with sync_context:
        sync_sleep(number)

    with async_context:
        await_it(async_sleep(number))
