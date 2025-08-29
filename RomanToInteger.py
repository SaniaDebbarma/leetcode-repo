class Solution(object):
    def RomanToInteger(self, s):

        roman_dict = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        total = 0
        prev = 0

        for char in reversed ( s):
            value = roman_dict[char]
        if value < prev : 
            total = total - value
        else : 
            total = total + value
        prev = value

        return total
    
user_input = input("Enter a roman numeral : ")
sol = Solution()
print("Integer value is : ", sol.RomanToInteger(user_input))





    
    