from src.fizzbuzz import fizzbuzz


def test_fizzbuzz_cases():
    cases = {1: "1", 3: "Fizz", 5: "Buzz", 15: "FizzBuzz"}
    for n, expected in cases.items():
        assert fizzbuzz(n) == expected
