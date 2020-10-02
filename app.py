def convert_to_roman(decimal_num):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_to_roman = ""
    for i,d in enumerate(num):
        while (decimal_num >= d):
            decimal_num -= d
            num_to_roman += roman[i]
    return num_to_roman
#print(convert_to_roman(3285))