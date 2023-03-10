import turtle 
import time
import re
from decorators import *
from fractal_dict import fract_info
'''
кодовые обозначения

F - идти вперёд, параметр: длина
K - идти вперёд, не рисуя: длина
U - поднять перо, параметров нет
D - опустить перо, параметров нет
+ - поворот налево, параметр: угол поворота
- - поворот направо, параметр: угол поворота
[ - начало повторяемой части
] - конец повторяемой части

'''





class SystemL:

    def __init__(self,t,axiom,width,length,angle,):
        self.state_list = list(axiom.split())    # массив с набором команд (F,+,-)
        self.state = axiom
        self.width = width                  # толщина линии рисования
        self.length = length                # длина одного линейного сигмента
        self.angle = angle                  # фиксированный угол поворота
        self.t = t                          # черепашка
        self.rules = {}                     #словарь правил
        self.t.pensize(self.width)          # установка толщины пера
        
    def set_turtle(self,x,y,angle,width):
        self.width = width
        self.t.penup()
        self.t.goto(x,y)
        self.t.pendown()
        self.t.seth(angle)
        self.t.pensize(self.width)

    def add_rules(self, rules): #на вход подавать кортеж содержащий кортежи-правила
        for rule in rules:
            self.rules[rule[0]] = rule[1]

    def generate_path(self,iter):
        for n in range(iter):
            #self.length = self.length / iter
            for key,value in self.rules.items():
                #заменяем F на правило, при этом понижаем регистр, чтобы при большом количестве правил они не наслаивались
                self.state = self.state.replace(key,value.lower()) 

            self.state = self.state.upper()                   
    def draw_turtle(self,start_pos,start_angle):
        #границы
        #устанавливаем скоростной режим черепашки
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()
        turtle_stack = []
        for part in self.state:
            if part == 'F':
                self.t.forward(self.length)
            elif part == 'U':
                self.t.penup()
            elif part == 'D':
                self.t.pendown()
            elif part == '+':
                self.t.left(self.angle)
            elif part == '-':
                self.t.right(self.angle)
            #ветвление
            elif part == '[':
                turtle_stack.append((self.t.xcor(),self.t.ycor(),self.t.heading(),self.t.pensize()))
            elif part == ']':
                x,y,angle,w = turtle_stack.pop()
                self.set_turtle(x,y,angle,w)
                
            #специфичные значения
            elif part == 'K':
                self.t.penup()
                self.t.forward(self.length)
                self.t.pendown()


class Shape:


    @Repeater()
    #@classmethod
    def Do_Fract(self,iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos = (0,0),start_angle = 0): 
        turtle.tracer(speed,0)
        l_sys = SystemL(t,axiom,pen_width,f_len,angle)
        l_sys.add_rules(rules)
        l_sys.generate_path(iterations)
        l_sys.draw_turtle(start_pos, start_angle)


    #возле каждого фрактала помечено рекомендуемое число итераций
    #простые фракталы
    @staticmethod
    def Koh_line(iterations,speed = 1,f_len = 10,pen_width = 2):    # 2-8 итераций
        #расстояние по иксу равно 3**iter * f_len
        angle = 60
        axiom = 'F'
        rules = (('F', 'F+F--F+F'),)
        ots = 3**iterations * f_len/2
        start_pos = (0-ots/2,0-ots/2)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Koh_star(iterations,speed = 1,f_len = 10,pen_width = 2):    # 4-7 итераций
        angle = 60
        axiom = 'F--F--F'
        rules = (('F','F+F--F+F'),)

        start_pos = (0-50*iterations,0+25*iterations)
        start_angle = 0

        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Koh_square(iterations,speed = 1,f_len = 10,pen_width = 2):  # 1-4 итераций
        angle = 90
        axiom = 'F+F+F'
        rules = (('F', 'F-F+F+FFF-F-F+F'),)

        start_pos = (0,0-50*iterations)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def crystal(iterations,speed = 1,f_len = 10,pen_width = 2):     # 3-6 итераций
        angle = 90
        axiom = 'F+F+F+F'
        rules = (('F', 'FF+F++F+F'),)

        start_pos = (0-50*iterations,0-50*iterations)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def curve_32seg(iterations,speed = 1,f_len = 10,pen_width = 2): # 1-3 итераций
        angle = 90
        axiom = 'F+F+F+F'
        rules = (('F', '-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+'),)
        start_pos = (0-100*iterations,0-100*iterations)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Dragon_Harter(iterations, speed = 1,f_len = 10,pen_width = 2):#4-13 итераций
        angle = 90
        axiom = 'FX'
        rules = (('FX', 'FX+FY+'),('FY','-FX-FY'))

        start_pos = (0,0)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Gilbert_curve(iterations, speed = 1,f_len = 10, pen_width = 2): #2-6 итераций
        angle = 90
        axiom = 'A'
        rules = (('A','+BF-AFA-FB+'),('B','-AF+BFB+FA-'))

        start_pos = (0-f_len*50,0+f_len*50)
        start_angle = -90

        fract = Shape()
        fract.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Serpin_triangle(iterations, speed = 1,f_len = 10, pen_width = 2):#
        angle = 60
        axiom = 'FXF--FF--FF--FF'
        rules = (('F','FF'),('X','--FXF++FXF++FXF--'))

        start_pos = (-200,-50)
        start_angle = 0

        fract = Shape()
        fract.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)
    @staticmethod
    def Gosper_curve(iterations,speed = 1,f_len = 10,pen_width = 2):
        angle = 60
        axiom = 'FL'
        rules = (('F',''),('L','FL-FR--FR+FL++FLFL+FR-'),('R','+FL-FRFR--FR-FL++FL+FR'))
        start_pos = (100,200)
        start_angle = 0

        fract = Shape()
        fract.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)

    #======================================
    #фракталы с ветвлением
    @staticmethod
    def Tree_Heart(iterations, speed = 1,f_len = 10, pen_width = 2): #4-8(шаг 20-5)
        angle = 60
        axiom = 'F'
        rules = (('F','FXF'),('X','[+FX][-FX]'),)
        start_pos = (0,0-400)
        start_angle = 90

        fract = Shape()
        fract.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)

    #======================================
    #авторские фракталы(сам реализовывал)
    @staticmethod #треугольник обратный серпинскому
    def Not_Serpin_triangle(iterations, speed = 1,f_len = 10, pen_width = 2):
        angle = 60
        axiom = 'FXF--FXF--FXF--FF'
        rules = (('F','FF'),('X','++FXF--FXF--FXF++'))
        start_pos = (-200,-50)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Cantor_set(iterations, speed = 1,f_len = 10, pen_width = 2):

        for iter in range(1,iterations+1):
            angle = 90
            axiom = "F"
            rules = (('F', 'FKF'),)
            ots = (3/2)**iterations * f_len/2
            start_pos = (-ots,-50*(iter-1))
            indent = 50
            iter_len = f_len
            fract = Shape()
            fract.Do_Fract(iter,speed,f_len,pen_width,angle,axiom,rules,start_pos)
    @staticmethod
    def Triangle_sieve(iterations,speed = 1,f_len = 10, pen_width = 2): #при увеличении глубины, повышать скорость(1_10+)
        angle = 60
        axiom = 'FX++FX++FX'
        rules = (('X','-FX++FX++F---'),)
        start_pos = (0,0)
        start_angle = 0
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos,start_angle)

    @staticmethod
    def Palochki(iterations, speed = 1,f_len = 10,pen_width = 2): # в процессе
        angle = 90
        axiom = 'XFFX'
        rules = (('X', '[+FX][-FX]'),)
        start_pos = (-200,-50)
        Shape.Do_Fract(iterations,speed,f_len,pen_width,angle,axiom,rules,start_pos)
        


#базовые параметры
width = 1920
height = 1080
screen = turtle.Screen()
screen.setup(width, height, 0, 0)
t =turtle.Turtle()
t.ht()
shape = Shape()
#================= основное тело
#@Repeater()
#shape.Triangle_sieve(5,2,10)

#================= не закрывает окно 
turtle.done()

#key_re = re.sub(r"([a-z]+)([, ]*)", lambda m: r"([-+]?\b\d+(?:\.\d+)?\b)" + m.group(2), key_re)