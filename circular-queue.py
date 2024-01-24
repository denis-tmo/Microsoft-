"""
CircularQueue: A dictionary using a circular buffer. It removes the oldest element when the buffer lenght exceed the maximum size.
"""

from collections import OrderedDict

class CircularQueue(OrderedDict):
    """
    Initialize maxlen and call initialize the base class
    """
    def __init__(self, maxlen, *args, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    """
    enqueue: removes last inserted item or remove last inserted item if buffer is full
    """
    def enqueue(self, key, value):
        # Remove last item
        if len(self) >= self.maxlen:
            assert len(self) == self.maxlen, f"len(self) must be equal to self.maxlen. len(self)={len(self)}, self.maxlen={self.maxlen}"
            super().popitem(last=True)        
        OrderedDict.__setitem__(self, key, value)

# Initialize a CircularDict with a maximum length of 3
cqueue = CircularQueue(maxlen=3)
# Add items
size = 3
for i in range(1, size + 1):
    cqueue.enqueue( 'key' + str(i) , 'value' + str(i))

print(f'Initialy:')
print(cqueue)

print(f'After adding an element beyond maxlen: {cqueue}')
print(f'{cqueue}')

