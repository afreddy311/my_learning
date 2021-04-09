def suma_de_gastos():
    total = 0 
    gastos = []
    for i in range(7) :
        gastos.append(float(input("ingrese su gasto \n")))
        total = sum(gastos)
        print('has gastado en total',' ', total )

