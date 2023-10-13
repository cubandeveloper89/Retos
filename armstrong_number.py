### It's a Armstrong Number? ### 

def is_armstrong_number(number):
    print(number)
    sum = 0
    number_str = str(number)
    number_dig = len(number_str)
    for i in number_str:
        p = int(i)**int(number_dig)
        sum += p
    if sum == number:
        return 'It\'s an Armstrong Number, congrats!'
    else:
        return 'It\'s not an Armstrong Number, try another'
    
print(is_armstrong_number(407))