class Jar:
    def __init__(self, capacity=12):
        # Initialize the jar with a specified capacity, defaulting to 12 cookies.
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        # Return a string representation of the jar using cookie emojis.
        return "🍪" * self.size

    def deposit(self, n):
        # Add cookies to the jar, raising a ValueError if the jar would overflow.
        if self.size + n > self.capacity:
            raise ValueError("Deposit error")
        self.size += n

    def withdraw(self, n):
        # Remove cookies from the jar, raising a ValueError if the jar would be emptied beyond its current size.
        if n > self.size:
            raise ValueError("Withdraw error")
        self.size -= n

    @property
    def capacity(self):
        # Property to get the capacity of the jar.
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # Setter for the capacity property, ensuring that it is always a positive integer.
        if capacity < 1:
            raise ValueError("@capacity.setter error")
        self._capacity = capacity

    @property
    def size(self):
        # Property to get the current size of the jar.
        return self._size

    @size.setter
    def size(self, size):
        # Setter for the size property, ensuring that it does not exceed the jar's capacity.
        if size > self.capacity:
            raise ValueError("@size.setter error")
        self._size = size

def main():
    # Create a jar object.
    jar = Jar()
    print(jar)  # Print the initial state of the jar.
    
    # Deposit and withdraw cookies, printing the jar's state after each operation.
    jar.deposit(1)
    print(jar)
    jar.deposit(3)
    print(jar)
    jar.withdraw(2)
    print(jar)

if __name__ == "__main__":
    main()
