"""
Quadratic equations  a x^2 + b x + c = 0
input: 3 coefficients a, b, c
tasks:
1. Validate the user's inputs
2. Display the equation in a nice form with superscript
3. Print the number of real roots
3. Display the roots with subscripts
"""
import math as m


def validate_input(prompt_string):
    while True:
        try:
            input_num = float(input(prompt_string))
            if input_num.is_integer():
                return input_num
            else:
                print('Invalid input. Plz enter an integer')
        except ValueError:
            print('Invalid input. Plz enter an integer')


def solve_quadratic_eqn(coeff_1, coeff_2, coeff_3):
    # display the equation
    print('Given the equation:\n',
          coeff_1, 'x', "{}".format('\N{SUPERSCRIPT TWO}'),
          '+', coeff_2, 'x', '+', coeff_3, '= 0')
    if coeff_1 == 0:
        if coeff_2 == 0:
            if coeff_3 != 0:
                print('The equation is inconsistent.')
            else:
                print('The equation has infinitely many solutions.')
        else:
            print('The equation has a unique solution,', 'x = ', -coeff_3 / coeff_2)
    else:
        delta = coeff_2 ** 2 - 4 * coeff_1 * coeff_3
        print('\u0394 = ', delta)
        if delta < 0:
            print("The equation doesn't have any real roots")
        elif delta == 0:
            print('The equation has a unique real solution',
                  'x = ', - coeff_2 / (2 * coeff_1))
        else:
            print('The equation has 2 distinct real roots',
                  'x{} = '.format('\N{SUBSCRIPT ONE}'), (- coeff_2 - m.sqrt(delta)) / (2 * coeff_1),
                  ', x{} = '.format('\N{SUBSCRIPT TWO}'), (- coeff_2 + m.sqrt(delta)) / (2 * coeff_1))


if __name__ == '__main__':
    test_cases = int(validate_input('number of test cases = '))
    while test_cases > 0:
        num_1 = validate_input('a = ')
        num_2 = validate_input('b = ')
        num_3 = validate_input('c = ')
        solve_quadratic_eqn(num_1, num_2, num_3)
        test_cases -= 1
