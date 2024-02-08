#!usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    else:
        sum_multiplied_values = sum(score * weight for score, weight in my_list)
        addition_of_weights = sum(weight for _, weight in my_list)

    return (sum_multiplied_values / addition_of_weights)
