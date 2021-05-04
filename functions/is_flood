from time import time
from typing import Union

from config import MESSAGES, SECONDS, USERS


def is_flooder(uid: int) -> Union[bool, None]:
    USERS[uid].append(time())
    if len(list(filter(lambda x: time() - int(x) < SECONDS, USERS[uid]))) > MESSAGES:
        USERS[uid] = list(
            filter(lambda x: time() - int(x) < SECONDS, USERS[uid]))
        return True
