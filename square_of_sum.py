def square_of_sum(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
        square = sum**2
    return square





def sum_of_squares(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i**2
        
    return sum



def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)

print(difference_of_squares(10))