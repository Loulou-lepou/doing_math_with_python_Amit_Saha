"""
Enhanced multiplication table generator
input: numbers a, n
tasks: 1. Print a x i = a * i  for 1 <= i <= n
"""


def nth_multiples(num, n):
    print(f'Multiplication table with number {num}')
    for i in range(1, n + 1):
        print(f'{num} x {i} = {num * i}')


def validate_input(prompt_string):
    while True:
        try:
            input_num = float(input(prompt_string))
            if input_num.is_integer() and input_num > 0:
                return int(input_num)
            else:
                print('Invalid input. Plz enter an integer')
        except ValueError:
            print('Invalid input. Plz enter an integer')


if __name__ == '__main__':
    num_1 = validate_input('Enter number a = ')
    num_2 = validate_input('Enter number n = ')
    nth_multiples(num_1, num_2)
