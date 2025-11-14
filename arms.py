def romanToInt(romaninput):

    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

    resultInteger = 0

    for i in range(0, len(romaninput) - 1):
        if roman[romaninput[i]] < roman[romaninput[i+1]]:
            resultInteger -= roman[romaninput[i]]
        else:
            resultInteger += roman[romaninput[i]]
    return resultInteger + roman[romaninput[-1]]

roman = input("enter roman numeral: ")

print("interger equivalent: ", romanToInt(roman))