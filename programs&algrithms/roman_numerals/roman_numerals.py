

a_nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

r_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

def roman_numerals(number, a_nums, r_nums):
    result = ""
    idx = 0

    while number > 0 :
        result += (number // a_nums[idx]) * r_nums[idx]
        number %= a_nums[idx]
        idx += 1

    return result
