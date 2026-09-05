def simpleCalc(num1, num2, method):
    
    if method in ['mult', 'add', 'subs', 'div']:
        pass
    else:
        #print('Invalid method to calculate!')
        #return None
        raise ValueError("Invalid method to calculate")
        
    def mult(num1, num2):
        return num1*num2
    def add(num1, num2):
        return num1+num2 
    def subs(num1, num2):
        return num1 - num2 
    def div(num1, num2):
        return num1 / num2
        
    if method == "mult":
        return mult(num1, num2)
    if method == "add":
        return add(num1, num2)
    if method == "subs":
        return subs(num1, num2)
    if method == "div":
        try:
            return div(num1, num2)
        except ZeroDivisionError:
            print('Error: Can not divide number by zero!')
            return None

print('Testing program')
print(simpleCalc(12,0, "miss"))
    
    
    
    
