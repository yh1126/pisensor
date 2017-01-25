#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta


class PeriodicIo(metaclass=ABCMeta):
    """This class is for the periodically driven sensors"""

    @abstractmethod
    def periodic_read(self):
        # subclass implement this method.
        # this methos is for the sensor to periodically read value.
        pass
