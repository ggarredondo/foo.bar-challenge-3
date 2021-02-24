import solution
import random


def list_gen():
    length = random.randint(1, 10)
    array = []
    product_positive = 1
    product_negative = 1
    highest_negative = -2**31
    for i in range(0, length):
        array.append(random.randint(-10, 10))
        if array[i] > 0:
            product_positive *= array[i]
        elif array[i] < 0:
            product_negative *= array[i]
            if array[i] > highest_negative:
                highest_negative = array[i]
    print("Product positive: " + str(product_positive))
    print("Product negative: " + str(product_negative))
    print("Highest negative: " + str(highest_negative))
    print(array)
    return array


def main():
    print(solution.solution(list_gen()))


if __name__ == '__main__':
    main()