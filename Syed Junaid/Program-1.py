# Create a small calculator
class Calculator:
    def __init__(self, a, b, operator):
        self.a = a
        self.b = b
        self.operator = operator
    def calculate(self):
        if self.operator =='add':
            return self.a+self.b
        elif self.operator =='subtract':
            return self.a-self.b
        elif self.operator =='mul':
            return self.a*self.b
        elif self.operator =='divide':
            if self.b!=0:
                return self.a/self.b
            else:
                return "Denominator cannot be Zero."
        else:
            return "Enter only available operations"

a= int(input('Enter the value for a:'))
b = int(input('Enter the value for b:'))
operator = input('Enter the operation to be performed(add,subtract,mul,divide:)').lower()

res= Calculator(a,b,operator)
print('Result:',res.calculate())