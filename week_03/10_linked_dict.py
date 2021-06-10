# hash collision 을 chaining 을 통해서 해결함
# linked list 자료구조 활용

class LinkedTuple:
    def __init__(self):
        self.items = list()

    # [("sdkfdkfslf8", "test")] -> [("sdkfdkfslf", "test33)]
    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __int__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        idx = hash(key) % len(self.items)
        self.items[idx].add(key, value)

    def get(self, key):
        idx = hash(key) % len(self.items)
        return self.items[idx].get(key)
