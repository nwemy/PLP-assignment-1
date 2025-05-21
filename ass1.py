print("Welcome Please input two numbers and the arithmetic operations below")
#let the first and second number be a and b respectively
a = float(input ("Input the first number: "))
b = float(input("Input the second number: "))
operator = input("which of these do you want" \
" +, -, *, / : ")

if operator == "+":
    output = a + b
elif operator == "-":
    output = a - b
elif operator == "*": 
    output = a * b
else:
    output = a/b
        
    
print("This is your result for ",a,
       operator ,b ,"= ", output)