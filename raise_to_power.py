
# print(4**4)


def raise_to_power(base_number, power_number):
    result = 1
    for index in range(power_number):
        result = result * base_number
    return result


print(raise_to_power(7, 5))

