'''
Python
Author: Xiang Li

Time used: 188 ms
check desired substrings and add corresponding values
then delete such subtrings from the string
use loop to check each remaining roman char from the string and add values
'''
roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]

roman_num = dict()
for i in range(len(roman)):
    roman_num[roman[i]] = num[i] 
# @param {string} s
# @return {integer}
def romanToInt(s):
    num = 0
    check = ['IV','IX','XL','XC','CD','CM']
    for a in check:
        if a in s:
            i = s.index(a)
            num = num + roman_num[a]
            s = s[0:i]+s[i+2:]    
    input_s = list(s)
    for b in input_s:
        num = num + roman_num[b]
    return num
