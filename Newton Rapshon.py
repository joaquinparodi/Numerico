import os

def main():
    os.system("cls")
    xNew = []
    func = input("Function#> ") # Ingreso de funcion
    apro = input("AproxIni#> ")   # Aproximacion inicial
    erro = input("ErrorTol#> ")   # Tolerancia de error
    xNew.append(apro)
    E = 100\
    
    file = open("data.py", "w")
    file.close()
    file = open("data.py", "a")
    file.write("from sympy import *\n") # Importar SymPy para derivada
    file.write("x = symbols('x')\n")
    file.write(func)
    file.write("\ny_ = diff(y,x)")  # Derivada de funcion
    file.close()\
    
    import data\
    
    while (E >= erro):
        new = xNew[-1]-\
              (data.y.evalf(subs={data.x:xNew[-1]})\
               /data.y_.evalf(subs={data.x:xNew[-1]}))
        xNew.append(new)
        E = abs(xNew[-1]-xNew[-2])
        print ("\nNewAprox:",xNew[-1])
    
    print ("\n\nMetodo de Newton terminado...")
    print ("\nf(x) =",data.y,"\nf'(x) =",data.y_,"\nAproxIni.:",apro)
    print ("AproxFinal con Tol",erro,": ",xNew[-1])
    input("Mostrando resultados -Enter para salir-.")

main()

#- Cuando pide "Function#>" se escribe una funcion algebráica. Por ejemplo: y = x**2, o y = 2*x-3 ... siempre escribiendo "y ="...
#- Después pedirá un valor inicial; por ejemplo, para la función y = x**2, la raíz se encuentra en 0, podemos dar un valor inicial distinto de cero para iniciar...
#- Después pedirá una tolerancia de error, ésta se escribe por ejemplo 0.0001, 1e-4, o 10e-5 y así...
