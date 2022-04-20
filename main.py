
def euclid_algo():
    array = []
    for i in range(2):
        array.append(int(input("Enter values: ")))
    # return array
    highest_num = max(array)
    small_num = min(array)
    val1, val2 = highest_num, small_num

    while small_num > 0:
        remainder = highest_num % small_num
        highest_num = small_num
        small_num = remainder

    print(f"GCD of {val1} and {val2} is {highest_num} ")


euclid_algo()
