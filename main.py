"""
OrderOfNumbers
"""


def order_of_numbers():
    n1 = int(input("n1:"))
    n2 = int(input("n2:"))
    n3 = int(input("n3:"))

    if n1 < n2 < n3:
        print("numbers are ascending")
    elif n3 < n2 < n1:
        print("numbers are descending")
    else:
        if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
            print("no specific order, but all even")
        elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
            print("no specific order, but all odd")
        else:
            print("no specific order")


"""
SumUp
"""


def sum_up():
    n1 = int(input("n1:"))
    n2 = int(input("n2:"))

    if n1 <= 0 or n2 <= 0:
        print("n1 and n2 need to be > 0")
    elif n2 < n1:
        print("n2 needs to be > n1")
    else:
        while n1 <= n2:
            print(str(n1) + " ", end="")
            n1 += 1


if __name__ == '__main__':
    print("Test your solutions here")
    order_of_numbers()
    sum_up()
