"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# while exit_condition_not_reached:
#     input = consume_input()
#     output = evaluate_input(input)
#     print(output)

while True:
    # get user input in the form [operation] [num1] [num2]
    input_string = input('What do you want to calculate? ')
    # sample input would be '+ 1 2'

    # separate the input string into usable parts
    input_tokens = input_string.split(' ')
    operation = input_tokens[0]

    if 'q' in operation:
        print('You will exit')
        break
    else:
        num1 = input_tokens[1]
        num2 = input_tokens[2]

        output = f'num1 is {num1} and num2 is {num2}'

    print(output)
