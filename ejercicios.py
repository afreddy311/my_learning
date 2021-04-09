import openpyxl as pyxl
import pandas as pd
import xlrd

def ejercicio_01():
    """ 
    operaciones aritmeticas
    division y multipicacion
    
    """

    #Ejercicio operaciones aritmeticas
    a = int(input("ingrese el valor de a\n"))
    b = int(input("ingrese el valor de b\n"))
    c = int(input("ingrese el valor de c\n"))
    resultado = (a**3 * (b**2-2*a*c))/2*b
    print(f"el resultado es {resultado}")

def ejercicio_02():
    #Ejerc operaciones logicas
    a = int(input("ingrese el valor de a\n"))
    b = int(input("ingrese el valor de b\n"))
    resultado = 3+5*8 < 3 & ((-6*4/3+2<2)) or (a>b)
    print(f"el resultado es {resultado}")

def ejercicio_03():
    #descuento del 15 %
    precio = float(input("ingrese el precio\n"))
    descuento = Precio * 0.15
    precio_final = precio-descuento
    print(f"su precio con descuento es $ {precio_final:.2f}")

def ejercicio_05():
#solicitar 2 numeros y arrojar cual es par
numero1 = int(input("ingrese un numero entero1\n"))
numero2 = int(input("ingrese un numero entero2\n"))
if numero1%2==0 and numero2%2 == 0 :
    print(f"los numeros pares son{numero1,numero2}")
elif numero1%2==0 and numero2%2 != 0 :
    print(f"{numero1} es numero par")
elif numero1%2!=0 and numero2%2 == 0:
    print(f"{numero2}es numero par")
else:
    print("ningun numero es par")


#Leer un excel #Como haria para imprimir 2 columnas

def ejercicio_04():
    plantilla_alianza = pyxl.load_workbook("C:/Users/Freddy/Desktop/Sample.xlsx")
    hoja1 = plantilla_alianza.get_sheet_by_name('Hoja1')
    #listar_varias_celdas=Hoja1['a1':'b3']
    for row in hoja1.iter_rows():
        nombre=row[0]
        posicion=row[1]
        partidos_jugados=row[2]
        print(nombre.value + ' ' + posicion.value + ' ' + str(partidos_jugados.value))
      

def ejercicio_06():
    archivo = 'C:/Users/Freddy/Desktop/Sample.xlsx'        
    df=pd.read_excel(archivo,sheet_name='Hoja1')
    print(df.head())
    jugador=input("Ingrese el jugador\n")
    is_jugador= df.loc[:, 'Nombre'] == jugador
    df_jugador = df.loc[is_jugador]
    print(df_jugador.head())


