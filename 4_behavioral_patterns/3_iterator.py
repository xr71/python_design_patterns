import pytest

# iterators allow for isolation
# interface

def count_to():

    numbers = ["un", "deux", "trois", "quatre", "cinq"]

    it = zip(range(len(numbers)), numbers)

    for p, n in it:
        yield n

for num in count_to():
    print(num)
