def return_10 ():
    return 10

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_num, second_num):
    return first_num - second_num

def multiply(first_num, second_num):
    return first_num * second_num

def divide(first_num, second_num):
    return first_num / second_num

def length_of_string(a_string):
    return len(a_string)

def join_string(first_string, second_string):
    return first_string + second_string

def add_string_as_number(first_string_num, second_string_num):
    return int(first_string_num) + int(second_string_num)

def number_to_full_month_name(month_as_num):
    month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_list[month_as_num - 1]

def number_to_short_month_name(month_as_num):
    short_month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return short_month_list[month_as_num - 1]

def volume_of_cube(side_length):
    return side_length**3

def reverse_string(string_to_reverse):
    list_of_characters = []
    for character in string_to_reverse:
        list_of_characters.append(character)
    list_of_characters.reverse()
    reversed_string = ""
    for character in list_of_characters:
        reversed_string += character
    return reversed_string

def farenheit_to_celcius(farenheit_temp):
    celcius_temp = (farenheit_temp - 32) * 5/9
    return celcius_temp