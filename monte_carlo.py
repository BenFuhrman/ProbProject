# Global variables
import math
import statistics

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
    ulist = generate(num_runs*2)
    xlist = generate_xi(num_runs)
    for i in range(num_runs):
        failure = 0
        while failure < 4:
            w_list[i] += 6
            if ulist[i+num_runs] <= 0.2:
                failure += 1
                w_list[i] += 3
                w_list[i] += 1
            elif ulist[i+num_runs] <= 0.5:
                failure += 1
                w_list[i] += 25
                w_list[i] += 1
            else:
                w_list[i] += xlist[i]
                break
    print(len(ulist))
    print(w_list)
    print("Average X R.V = " + str(sum(xlist) / 500))


def prob(val, length, lg):
    count = 0
    if lg == '>=':
        for element in w_list:
            if element >= val:
                count += 1
    elif lg == '>':
        for element in w_list:
            if element > val:
                count += 1
    elif lg == '<=':
        for element in w_list:
            if element <= val:
                count += 1
    elif lg == '<':
        for element in w_list:
            if element < val:
                count += 1
    return count / length


length_of_list = len(w_list)
mc_sim(500)

w_list_first = [0] * 125
w_list_third = [0] * 125
for w in range(length_of_list):
    if w < 125:
        w_list_first[w] = w_list[w]
    elif 250 <= w < 375:
        w_list_third[w-250] = w_list[w]

print("Mean = " + str(sum(w_list) / len(w_list)))
print("Median = " + str(statistics.median(w_list)))
print("First Quartile = " + str(statistics.median(w_list_first)))
print("Third Quartile = " + str(statistics.median(w_list_third)))
print("P(W<=15) = " + str(prob(15, length_of_list, '<=')))
print("P(W<=20) = " + str(prob(20, length_of_list, '<=')))
print("P(W<=30) = " + str(prob(30, length_of_list, '<=')))
print("P(W>40) = " + str(prob(40, length_of_list, '>')))





