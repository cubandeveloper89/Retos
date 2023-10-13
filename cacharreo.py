


def end_zeros(a: int) -> int:
    zeros = 0
    for i in a :
        if i == '0':
            zeros += 1
        else:
            break
    return zeros


print(end_zeros('0000010010'))