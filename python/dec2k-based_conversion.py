# dec 2 k-based

def dec2k(dec, k):
    
    result = []
    result_reversed = []
    remainder = 0
    
    while dec > 0:
        remainder = dec % k
        result.append(remainder)
        dec = dec // k
        
    result_reversed = result[::-1]
    
    return result, result_reversed
 
decimal = int(input('Enter decimal: '))
k = int(input('Enter k: '))

print(dec2k(decimal, k))



