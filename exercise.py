import random as rd


class CalculationGenerator:
    """
    A class that generates calculations based on user-defined parameters.

    Parameters
    ----------

    num_type : int or float
        type of number used in the calculations, can be integer or decimal.
        Example:  int -> 1, float -> 1.5
    num_digits : int
        number of digits for the operand in the calculation.
        Example:  2
    operation : str
        type of operation to perform in the calculation.
        Example:  "+", "-", "*", "/"
    difficulty : str
        level of difficulty of the calculation
        Example:  "easy", "medium", "hard"

    Note
    ----
    - Supported operations : "+", "-", "*", "/".
    - The level of difficulty is linked to the number of carry-overs.

    Returns
    -------     

    
    """
    def __init__(self, num_type, num_digits, operation, difficulty):
        self.num_type = num_type
        self.num_digits = num_digits
        self.operation = operation
        self.difficulty = difficulty
        self.a, self.b = 0, 0

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
        if self.difficulty == "medium": #not complete
            i = 0
            carry_over = 0
            while i < self.num_digits: 
                if i == self.num_digits-1:
                    a_i = rd.randint(1,8)
                    b_i = rd.randint(1,9-a_i)
                else:
                    pass
                a_i = rd.randint(1,9)
                b_i = rd.randint(10-carry_over-a_i,9)
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

if __name__ == "__main__":
    print("Test zone :")
    calculation = CalculationGenerator(int, 3, "+", "hard")
    calculation.generation_addition()
    print(calculation.a)
    print(calculation.b)