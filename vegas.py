import random

def lasvegas():
    c=0
    while True:
        c+=1
        x=random.random()*50
        y=random.random()*50
        print(f"({x},{y})")
        if x*x+y*y<1:
            print(f"({x},{y}) {c} intentos")
            return

lasvegas()

def montecarlo():
    c=0
    for _ in range(100):
        c+=1
        x=random.random()*50
        y=random.random()*50
        print(f"({x},{y})")
        if x*x+y*y<1:
            print(f"({x},{y}) {c} intentos")
            return
        
        print("No existe punto")




