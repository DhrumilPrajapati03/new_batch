#syntax :
# def function_name(parameters):
#     function body(Logic)
#     return statement

def greet():
    print("Hello, welcome to Python programming!")

def user_info(name, age):
    print(f"Name: {name}, Age: {age}")
    
#functoin call
user_info("Karan",20)

greet()

def add(a,b):
    '''
    input : a,b (numbers)
    output : sum of a and b'''
    return a + b

print(add(5, 10))
print(add(3.5, 2.5))