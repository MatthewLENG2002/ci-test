# -*- coding: UTF-8 -*-

from event import Event
from fp_user import FPUser


class AccessEvent(Event):

    def __init__(self, timestamp: int, user: FPUser, key: str, value: str, version: int, index: int):
        super().__init__(timestamp, user)
        self._key = key
        self._value = value
        self._version = version
        self._index = index

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

    @property
    def version(self):
        return self._version

    @property
    def index(self):
        return self._index
