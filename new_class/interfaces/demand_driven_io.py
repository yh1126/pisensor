#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta


class DemandDrivenIo(metaclass=ABCMeta):
    """This class is for the demand driven sensors"""

    @abstractmethod
    def read(self):
        # subclass implement this method.
        # this method is for the sensor to read value.
        pass

    @abstractmethod
    def write(self):
        # subclass implement this method.
        # this method is for the sensor to write value.
        pass
