'''
You are tasked with writing a Python function to multiply two extremely large positive integers. These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.

Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.

Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.

Challenge yourself, and Happy Coding!
'''

def solution(num1, num2):
    # TODO: Implement Function
    
    num1_length = len(num1) - 1
    total = "0"
    while num1_length >= 0:
        digit1 = int(num1[num1_length])
        
        mult_carry = 0
        digit_total = []
        
        if num1_length != len(num1) - 1:
            for i in range(len(num1) - 1 - num1_length):
                digit_total.append("0")
            
        num2_length = len(num2) - 1
        while num2_length >= 0:
            digit2 = int(num2[num2_length])
            product = (digit1 * digit2) + mult_carry
            
            if product > 9:
                mult_carry = product // 10
            else:
                mult_carry = 0
                
            digit_total.append(str(product % 10))
            num2_length -= 1
            
        if mult_carry != 0:
            digit_total.append(str(mult_carry))
        total = large_addition(total, ''.join(digit_total[::-1]))
        num1_length -= 1
        
    return total.lstrip('0') or '0'
        
       
def large_addition(num1, num2):
    i, j, carry, res = len(num1) - 1, len(num2) - 1, 0, []
    
    while i >= 0 or j >= 0 or carry > 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = n1 + n2 + carry
        if total > 9:
            carry = 1
        else:
            carry = 0
        curr = total % 10
        res.append(str(curr))
        i, j = i - 1, j - 1

    return ''.join(res[::-1])