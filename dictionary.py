def roman(num):
    roman_dictionary = {
        'I': 1,
        "V": 5,
        'X':10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    previous = 0
    for i in num:
        current = roman_dictionary[i]
        result += current
        ##Check for consecutive letters
        if  current > previous:
            result -= 2 * previous
        previous = current
    return result
print(roman('MCMXCIV'))