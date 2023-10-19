"""
Even-odd vending machine
input: a number
tasks: 1. Print whether the number is even or odd
       2. Display the number followed by the next 9 even or odd numbers
"""


def is_even(int_num):
    return int_num % 2 == 0


def next_9_numbers(num):
    return ','.join([str(num + 2 * _) for _ in range(1, 10)])


def validate_input():
    while True:
        try:
            input_num = float(input())
            if input_num.is_integer():
                return int(input_num)
            else:
                print('Invalid input. Plz enter an integer')
        except ValueError:
            print('Invalid input. Plz enter an integer')


if __name__ == '__main__':
    user_input = validate_input()
    parity = 'even' if is_even(user_input) else 'odd'
    print(user_input, 'is', parity)
    print('next 9 numbers are:', next_9_numbers(user_input))
