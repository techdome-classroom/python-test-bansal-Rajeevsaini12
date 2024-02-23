class Solution(object):
    def romanToInt(self, s):
        rom_dict={ 'I':1, 'V':5,'X':10,'L':50, 'C':100, 'D':500 , 'M':1000}
        total=0
        pre_value=0

        for char in s:
            value=rom_dict[s]
            if value>pre_value:
                total+=value-2* pre_value

            else:
                total+=value
            pre_value=value

        return total   


Sol=Solution()
print(Sol.romanToInt('III'))
print(Sol.romanToInt('LVIII'))
print(Sol.romanToInt('MCMXCIV'))
