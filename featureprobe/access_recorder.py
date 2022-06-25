# -*- coding: UTF-8 -*-


from time import time
from typing import Dict, List
import copy

from featureprobe.access_event import AccessEvent


class AccessRecorder:
    class Counter:

        def __init__(self, value: str, version: int, index: int):
            self._value = value
            self._version = version
            self._index = index
            self._count = 0

        @property
        def value(self):
            return self._value

        @property
        def version(self):
            return self._version

        @property
        def index(self):
            return self._index

        def increment(self):
            self._count += 1

        def is_group(self, event: AccessEvent):
            return self._value == event.value and self._version == event.version and self._index == event.index

    def __init__(self):
        self._counters: Dict[str, List[AccessRecorder.Counter]] = {}
        self._start_time = 0
        self._end_time = 0

    @property
    def counters(self):
        return self._counters

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    def add(self, event: AccessEvent):
        if not self._counters:
            self._start_time = int(time() * 1000)
        if counters := self._counters[event.key]:
            for counter in counters:
                if counter.is_group(event):
                    counter.increment()
                    return
            counters.append(AccessRecorder.Counter(event.value, event.version, event.index))
        else:
            groups = [AccessRecorder.Counter(event.value, event.version, event.index)]
            self._counters[event.key] = groups

    def snapshot(self):
        _snapshot = copy.deepcopy(self)
        _snapshot._end_time = int(time() * 1000)
        return _snapshot

    def clear(self):
        self._counters = {}
