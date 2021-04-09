def disponibilidad_de_peliculas():
    movies_del_dia = {'titanic': '10 pm', 'betty': '11 pm','pianista':'9 pm'}
    print('tenemos las siguientes peliculas')
    for a in movies_del_dia :
        print(a)
    
    movie = input("Que pelicula quiere ver\n")
    horario = movies_del_dia.get(movie)
    if horario == None :
        print('la pelicula no esta disponible')
    else:
        print('El horario para su pelicula es'+ ' ' + str(horario))
    
disponibilidad_de_peliculas()
    