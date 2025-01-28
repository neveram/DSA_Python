class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    # Enqueue operation
    def enqueue(self, value):
        # Check if the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full! Overflow condition.")
            return

        # Check if the queue is empty
        if self.front == -1:
            self.front = 0

        # Update rear and insert the new element
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

    # Dequeue operation
    def dequeue(self):
        # Check if the queue is empty
        if self.front == -1:
            print("Queue is Empty! Underflow condition.")
            return

        # Remove the element from the front
        value = self.queue[self.front]
        self.queue[self.front] = None

        # Check if the queue becomes empty after this operation
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

        print(f"Dequeued: {value}")

    # Display the current state of the queue
    def display(self):
        if self.front == -1:
            print("Queue is Empty!")
            return

        print("Circular Queue Elements:")
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
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