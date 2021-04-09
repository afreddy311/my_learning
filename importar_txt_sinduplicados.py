#para instalar python -3.9 -m pip install pandas
import pandas as pd
# Para analizar arreglos
import numpy as np

def importar_archivotxt_y_mostrar_sinduplicados():
    #solucion 0 :
    #archivo_nombre = 'C:/Users/Freddy/Desktop/Prueba1_luis.txt'
    #archivo = open(archivo_nombre,mode='r')
    #texto = archivo.readlines()
    #archivo.close()
    #print (len(texto))
    
    # convertir a filas y columnas con panda desde txt
    #df = pd.read_fwf('C:/Users/Freddy/Desktop/Prueba1_luis.txt',header=None)

    #Solución 1: Como formatear un archivo sin delimitadores por posiciones
    #columnas = [(0,4),(4,25),(111,5)]
    #columnas = [(0,4),(4,25),(29,2211)]
    #columnas = [(0,3),(3,4),(4,29),(29,109),(109,189),(189,197),(197,212),(212,292),(292,372),(372,412),(412,492),(492,496),(496,509),(509,514),(514,519),(519,529),(529,537),(537,577),(577,592),(592,597),(597,605),(605,665),(665,673),(673,681),(681,689),(689,769),(769,849),(849,857),(857,865),(865,905),(905,945),(945,985),(985,1000),(1000,1008),(1008,1023),(1023,1036),(1036,1051),(1051,1054),(1054,1062),(1062,1063),(1063,1066),(1066,1074),(1074,1078),(1078,1084),(1084,1092),(1092,1096),(1096,1104),(1104,1105),(1105,1120),(1120,1121),(1121,1146),(1146,1151),(1151,1152),(1152,1153),(1162,1242),(1242,1247),(1247,1252),(1252,1260),(1260,1275),(1275,1290),(1290,1298),(1298,1306),(1306,1321),(1321,1334),(1321,1334),(1347,1350),(1350,1355),(1355,1370),(1370,1375),(1375,1390),(1390,1395),(1395,1410),(1410,1415),(1415,1430),(1430,1445),(1445,1450),(1450,1463),(1463,1467),(1467,1507),(1507,1547),(1547,1548),(1548,1549),(1549,1550),(1550,1551),(1551,1552),(1552,1560),(1560,1568),(1568,1608),(1608,1648),(1648,1663),(1663,1664),(1664,1667),(1667,1682),(1682,1697),(1697,1712),(1712,1727),(1727,1735),(1735,1745),(1745,1765),(1765,1805),(1805,1806),(1806,1814),(1814,1834),(1834,1842),(1842,1867),(1867,1875),(1875,1880),(1880,1895),(1895,1910),(1910,1925),(1925,1933),(1933,1943),(1943,1963),(1963,1983),(1983,2003),(2003,2023),(2023,2038),(2038,2048),(2048,2058),(2058,2068),(2068,2098),(2098,2128),(2128,2138),(2138,2143),(2143,2148),(2148,2151),(2151,2159),(2159,2164),(2164,2172),(2172,2187),(2187,2192),(2192,2212),(2212,2214)]
    #df = pd.read_fwf('C:/Users/Melanie/Downloads/Carga de G1/Prueba.txt',colspecs=columnas,header=None)
    #print(df.head())
    #print(df)

    #Solución 2: Como formatear un archivo por longitudes con cabecera
    #columnas = [(0,3),(3,4),(4,29),(29,109),(109,189),(189,197),(197,212),(212,292),(292,372),(372,412),(412,492),(492,496),(496,509),(509,514),(514,519),(519,529),(529,537),(537,577),(577,592),(592,597),(597,605),(605,665),(665,673),(673,681),(681,689),(689,769),(769,849),(849,857),(857,865),(865,905),(905,945),(945,985),(985,1000),(1000,1008),(1008,1023),(1023,1036),(1036,1051),(1051,1054),(1054,1062),(1062,1063),(1063,1066),(1066,1074),(1074,1078),(1078,1084),(1084,1092),(1092,1096),(1096,1104),(1104,1105),(1105,1120),(1120,1121),(1121,1146),(1146,1151),(1151,1152),(1152,1153),(1162,1242),(1242,1247),(1247,1252),(1252,1260),(1260,1275),(1275,1290),(1290,1298),(1298,1306),(1306,1321),(1321,1334),(1321,1334),(1347,1350),(1350,1355),(1355,1370),(1370,1375),(1375,1390),(1390,1395),(1395,1410),(1410,1415),(1415,1430),(1430,1445),(1445,1450),(1450,1463),(1463,1467),(1467,1507),(1507,1547),(1547,1548),(1548,1549),(1549,1550),(1550,1551),(1551,1552),(1552,1560),(1560,1568),(1568,1608),(1608,1648),(1648,1663),(1663,1664),(1664,1667),(1667,1682),(1682,1697),(1697,1712),(1712,1727),(1727,1735),(1735,1745),(1745,1765),(1765,1805),(1805,1806),(1806,1814),(1814,1834),(1834,1842),(1842,1867),(1867,1875),(1875,1880),(1880,1895),(1895,1910),(1910,1925),(1925,1933),(1933,1943),(1943,1963),(1963,1983),(1983,2003),(2003,2023),(2023,2038),(2038,2048),(2048,2058),(2058,2068),(2068,2098),(2098,2128),(2128,2138),(2138,2143),(2143,2148),(2148,2151),(2151,2159),(2159,2164),(2164,2172),(2172,2187),(2187,2192),(2192,2212),(2212,2214)]
    df = pd.read_fwf('C:/Users/Freddy/Desktop/Prueba1_luis.txt',widths=[3,1,25,80,80,8,15,80,80,40,80,4,13,5,5,10,8,40,15,5,8,60,8,8,8,80,80,8,8,40,40,40,15,8,15,13,15,3,8,1,3,8,4,6,8,4,8,1,15,1,25,5,1,1,89,5,5,8,15,15,8,8,15,13,13,3,5,15,5,15,5,15,5,15,15,5,13,4,40,40,1,1,1,1,1,8,8,40,40,15,1,3,15,15,15,15,8,10,20,40,1,8,20,8,25,8,5,15,15,15,8,10,20,20,20,20,15,10,10,10,30,30,10,5,5,3,8,5,8,15,5,20,2],header=None)
    df.columns = ['regcct','dmacctg','dmacct','dmaddr1','dmaddr2','dmagency','dmamtdlq','dmbaddr1','dmbaddr2','dmbcity','dmbname','dmbpext','dmbphone','dmbranch','dmbstate','dmbzip','dmccsdt','dmcity','dmcurbal','dmdays','dmdlqdt','dmemail','dmhostup','dminacct','dmlstcon','dmname','dmname2','dmnxtcon','dmofficr','dmp1','dmp2','dmp3','dmpayamt','dmpaydt','dmpayoff','dmphone','dmppamt','dmppbrok','dmppdue','dmppflag','dmppkept','dmppmade','dmprevq','dmprod','dmqchgdt','dmque','dmreact','dmreassg','dmresv1','dmrevcod','dmssnum','dmstate','dmstatus','dmzip','u1namecob','u1arcod1','u1arcod2','u1bthdt','u1capven','u1currency','u1ext1','u1ext2','u1intvdo','u1phone2','u1phone1','u1docvenc','u1cntbed','u1mntbed','u1cntbolcom','u1mntbolcom','u1cnticom','u1mnticom','u1cntbolab','u1mntbolab','u1quiebra','u1dacode','u1dphone','u1dpext','u1sexo','u1empresa','u1segdev','u1segvid','u1sedgin','u1segces','u1segotr','u1fecing','u1fecpcom','u1dirpostal','u1tienda','u1cupo','u1taradic','u1diapago','u1sdoliq','u1avance','u1savance','u1pagmin','u1vcpagmin','u1tipcar','u1score','u1marseg','u1castigo','u1feccar','u1fallecido','u1fchfall','u1msiniestr','u1fchsinies','u1tramo','u1ssnum','u1sir','u1ajuste','u1feccast','u1estatus','u1noasignar','u1seguros','u1lisblanca','u1inubicable','u1segcast','u1segvig','u1scrreac','u1scrprev','u1pdmesant','u1pdmesact','u1flujo','u1numinst','u1numprot','u1dicom','u1infocam','u1daystrx','u1datetrx','u1amttrx','u1cuotatrx','u1tipotrx','u1vehiculo']
    print(df)

    #listar solo la columna dmacct
    print(df.dmacct)

    # aquí puedo saber la cantidad de duplicados de la columna
    print(df['dmacct'].duplicated().sum())

    # aquí puedo saber cuales son los duplicados de la columna
    duplicates = df[df['dmacct'].duplicated(keep=False)]['dmacct'].tolist()
    print (duplicates)

    #Listar los registros duplicados- Pendiente corregir
    #set_duplicates = set(duplicates)
    #for r in set_duplicates:
    #    dup = df[df['dmacct'] == r]
    #    df.loc[dup.iloc[1,:].name, 'dmacct'] = df.loc[dup.iloc[1,:].name]['dmacct'] + 'z'

    # aquí listo el archivo sin los registros duplicados    
    print(df.sort_values('dmacct').drop_duplicates(subset='dmacct', keep="first"))
    # aquí verifico que no hay más duplicados
    print(df.duplicated().sum())






    
      
    
        

 
