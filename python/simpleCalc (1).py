def validRunner(func):
    def wrapper(*args, **kwargs):
        if func.__name__ not in ['mult', 'add']:
            print('Invalid method for calculation')
            return None
        
        return func(*args, **kwargs)
        
    return wrapper
    
@validRunner
def mult(n1, n2):
    print(f"Mupltiplying {n1} and {n2}:")
    return n1*n2

@validRunner
def add(n1, n2):
    print(f"Adding {n1} and {n2}:")
    return n1+n2

print("Program testing")
print('-' * 30)
print(mult(4,5))
print(add(4,5))
    
    
    
