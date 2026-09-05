def productInfo(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} --> {value}')
        
productInfo(
    id= 1245,
    name= "Regrigerator",
    Brand= "Samsung",
    Price= 1499.9
)
