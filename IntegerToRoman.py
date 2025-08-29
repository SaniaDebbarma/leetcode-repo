class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #val = v
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]
        
        result = ""

        for v, s in zip(val, syms): #zip is built in function => names = ["Sania", "Rahul", "Aditi"] #ages = [19, 21, 20] Sania 19# Rahul 21# Aditi 20

            count = num // v # for example num is 1994 // 1000 = 1 
            result += s * count #result = result + (symbol * 1 = M)
            num %= v #1994%1000 = 994

        return result


roman = int(input("Enter a number between 1 and 3999: "))


sol = Solution()


print("Roman numeral:", sol.intToRoman(roman))