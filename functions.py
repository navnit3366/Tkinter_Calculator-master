numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e']
operator_list = ['+', '-', '*', '**', '(', ')', '÷', '/']
dot_list = ['.']
got_operator = False
got_point = True
string_fill = "0"

# Function for validation


def get_value(values):
    string = ""
    for value in values:
        if value in numbers_list or value in operator_list or value in dot_list:
            string = string + value
    if values == '0':
        string = ""
    return string


def arrange(unarrangeed_string):
    new_str = ""
    count = 0
    point_str = unarrangeed_string.split()[1]
    if len(point_str) > 2:
        for i in point_str:
            if count > 2:
                new_str = new_str + i
                count += 1
    elif point_str == "0" or point_str == "00":
        new_str = int(unarrangeed_string)
