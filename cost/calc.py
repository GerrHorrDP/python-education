"""This module contains a code for calculator class"""


class SimpleCalculator:
    """Code for calculator class"""
    @staticmethod
    def addition():
        """This function adding one input number
         to another input number"""
        first_number = input('Please input first number')
        second_number = input(f'{first_number} + \n'
                              f'Please input second number')
        solution = int(first_number) + int(second_number)
        print(f'{first_number} + {second_number} ='
              f' {solution}')

    @staticmethod
    def subtraction():
        """This function subtracting one input number
         from another input number"""
        first_number = input('Please input first number')
        second_number = input(f'{first_number} - \n'
                              f'Please input second number')
        solution = int(first_number) - int(second_number)
        print(f'{first_number} - {second_number} ='
              f' {solution}')

    @staticmethod
    def multiplication():
        """This function multiplying one input number
         by another input number"""
        first_number = input('Please input first number')
        second_number = input(f'{first_number} * \n'
                              f'Please input second number')
        solution = int(first_number) * int(second_number)
        print(f'{first_number} * {second_number} ='
              f' {solution}')

    @staticmethod
    def division():
        """This function dividing first input number 'dividend'
         by second input number 'divisor'"""
        first_number = input('Please input dividend')
        second_number = input(f'{first_number} / \n'
                              f'Please input divisor')
        solution = int(first_number) / int(second_number)
        print(f'{first_number} / {second_number} ='
              f' {solution}')

# SimpleCalculator.addition()
# SimpleCalculator.subtraction()
# SimpleCalculator.multiplication()
# SimpleCalculator.division()
