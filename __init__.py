import numpy as np
import time


class metric(object):
    def __init__(self, description='Metric'):
        self.x = np.empty((100,))
        self.y = np.empty((100,))
        self.i = 0
        self.last = None

    def __lshift__(self, other):
        if hasattr(other, '__len__'):
            if len(other) == 2:
                new_x = other[0]
                new_y = other[1]
        else:
            new_x = self.i
            new_y = other
        self.x[self.i] = new_x
        self.y[self.i] = new_y
        self.last = new_y
        self.i += 1
        if self.i == (len(self.x) - 1):
            empty = np.empty((100,))
            self.x = np.concatenate((self.x, empty), axis=0)
            empty = np.empty((100,))
            self.y = np.concatenate((self.y, empty), axis=0)

    def is_max(self):
        if self.i >= 2:
            return self.y[self.i - 1] == np.nanmax(self.y[:self.i-1])
        else:
            return True
