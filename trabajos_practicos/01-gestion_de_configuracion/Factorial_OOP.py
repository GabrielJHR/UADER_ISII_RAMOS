#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
class Factorial():
    def __init__(self) -> None:
        pass
    
    def factorial(self, num): 
        if num < 0: 
            print("Factorial de un número negativo no existe")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact
    
    def run(self, min, max):
        for num in range(min, max + 1):
            print("Factorial ",num,"! es ", self.factorial(num))


if len(sys.argv) == 1:
   num_min = int(input("Ingresar un minimo para calcular su factorial sin limite: "))
   num_max = int(input("Ingresar un maximo para calcular su factorial sin limite: "))
else:
    num_min=int(sys.argv[1])
    num_max=int(sys.argv[2])

factorial_obj = Factorial()
factorial_obj.run(1, num_max)
factorial_obj.run(num_min, 60)