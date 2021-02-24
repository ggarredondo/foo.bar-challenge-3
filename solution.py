

def solution(xs):
    product_positive = -1
    product_negative = 1
    highest_negative = -2**31
    for i in range(0, len(xs)):
        if xs[i] > 0:
            if product_positive == -1:
                product_positive = 1
            product_positive *= xs[i]
        elif xs[i] < 0:
            product_negative *= xs[i]
            if xs[i] > highest_negative:
                highest_negative = xs[i]
    result = abs(product_positive) * product_negative

    if 0 > product_negative >= result:
        result /= highest_negative
    if result == 1:
        if len(xs) > 1:
            result = 0
        else:
            result = product_negative

    return str(result)
