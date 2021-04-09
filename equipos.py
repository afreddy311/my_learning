def elegir_alianza():
    #Ingresar equipo y Elegir alianza de una lista de equipos
    equipos = ['alianza' , 'melgar' , 'municipal' , 'boys' , 'cristal']
    
    for i in range(5) : 
        print(equipos)
        eleccion = input("De que equipo eres\n")
        if eleccion == equipos[0]:
            print('Eres el mejor')
            break
        else :
            equipos.remove(eleccion)

elegir_alianza()
