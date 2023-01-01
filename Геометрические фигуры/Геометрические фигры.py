from abc import ABC, abstractmethod
import math
class tochkaP2:
    def __init__(self, num):
        self.x = int(input (f"Введите расположение по x точки {num}: "))
        self.y = int(input (f"Введите расположение по y точки {num}: "))
        num=num+1

class tochkaP3:
    def __init__(self, num):
        self.x = int(input (f"Введите расположение по x точки {num}: "))
        self.y = int(input (f"Введите расположение по y точки {num}: "))  
        self.z = int(input (f"Введите расположение по z точки {num}: "))
        num=num+1

class figure(ABC):
    
    def make():
        n = int(input("""Обозначающие номера фигур:
            Круг - 1;
            Треугольник - 2;
            Четырёхугольник - 3;
            Какого типа фигуру вы желаете добавит?
            """))
        if n == 1:
             f2.append(circle())
            
        elif n == 2:
             f2.append(triangle())
            
        elif n == 3:
             f2.append(quadrilateral())
             

    def perims(t, u, i):
        if u ==1:
            if t == 1:
                p = 2*math.pi*f2[i-1].rad
                return p
            if t == 2:
                if (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs( f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                else:
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)

                if (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs( f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                else:
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)

                s1 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs( f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                else:
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)

                if (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs( f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                else:
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)

                s2 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch3.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch3.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch3.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch3.x <= f2[i-1].toch1.x)):
                    x= abs( f2[i-1].toch1.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch3.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch3.x <= f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)
                else:
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)

                if (f2[i-1].toch3.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch3.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch3.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch3.y <= f2[i-1].toch1.y)):
                    y= abs( f2[i-1].toch1.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch3.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch3.y <= f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)
                else:
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)

                s3 = (math.sqrt(x**2 + y**2))

                p = s1 + s2 + s3

                return p

            if t == 3:
                if (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs( f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                else:
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)

                if (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs( f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                else:
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)

                s1 = (math.sqrt(x**2 + y**2))
                
                if (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs( f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                else:
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)

                if (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs( f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                else:
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)

                s2 = (math.sqrt(x**2 + y**2))
                
                if (f2[i-1].toch3.x >= 0 and f2[i-1].toch4.x >=0 and (f2[i-1].toch3.x > f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch3.x >= 0 and f2[i-1].toch4.x >=0 and (f2[i-1].toch3.x <= f2[i-1].toch4.x)):
                    x= abs( f2[i-1].toch4.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch4.x < 0 and (f2[i-1].toch3.x > f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch4.x < 0 and (f2[i-1].toch3.x <= f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)
                else:
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)

                if (f2[i-1].toch3.y >= 0 and f2[i-1].toch4.y >=0 and (f2[i-1].toch3.y > f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch3.y >= 0 and f2[i-1].toch4.y >=0 and (f2[i-1].toch3.y <= f2[i-1].toch4.y)):
                    y= abs( f2[i-1].toch4.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch4.y < 0 and (f2[i-1].toch3.y > f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch4.y < 0 and (f2[i-1].toch3.y <= f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)
                else:
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)

                s3 = (math.sqrt(x**2 + y**2))
                
                if (f2[i-1].toch4.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch4.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch4.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch4.x <= f2[i-1].toch1.x)):
                    x= abs( f2[i-1].toch1.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch4.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch4.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch4.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch4.x <= f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)
                else:
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)

                if (f2[i-1].toch4.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch4.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch4.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch4.y <= f2[i-1].toch1.y)):
                    y= abs( f2[i-1].toch1.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch4.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch4.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch4.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch4.y <= f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)
                else:
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)

                s4 = (math.sqrt(x**2 + y**2))
                
                p = s1 + s2 + s3 + s4
                return p
        elif u ==2:
            if t == 1:
                S = math.pi*(f2[i-1].rad**2)
                return S
            if t == 2:
                if (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs( f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                else:
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)

                if (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs( f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                else:
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)

                s1 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs( f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                else:
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)

                if (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs( f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                else:
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)

                s2 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch3.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch3.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch3.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch3.x <= f2[i-1].toch1.x)):
                    x= abs( f2[i-1].toch1.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch3.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch3.x <= f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)
                else:
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch1.x)

                if (f2[i-1].toch3.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch3.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch3.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch3.y <= f2[i-1].toch1.y)):
                    y= abs( f2[i-1].toch1.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch3.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch3.y <= f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)
                else:
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch1.y)

                s3 = (math.sqrt(x**2 + y**2))

                p = (s1 + s2 + s3)/2

                S = math.sqrt(p*(p-s1)*(p-s2)*(p-s3))
                return S

            if t == 3:
                if (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch1.x >= 0 and f2[i-1].toch2.x >=0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs( f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x > f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch1.x < 0 and f2[i-1].toch2.x < 0 and (f2[i-1].toch1.x <= f2[i-1].toch2.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)
                else:
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch2.x)

                if (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch1.y >= 0 and f2[i-1].toch2.y >=0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs( f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y > f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch1.y < 0 and f2[i-1].toch2.y < 0 and (f2[i-1].toch1.y <= f2[i-1].toch2.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)
                else:
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch2.y)

                s1 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch2.x >= 0 and f2[i-1].toch3.x >=0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs( f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x > f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch2.x)
                elif (f2[i-1].toch2.x < 0 and f2[i-1].toch3.x < 0 and (f2[i-1].toch2.x <= f2[i-1].toch3.x)):
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)
                else:
                    x= abs(f2[i-1].toch2.x - f2[i-1].toch3.x)

                if (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch2.y >= 0 and f2[i-1].toch3.y >=0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs( f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y > f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch2.y)
                elif (f2[i-1].toch2.y < 0 and f2[i-1].toch3.y < 0 and (f2[i-1].toch2.y <= f2[i-1].toch3.y)):
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)
                else:
                    y= abs(f2[i-1].toch2.y - f2[i-1].toch3.y)

                s2 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch3.x >= 0 and f2[i-1].toch4.x >=0 and (f2[i-1].toch3.x > f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch3.x >= 0 and f2[i-1].toch4.x >=0 and (f2[i-1].toch3.x <= f2[i-1].toch4.x)):
                    x= abs( f2[i-1].toch4.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch4.x < 0 and (f2[i-1].toch3.x > f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch3.x)
                elif (f2[i-1].toch3.x < 0 and f2[i-1].toch4.x < 0 and (f2[i-1].toch3.x <= f2[i-1].toch4.x)):
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)
                else:
                    x= abs(f2[i-1].toch3.x - f2[i-1].toch4.x)

                if (f2[i-1].toch3.y >= 0 and f2[i-1].toch4.y >=0 and (f2[i-1].toch3.y > f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch3.y >= 0 and f2[i-1].toch4.y >=0 and (f2[i-1].toch3.y <= f2[i-1].toch4.y)):
                    y= abs( f2[i-1].toch4.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch4.y < 0 and (f2[i-1].toch3.y > f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch3.y)
                elif (f2[i-1].toch3.y < 0 and f2[i-1].toch4.y < 0 and (f2[i-1].toch3.y <= f2[i-1].toch4.y)):
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)
                else:
                    y= abs(f2[i-1].toch3.y - f2[i-1].toch4.y)

                s3 = (math.sqrt(x**2 + y**2))

                if (f2[i-1].toch4.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch4.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)
                elif (f2[i-1].toch4.x >= 0 and f2[i-1].toch1.x >=0 and (f2[i-1].toch4.x <= f2[i-1].toch1.x)):
                    x= abs( f2[i-1].toch1.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch4.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch4.x > f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch1.x - f2[i-1].toch4.x)
                elif (f2[i-1].toch4.x < 0 and f2[i-1].toch1.x < 0 and (f2[i-1].toch4.x <= f2[i-1].toch1.x)):
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)
                else:
                    x= abs(f2[i-1].toch4.x - f2[i-1].toch1.x)

                if (f2[i-1].toch4.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch4.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)
                elif (f2[i-1].toch4.y >= 0 and f2[i-1].toch1.y >=0 and (f2[i-1].toch4.y <= f2[i-1].toch1.y)):
                    y= abs( f2[i-1].toch1.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch4.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch4.y > f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch1.y - f2[i-1].toch4.y)
                elif (f2[i-1].toch4.y < 0 and f2[i-1].toch1.y < 0 and (f2[i-1].toch4.y <= f2[i-1].toch1.y)):
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)
                else:
                    y= abs(f2[i-1].toch4.y - f2[i-1].toch1.y)

                s4 = (math.sqrt(x**2 + y**2))
               
                p = (s1 + s2 + s3 + s4)/2
                S = math.sqrt((p-s1)*(p-s2)*(p-s3)*(p-s4))
                return S

class circle(figure):
    def __init__(self):
        self.type = "circle"
        if P == 2:
            self.toch1 = tochkaP2(1)
        elif P == 3:
            self.toch1 = tochkaP3()
        self.rad = int(input("Введите радиус круга: "))
    def perimPlosh(self, i):
        self.perim = figure.perims(1, 1, i)
        self.plosh = figure.perims(1, 2, i)

class triangle(figure):
    def __init__(self):
        self.type = "triangle"
        self.toch1 = tochkaP2(1)
        self.toch2 = tochkaP2(2)
        self.toch3 = tochkaP2(3)
    def perimPlosh(self, i):
        self.perim = figure.perims(2, 1, i)
        self.plosh = figure.perims(2, 2, i)

class quadrilateral(figure):
    def __init__(self):
        self.type = "quadrilateral"
        self.toch1 = tochkaP2(1)
        self.toch2 = tochkaP2(2)
        self.toch3 = tochkaP2(3)
        self.toch4 = tochkaP2(4)
    def perimPlosh(self, i):
        self.perim = figure.perims(3, 1, i)
        self.plosh = figure.perims(3, 2, i)
d = 1
f2 = []
j=0
P = int(input("В каком пространстве желаете работать? Двухмерном - 2, трёхмерном - 3 (не реализовано)\n"))
while (d!=0):
    d = int(input("""Что желаете сделать?
           Добавить фигуру - 1
           Удалить фигуру из списка - 2
           Сотрировать список по площади - 3
           Показать список - 4
           Посчитать периметр и площадь фигур - 5
           Выйти - 0
           """))
    if (d==1):
        i1 = int(input("Сколько фигур желаете добавить? "))
        for i in range(i1):
            figure.make()

    elif (d==2):
        for k in f2:
            print (f"{f2.index(k)+1}.Фигура: {k.type}")
        n = int(input("\nВедите порядковый номер фигуры, которую желаете удалить: "))
        f2.pop(n-1)
    elif (d==3):
         list.sort(f2, key=lambda figure: figure.plosh)
    elif (d==4):
        for k in f2:
            print (f"""\n{f2.index(k)+1}.Фигура: {k.type}
            ----Периметр: {k.perim}
            ----Площадь: {k.plosh}
            """)
    elif (d==5):
        for k in f2:
            j=j+1
            k.perimPlosh(j)
    j=0

