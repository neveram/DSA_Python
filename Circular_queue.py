  class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    # Enqueue operation
    def enqueue(self, value):
        # Check if the queue is full
        if (self.tail + 1) % self.size == self.head:
            print("Queue is Full! Overflow condition.")
            return

        # Check if the queue is empty
        if self.head == -1:
            self.head = 0

        # Update tail and insert the new element
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        print(f"Enqueued: {value}")

    # Dequeue operation
    def dequeue(self):
        # Check if the queue is empty
        if self.head == -1:
            print("Queue is Empty! Underflow condition.")
            return

        # Remove the element from the head
        value = self.queue[self.head]
        self.queue[self.head] = None

        # Check if the queue becomes empty after this operation
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size

        print(f"Dequeued: {value}")

    # Display the current state of the queue
    def display(self):
        if self.head == -1:
            print("Queue is Empty!")
            return

        print("Circular Queue Elements:")
        index = self.head
        while True:
            print(self.queue[index], end=" ")
            if index == self.tail:
                break
            index = (index + 1) % self.size
        print()


# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # Queue should be full here
cq.display()

cq.dequeue()
cq.enqueue(60)  # Should successfully add at the beginning
cq.display()