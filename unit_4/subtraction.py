'''
You are given two exceedingly large positive decimal numbers, num1 and num2, both represented as strings. The length of these strings can range anywhere from 1 to 500 characters. The challenge here is to subtract num2 from num1 without directly converting the strings into integers.

Create a Python function that performs this operation and returns the resultant string, referred to as num3.

Please note that the subtraction will not result in a negative number, as num1 will always be greater than or equal to num2.
'''

def solution(num1, num2):
    # TODO: Implement the solution
    i = len(num1) - 1
    j = len(num2) - 1
    borrow = 0
    result = []
    
    '''
    398746
    199234
     
    '''
    
    while i >= 0 or j >= 0 or borrow > 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0
        
        if borrow > 0:
            digit1 -= 1
        
        if digit2 > digit1:
            borrow = 10
        else:
            borrow = 0
            
        total = digit1 + borrow - digit2
        
        curr = total % 10
        result.append(str(curr))
        i -= 1
        j -= 1
        
    result = result[::-1]
    return ''.join(result).lstrip('0') or '0'