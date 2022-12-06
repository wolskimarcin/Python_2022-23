import random
import itertools


# iterator nieskończony zwracający 0, 1, 0, 1, 0, 1, ...
class InfiniteZeroOnes:
    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        result = self.current
        self.current = 1 - self.current
        return result


zeroOnes = InfiniteZeroOnes()

# można jawnie utworzyć iterator
it_zeroOnes = iter(zeroOnes)

# for i in it_zeroOnes:
#     print(i)

# lub iterować po zeroOnes

# for number in zeroOnes:
#     print(number)

# rozwiązanie bez tworzenia klasy
iter_zeroOnes2 = itertools.cycle([0, 1])
# for i in iter_zeroOnes2:
#     print(i)

# przypadkowa wartość z ("N", "E", "S", "W")
it_direction = (random.choice(("N", "E", "S", "W")) for _ in iter(int, 1))

# for i in it_direction:
#     print(i)

# dni tygodnia: 0, 1, 2, 3, 4, 5, 6, 0, 1, ...
it_days = itertools.cycle([0, 1, 2, 3, 4, 5, 6])

# for i in it_days:
#     print(i)
