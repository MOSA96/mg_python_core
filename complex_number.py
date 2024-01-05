class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __str__(self):
        # Human-readable string representation 
        return f"({self.real} + {self.imag}i)"

num1 = ComplexNumber(1, 2)  
num2 = ComplexNumber(3, 4) 

print(num1 + num2)  # Addition: (1 + 2i) + (3 + 4i) = (4 + 6i)
print(num1 * num2)  # Multiplication: (1 + 2i)(3 + 4i) = (3 + 8) + (4 + 6)i = (-5 + 10i)