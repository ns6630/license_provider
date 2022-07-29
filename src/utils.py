from datetime import datetime

from src.constants import DELTA_BEFORE_EXPIRATION


def get_utcnow_timestamp():
    return int(round(datetime.utcnow().timestamp()))


def get_expiration_timestamp():
    return int(round((datetime.utcnow() - DELTA_BEFORE_EXPIRATION).timestamp()))
