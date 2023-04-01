class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or type(capacity) != int:
            raise ValueError
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if n < 0 or type(n) != int:
            raise ValueError
        if self.cookies + n > self.capacity:
            raise ValueError
        self.cookies += n

    def withdraw(self, n):
        if n < 0 or type(n) != int:
            raise ValueError
        if self.cookies - n < 0:
            raise ValueError
        self.cookies -= n

    @property
    def size(self):
        return self.cookies
