
def calculadora_01():
    deuda_inicial = float(input("cuanto es tu deuda ?\n")) # 50000
    tasa = (float(input("cual es la tasa del prestamo \n"))) #3%
    pago_mensual = (float(input("cuanto es su pago mensual \n" ))) #1000
    meses_para_pagar = (int(input("cuantso meses desea el prestamo\n"))) #24
    # agregar intereses
    tasa_mensual = tasa/100/12

    for i in range(meses_para_pagar) :

        interes_mensual = deuda_inicial*tasa_mensual
        deuda_inicial = deuda_inicial + interes_mensual
        if deuda_inicial-pago_mensual < 0 :
            print("solo te falta una cuota de", deuda_inicial)
            print("tu terminas de pagar tu cuota en", i+1 , "meses")

    #Pago mensual
    deuda_inicial = deuda_inicial - pago_mensual

    # imprimir los resultados 
    print("pagó ", pago_mensual,"y su interes fue de " ,interes_mensual,"este mes",end=' ')
    print("ahora debe", deuda_inicial)                          

calculadora_01()