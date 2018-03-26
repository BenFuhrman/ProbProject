# Global variables
number_of_inputs = 4
user_input = [0] * number_of_inputs
user_input_text = ['starting value', 'multiplier', 'increment', 'modulus']


def prompt(variable_name, prompt_index):
    while True:
        try:
            user_input[prompt_index] = float(input("Please enter the " + variable_name + ": "))
        except ValueError:
            print('Dummy, enter in the correct format.')
        else:
            break


for i in range(number_of_inputs):
    prompt(user_input_text[i], i)

starting_value = user_input[0]
multiplier = user_input[1]
increment = user_input[2]
modulus = 2**user_input[3]


def generate(how_many):
    pseudo_random_values_x = [starting_value] * how_many
    pseudo_random_values_u = [starting_value] * how_many
    for i in range(how_many):
        if i != 0:
            x_i = multiplier * pseudo_random_values_x[i-1] + increment
            pseudo_random_values_x[i] = x_i % modulus

    for j in range(how_many):
        pseudo_random_values_u[j] = pseudo_random_values_x[j] / modulus
    return pseudo_random_values_u


#   1000, 7893, 3517, 2^13
print(generate(4))
