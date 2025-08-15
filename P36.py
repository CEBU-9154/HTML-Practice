class Expression:
    def __init__(self, expression):
        self.expression=expression
    def result(self):
        res=eval(self.expression)
        return res
    def display(self):
        print("Result = ", self.result())
expression=input("Enter a mathematical expression: ")
obj=Expression(expression)
obj.display()