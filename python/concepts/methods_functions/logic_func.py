def even_check(number):
    return number % 2 == 0

# print(even_check(10))

# return true if any num is even inside a list

def check_even_list(num_list):
    # return all the even numbers in a list
    even_numbers = []
    odd_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    return even_numbers, odd_numbers

print(check_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))