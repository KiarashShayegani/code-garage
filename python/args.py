def skyline(*args):
    if not args:
        return 0
    tallest = args[0]
    for current in args:
        if current > tallest:
            tallest = current
        else:
            pass
        
    return tallest
    
print(skyline(1,34,5,7))
