'''
Question:
    https://leetcode.com/problems/integer-to-roman/description/
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        input -> integer
        output -> string

        """

        # roman_map = {
        #     "I":1,
        #     "V":5,
        #     "X":10,
        #     "L":50,
        #     "C":100,
        #     "D":500,
        #     "M":1000
        # }

        # store_int_roman = {
        #     1000:"M",
        #     900:"CM",
        #     500:"D",
        #     400:"CD",
        #     100:"C",
        #     90:"XC",
        #     50:"L",
        #     40:"XL",
        #     10:"X",
        #     9:"IX",
        #     5:"V",
        #     4:"IV",
        #     1:"I",
        # }

        # storeIntRoman = [
        #     [1000, "M"], [900, "CM"], [500, "D"], 
        #     [400, "CD"], [100, "C"], [90, "XC"], 
        #     [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], 
        #     [5, "V"], [4, "IV"], [1, "I"]]

        # roman_string_list = []

        # for i in store_int_roman:
        #     if num >= i:
        #         roman_string_list.append(store_int_roman[i])
        #         num -= i
        # print("".join(roman_string_list))
        # return "".join(roman_string_list)

        Roman = ""
        storeIntRoman = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman
    

#-----------------
# OPTIMIZED SOLUTION

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        Given an integer, return its corresponding Roman numeral.

        Time Complexity: O(1) - The number of Roman numeral symbols is constant (13), so we always iterate a fixed number of times.
        Space Complexity: O(k) - The space used depends on the length of the output Roman numeral string, where k is the number of symbols needed to represent the integer.
        """
        
        # List of tuples where each tuple contains the integer value and its corresponding Roman numeral symbol.
        storeIntRoman = [
            [1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
            [100, "C"], [90, "XC"], [50, "L"], [40, "XL"],
            [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]
        ]
        
        result = ""

        # Iterate through each Roman numeral symbol and value pair
        for value, symbol in storeIntRoman:
            while num >= value:
                result += symbol  # Append the Roman numeral symbol
                num -= value  # Subtract the value from num

        return result
