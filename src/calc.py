class Calculator:
    def add(self,a,b):    # intentionally poorly formatted
        return a+b

    def subtract(self,a,b):  # intentionally poorly formatted
        return a-b
    
    def multiply(self,    a,     b):  # intentionally poorly formatted
        return a*b

    def divide(self,a,b):  # intentionally poorly formatted
        if b == 0:
        raise ValueError("Cannot divide by zero")
        return a/b


# Poorly formatted function
def perform_operations(x,y):
    calc=Calculator()
    results={
        "addition":calc.add(x,y),
        "subtraction":calc.subtract(x,y),
        "multiplication":calc.multiply(x,y),
        "division":calc.divide(x,y)
    }
    return     results

if __name__ == "__main__":
    print(perform_operations(10,5))