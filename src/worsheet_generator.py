from fpdf import FPDF
from exercise_generator import CalculationGenerator
import random as rd

def spacing(x):
    n = len(x)
    res = ''
    for k in range(n):
        if k!=n:
            res += x[k] + ' '
        else:
            res += x[k]
    return res
    

class WorksheetGenerator:
    def __init__(self, operation, difficulty):
        self.operation = operation
        self.difficulty = difficulty
        self.symbol = {'addition':'+', 'substraction':'-', 'multiplication':'x', 'division':'÷'}
        self.level = {'easy':'1', 'medium':'2', 'hard':'3'}
        self.rows = 3
        self.columns = 3
        # self.margin = 25
        self.margin = 20
        self.width = 210 - 2*self.margin
        self.height = 297 - 2*self.margin
        self.pdf = FPDF(format='A4')
        self.pdf.add_page()
        self.pdf.set_margin(self.margin)
    
    def header(self, y_offset=20):
        self.pdf.set_font("helvetica", "B", 20)
        
        #title
        self.pdf.cell(w=self.width,h=10,align='C', txt=f"{self.operation.capitalize()} level {self.level[self.difficulty]}", border=1)

        
        self.pdf.set_xy(self.margin, self.margin+y_offset)
        self.pdf.cell(txt="Nom :") 
        self.pdf.set_xy(self.margin+self.width-2*self.pdf.get_string_width("Note :"), self.margin+y_offset)
        self.pdf.cell(txt="Note :") 
        self.pdf.set_xy(self.margin, self.margin+y_offset+1.5*self.pdf.font_size)
        self.pdf.cell(txt="Prenom :") 
        
        #zone de travail
        # self.pdf.rect(x=self.margin, y=self.margin, w=self.width,h=self.height, style='D')
        
    def footer(self):
        self.pdf.set_xy(self.margin, self.height+self.margin-10)
        self.pdf.cell(w=self.width,h=10,align='C', txt="ArithmeticAce", border=1)
    
    def numbers_generator(self):
        CG = CalculationGenerator(operation=self.operation, difficulty=self.difficulty)
        self.num1_temp, self.num2_temp, self.res_temp = map(str,CG.generate())
        self.num1, self.num2, self.res = map(spacing, (self.num1_temp, self.num2_temp, self.res_temp))
 
        
    def print_row(self, x, y):
        self.pdf.set_font("helvetica", "B", 24)
        
        temp_numbers= []
        temp_length = []
        for j in range(self.columns):
            self.numbers_generator()
            temp_numbers.append([self.num1, self.num2, self.res, self.num1_temp, self.num2_temp, self.res_temp])
            self.length = max(self.pdf.get_string_width(self.num1 + " ") + self.pdf.get_string_width("00"), self.pdf.get_string_width(self.res + " "))
            temp_length.append(self.length)
            
        blank = int(self.width - sum(temp_length))
        
        for j in range(self.columns):
            self.pos = x + j*temp_length[j-1] + j*blank/2
            self.num1, self.num2, self.res, self.num1_temp, self.num2_temp, self.res_temp = temp_numbers[j]
            self.length = temp_length[j]
            
            #line1
            self.pdf.set_xy(self.pos+self.length-self.pdf.get_string_width(self.num1), y)
            self.pdf.cell(txt=self.num1)
            
            #line2
            self.pdf.set_xy(self.pos+self.length-self.pdf.get_string_width(self.num2), y+self.pdf.font_size)
            self.pdf.cell(txt=self.num2)
            
            
            self.pdf.set_xy(self.pos, y+self.pdf.font_size)
            self.pdf.cell(txt=self.symbol[self.operation])
            
            #line3
            self.pdf.line(x1=self.pos,
                    y1=y+2*self.pdf.font_size,
                    x2=self.pos+self.length,
                    y2=y+2*self.pdf.font_size)
            
            #line4
            if self.operation == 'substraction':
                n = len(self.num1_temp)
                d = self.pdf.get_string_width('0')
                for k in range(n):
                    self.pdf.circle(x=self.pos+self.length-self.pdf.get_string_width(self.num1)+0.65*d+k*1.5*d,y=y+3*self.pdf.font_size,r=1,style='F')
            else:
                n = len(self.res_temp)
                d = self.pdf.get_string_width('0')
                for k in range(n):
                    self.pdf.circle(x=self.pos+self.length-self.pdf.get_string_width(self.res)+0.65*d+k*1.5*d,y=y+3*self.pdf.font_size,r=1,style='F')
            
            
            
        
    def print(self):
        self.start = 50
        self.inter_row = 70
        for i in range(self.rows):
           self.print_row(self.margin,self.margin+self.start+i*self.inter_row)
        
    def generate(self, path='generated_pdfs/test.pdf'):
        self.header()
        self.footer()
        self.print()
        self.pdf.output(path)
        
        
operation = rd.choice(["addition", "substraction", "multiplication", "division"])
difficulty = rd.choice(["easy", "medium", "hard"])
# operation = 'addition'
# difficulty = 'easy'
WG = WorksheetGenerator(operation, difficulty)
WG.generate()
        
        
    
        

        
        
        

