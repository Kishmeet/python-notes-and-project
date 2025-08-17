# math_operations.py
def compute_sum(a, b):
    return a + b

def compute_average(a, b):
    return (a + b) / 2

def compute_difference(a, b):
    return a - b

def compute_product(a, b):
    return a * b

def compute_division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"
