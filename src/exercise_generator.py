import random as rd


class CalculationGenerator:
    """
    A class that generates calculations based on user-defined parameters.

    Parameters
    ----------
    operation : str
        type of operation to perform in the calculation.
        Example:  "addition", "substraction", "multiplication", "division"
    difficulty : str
        level of difficulty of the calculation
        Example:  "easy", "medium", "hard"

    Note
    ----
    Supported operations : "+", "-", "*", "/".
    """
    
    def __init__(self, operation, difficulty):
        self.operation = operation
        self.difficulty = difficulty
        self.a, self.b = 0, 0
        if self.difficulty == "easy":
            self.num_digits = 2
        if self.difficulty == "medium":
            self.num_digits = 3
        if self.difficulty == "hard":
            self.num_digits = 4

    def generation_addition(self):
        if self.difficulty == "easy":
            i = 0
            while i < self.num_digits:
                if i == self.num_digits-1:
                    a_i = rd.randint(1,8)
                    b_i = rd.randint(1,9-a_i)
                else:
                    a_i = rd.randint(0,9)
                    b_i = rd.randint(0,9-a_i)
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1
        if self.difficulty == "medium":
            i = 0
            carry_over = 0
            while i < self.num_digits: 
                a_i = rd.randint(1,9)
                b_i = rd.randint(max(1,6-carry_over-a_i),9)
                carry_over = (a_i+b_i)//10
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1     
        if self.difficulty == "hard":
            i = 0
            carry_over = 0
            while i < self.num_digits:
                a_i = rd.randint(1,9)
                b_i = rd.randint(10-carry_over-a_i,9)
                carry_over = (a_i+b_i)//10
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1  
        self.result = self.a + self.b 
    
    def generation_substraction(self):
        if self.difficulty == "easy":
            i = 0
            while i < self.num_digits:
                if i == self.num_digits-1:
                    b_i = rd.randint(1,9)
                    a_i = rd.randint(b_i,9)
                else:
                    b_i = rd.randint(0,9)
                    a_i = rd.randint(b_i,9)
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1          
        if self.difficulty == "medium":
            i = 0
            while i < self.num_digits:
                if i == self.num_digits-1:
                    b_i = rd.randint(1,8)
                    a_i = rd.randint(b_i+1,9)
                else:
                    x = rd.randint(0,9)
                    y = rd.randint(x,9)
                    a_i = rd.choice([x,y])
                    b_i = x if a_i == y else y
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1
        if self.difficulty == "hard":
            i = 0
            while i < self.num_digits:
                if i == self.num_digits-1:
                    b_i = rd.randint(1,7)
                    a_i = rd.randint(b_i+2,9)
                elif i == 0:
                    a_i = rd.randint(0,8)
                    b_i = rd.randint(a_i,9)
                else:
                    a_i = rd.randint(0,9)
                    b_i = rd.randint(a_i,9)
                self.a += a_i*10**i
                self.b += b_i*10**i
                i+=1
        self.result = self.a - self.b 
    
    def generation_multiplication(self):
        if self.difficulty == "easy":
            self.a = rd.randint(11,99)
            self.b = rd.randint(2,9)
        if self.difficulty == "medium":
            self.a = rd.randint(11,999)
            self.b = rd.randint(11,99)
        if self.difficulty == "hard":
            self.a = rd.randint(101,9999)
            self.b = rd.randint(11,999)
        self.result = self.a * self.b 
        
    def generation_division(self):
        if self.difficulty == "easy":
            self.a = rd.randint(11,99)
            self.b = rd.randint(2,9)
        if self.difficulty == "medium":
            self.a = rd.randint(100,999)
            self.b = rd.choice([rd.randint(2,9), rd.randint(11,99)])
        if self.difficulty == "hard":
            self.a = rd.randint(1000,9999)
            self.b = rd.randint(11,99)
        self.result = self.a // self.b, self.a % self.b
    
    def generate(self):
        if self.operation == "addition":
            self.generation_addition()
        if self.operation == "substraction":
            self.generation_substraction()
        if self.operation == "multiplication":
            self.generation_multiplication()
        if self.operation == "division":
            self.generation_division()
        # x, y, z = self.a, self.b, self.result
        # self.a, self.b = 0, 0
        return self.a, self.b, self.result
        # return x, y, z
    

    

    
if __name__ == "__main__":
    print("Test zone :")
    operation = rd.choice(["addition", "substraction", "multiplication", "division"])
    difficulty = rd.choice(["easy", "medium", "hard"])
    calculation = CalculationGenerator(operation, difficulty)
    CG = CalculationGenerator(operation=operation, difficulty=difficulty)
    print(CG.generate())