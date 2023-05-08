from ting_file_management.abstract_queue import AbstractQueue
from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self._data = deque()
        self._length = 0

    def __len__(self):
        return self._length

    def enqueue(self, value):
        self._data.append(value)
        self._length += 1

    def dequeue(self):
        try:
            removed_element = self._data.popleft()
        finally:
            self._length -= 1
            return removed_element

    def search(self, index):
        if index >= self._length or index < 0:
            raise IndexError("Índice Inválido ou Inexistente")

        return self._data[index]
