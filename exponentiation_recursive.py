def exponentiation(base, exponent ):
    if (exponent  == 0):
        return 1    
    else:
        return base * exponentiation(base, exponent  - 1)
    
base = int(input("Enter the value of Base: "))
exponent  = int(input("Enter the Value of Exponent: "))

print(f"{base}^{exponent} Equals:", exponentiation(base, exponent ))