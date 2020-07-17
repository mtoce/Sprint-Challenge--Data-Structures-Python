class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.storage = []

    def append(self, item):
        # if there is capacity left, append to storage
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        # begin overwrite existing elements
        else:
            self.storage[self.index] = item
        self.index += 1
        # if the index hits capacity, go back to index 0 and begin overwriting there
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        return self.storage