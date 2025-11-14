#!/usr/bin/env python3

def calculate_average(numbers):
    """Calculate the average of a list of numbers"""
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

def main():
    print("Welcome to the Average Calculator!")

    # Test with some numbers
    test_numbers = [10, 20, 30, 40, 50]
    result = calculate_average(test_numbers)
    print(f"Average of {test_numbers}: {result}")

    # Oops! Let's try with an empty list
    empty_list = []
    result2 = calculate_average(empty_list)
    print(f"Average of empty list: {result2}")

    print("All done!")

if __name__ == "__main__":
    main()
