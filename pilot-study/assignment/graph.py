class Node:
    def __init__(self, label, neighbors = None):
        self.label = label

        if (neighbors is None):
            neighbors = []

        self.neighbors = neighbors

    def __repr__(self):
        neighbor_labels = [neighbor.label for neighbor in self.neighbors]
        neighbors = ",".join(neighbor_labels)

        return f"Node(label = {self.label}, neighbors = [{neighbors}])"

    def __eq__(self, other):
        return self.label == other.label

    def __hash__(self):
        return hash(self.label)

class Queue:
    def __init__(self):
        self._items = []
        self._num_push = 0
        self._num_pop = 0

    def __len__(self) -> int:
        """ Override the len() operator to get the size of the queue. """

        return len(self._items)

    def push(self, item):
        """ Enqueue the item into the queue. """

        self._num_push += 1
        self._items.insert(0, item)

    def pop(self):
        """ Dequeue the earliest enqueued item still in the queue. """

        self._num_pop += 1
        return self._items.pop()

    def is_empty(self):
        """" Returns True if the queue is empty. """

        return len(self._items) == 0
