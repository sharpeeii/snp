class EvenNumbers:
    def __init__(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.amount = amount
        else:
            self.amount = 0
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.amount:
            result = self.counter * 2
            self.counter += 1
            return result
        else:
            raise StopIteration

