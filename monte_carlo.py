# Global variables
import math

w_list = [0] * 500


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


def generate_xi(how_many):
    xi_values = [0] * how_many
    ui_values = generate(how_many)
    for k in range(how_many):
        xi_values[k] = -12*math.log(1-(ui_values[k]))
    return xi_values


#   1000, 7893, 3517, 2^13
def mc_sim(num_runs):
    ulist = generate(num_runs)
    xlist = generate_xi(num_runs)
    for i in range(num_runs):
        failure = 0
        while failure < 4:
            w_list[i] += 6
            if ulist[i] <= 0.2:
                failure += 1
                w_list[i] += 4
            elif ulist[i] <= 0.5:
                failure += 1
                w_list[i] += 26
            else:
                w_list[i] += xlist[i]
                break
    #print(ulist)
    #print(xlist)
    print(w_list)


mc_sim(500)



