
import ast
ruta =  "c:/Users/diego/OneDrive/Documentos/ProyectoII_Diego_Rodriguez/BasedePersonas.txt"
#Es la ubicacion del txt con la base de datos
import requests
import json

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":""}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "90c2b8b002mshc23f61200f8d6d6p1765bdjsn9c69c1b3ac52"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


dicc = response.json()

def ImpresiondeTop (Lista,Diccionario):
    n= 1
    while n < 11:
        print(str(n) + ".   " + Lista[n-1]+ " : " + str(Diccionario[Lista[n-1]]))
        n += 1
    return

def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid

def pedirNumeroEnteroValidado(messages = "Ingrese un numero Enter0"):
    num = input(messages)
    while not validarEntero(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return int(num)  

def rellenarBD(diccionario):
    archivo = open(ruta, "r")
    jdic = archivo.read()
    diccionario = ast.literal_eval(jdic)
    archivo.close()
    return diccionario

def actualizaBD (dic):
    archivo = open(ruta, "w")
    archivo.write (str(dic))
    archivo.close()
    print ("Base de datos actualizada")
    return

class Persona ():
    def __init__(self,Nombres,Apellidos,Edad):
        self.Nombres = Nombres
        self.Apellidos = Apellidos
        self.Edad = Edad

class No_infectado (Persona):
    def __init__(self,Nombres,Apellidos,Edad,estado,numero):
        Persona.__init__(self,Nombres,Apellidos,Edad)
        self.estado = estado
        self.numero = numero

    def orden (self):
        return{
            "Nombres" : self.Nombres,
            "Apellidos": self.Apellidos,
            "Edad": self.Edad,
            "Estatus" : self.estado,
            "Telefono": self.numero
        }

class Posible_infectado (Persona):
    def __init__(self,Nombres,Apellidos,Edad,estado,direccion,ciudad,stade):
        Persona.__init__(self,Nombres,Apellidos,Edad)
        self.estado = estado
        self.direccion = direccion
        self.ciudad =ciudad
        self.stade = stade

    def orden (self): 
         return{
            "Nombres" : self.Nombres,
            "Apellidos": self.Apellidos,
            "Edad": self.Edad,
            "Estatus" : self.estado,
            "Lugar": [self.direccion, self.ciudad , self.stade]
            }

class Infectado (Posible_infectado):
    def __init__ (self,Nombres,Apellidos,Edad,estado,direccion,ciudad,stade,doctor):
        Posible_infectado.__init__(self,Nombres,Apellidos,Edad,estado,direccion,ciudad,stade)
        self.doctor = doctor

    def orden (self): 
         return{
            "Nombres" : self.Nombres,
            "Apellidos": self.Apellidos,
            "Edad": self.Edad,
            "Estatus" : self.estado,
            "Lugar": [self.direccion, self.ciudad , self.stade],
            "Doctor" : self.doctor
            }


print("="*150)
print("Bienvenido al prorgama de investigacion del coronavirus:")
Sesion = 0
while Sesion == 0:
    eleccion = pedirNumeroEnteroValidado('''
    Ingrese el numero si quieres:
    1) Ingresar usuario
    2) Ver estadisticas mundiales
    3) Salir
    ''')
    while eleccion != 1 and eleccion != 2 and eleccion !=3 :
        print("Coloque lo sugerido")
        eleccion = pedirNumeroEnteroValidado('''
    Ingrese el numero si quieres:
    1) Ingresar usuario
    2) Ver estadisticas mundiales
    3) Salir
    ''')
    if eleccion == 1:
        print("="*150)
        #Modulo #1
        BasedeDatos = {}
        archivo = open(ruta, "r")
        jdic = archivo.read()
        BasedeDatos = ast.literal_eval(jdic)
        archivo.close()
        registro = 0
        Sintomas = None
        while registro == 0:
            Nombres = str(input("Ingrese sus nombres: "))
            Apellidos = str(input("Ingrese sus apelidos: "))
            Nombre_completo = Nombres + " " + Apellidos
            Edad = pedirNumeroEnteroValidado("Indique su edad: ")
            Sintomas = 0
            Seleccion = ["Si", "No"]
            #Cuestionario de infeccion
            Secreciones = str(input("¿Tiene secreciones? Si[s] No[n] "))
            while Secreciones.lower() != "s" and Secreciones.lower() != "n":
                print ("Coloque lo indicado")
                Secreciones = str(input("¿Tiene secreciones? Si[s] No[n] "))
            if Secreciones.lower()== "s":
                Sintomas +=1
                Secreciones = Seleccion[0]
            elif Secreciones.lower() == "n":
                Secreciones = Seleccion[1]


            Garganta = str(input("¿Tiene dolor de garganta? Si[s] No[n] "))
            while Garganta.lower() != "s" and Garganta.lower() != "n":
                print ("Coloque lo indicado")
                Garganta = str(input("¿Tiene dolor de garganta? Si[s] No[n] "))
            if Garganta.lower()== "s":
                Sintomas +=1
                Garganta = Seleccion [0]
            elif Garganta.lower()== "n":
                Garganta = Seleccion [1]


            Tos = str(input("¿Tiene tos? Si[s] No[n] "))
            while Tos.lower() != "s" and Tos.lower() != "n":
                print ("Coloque lo indicado")
                Tos = str(input("¿Tiene tos? Si[s] No[n] "))
            if Tos.lower()== "s":
                Sintomas +=1
                Tos = Seleccion[0]
            elif Tos.lower()== "n":
                Tos = Seleccion[1]

            Fiebre = str(input("¿Tiene fiebre? Si[s] No[n] "))
            while Fiebre.lower() != "s" and Fiebre.lower() != "n":
                print ("Coloque lo indicado") 
                Fiebre = str(input("¿Tiene fiebre? Si[s] No[n] "))
            if Fiebre.lower()== "s":
                Sintomas +=1
                Fiebre = Seleccion[0]
            elif Fiebre.lower()== "n":
                Fiebre = Seleccion[1]

            Respirar =str(input("¿Tiene dificultad para respirar? Si[s] No[n] "))
            while Respirar.lower() != "s" and Respirar.lower() != "n":
                print ("Coloque lo indicado") 
                Respirar =str(input("¿Tiene dificultad para respirar? Si[s] No[n] "))
            if Respirar.lower() == "s":
                Sintomas += 1
                Respirar = Seleccion[0]
            elif Respirar.lower() == "n":
                Respirar = Seleccion[1]
            print("-"*100)
            print('''Datos del usuario:
            Nombre completo: {}
            Edad: {}
            ¿Tiene secreciones?: {}
            ¿Tiene dolor de garganta?: {}
            ¿Tiene tos?: {}
            ¿Tiene fiebre?: {}
            ¿Tiene dificultad para respirar?: {}
            '''.format(Nombre_completo, Edad, Secreciones, Garganta,Tos,Fiebre, Respirar))

            preguntar = str(input("¿Sus datos estan correcto? Si[s] No[n] "))
            while preguntar.lower() != "s" and preguntar.lower() != "n":
                print ("Coloque lo indicado")
                preguntar = str(input("¿Sus datos estan correcto? Si[s] No[n] "))

            if preguntar.lower() == "s":
                registro = 1
        #Clasificacion del usuario
        if Sintomas ==0:
            Status = "No infectado"
            print('''Segun sus respuestas usted se encuentra en el estado:
            {}

            Recuerde que este cuestionario no es la verdad absoluta'''.format(Status))

            Numero = pedirNumeroEnteroValidado("Ingrese su numero telefonico: ")
            BasedeDatos[Nombre_completo] = No_infectado(Nombres, Apellidos, Edad, Status,Numero).orden()

        elif Sintomas ==1 or Sintomas==2:
            Status = "En revision"
            print('''Segun sus respuestas usted se encuentra en el estado:
            {}

            Recuerde que este cuestionario no es la verdad absoluta'''.format(Status))

            Numero = pedirNumeroEnteroValidado("Ingrese su numero telefonico: ")
            BasedeDatos[Nombre_completo] = No_infectado(Nombres, Apellidos, Edad, Status,Numero).orden()

        elif Sintomas == 3 or Sintomas ==4:
            Status = "Posible infectado"
            print('''Segun sus respuestas usted se encuentra en el estado:
            {}

            Recuerde que este cuestionario no es la verdad absoluta'''.format(Status))
            estado = str(input("Colque el estado donde estara en cuarentena: "))
            ciudad =str(input("Colque la ciudad donde estara en cuarentena: "))
            direccion = str(input("Colque la direccion donde estara en cuarentena: "))
            BasedeDatos[Nombre_completo] = Posible_infectado (Nombres, Apellidos, Edad, Status, direccion, ciudad,  estado).orden()

        elif Sintomas == 5:
            Status = "Infectado"
            print('''Segun sus respuestas usted se encuentra en el estado:
            {}

            Recuerde que este cuestionario no es la verdad absoluta'''.format(Status))
            estado = str(input("Colque el estado donde estara en cuarentena: "))
            ciudad =str(input("Colque la ciudad donde estara en cuarentena: "))
            direccion = str(input("Colque la direccion donde estara en cuarentena: "))
            doctor = str(input("Ingrese el nombre del doctor encargado: "))
            BasedeDatos[Nombre_completo] = Infectado(Nombres, Apellidos, Edad, Status, direccion, ciudad,  estado, doctor).orden()

        print("Usuario Ingresado")
        actualizaBD(BasedeDatos)
        cuestionario = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu principal o 1 si quiere salir del programa: ")
        while cuestionario != 0 and cuestionario != 1:
            print("Coloque lo sugerido")
            cuestionario = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu principal o 1 si quiere salir del programa: ")
        if cuestionario ==1:
            Sesion =1
    

    elif eleccion == 2:
        print("="*150)
        #Modulo2
        diccinfectados = {}
        for x in dicc ['data']['covid19Stats']:
            if x ['country'] in diccinfectados:
                diccinfectados[x ['country']] = diccinfectados[x ['country']] + x['confirmed']
            else: 
                diccinfectados[x ['country']] =  x['confirmed']

        dicciMuertos = {}
        for x in dicc ['data']['covid19Stats']:
            if x ['country'] in dicciMuertos:
                dicciMuertos[x ['country']] = dicciMuertos[x ['country']] + x['deaths']
            else: 
                dicciMuertos[x ['country']] =  x['deaths']

        diccsalvados = {}
        for x in dicc ['data']['covid19Stats']:
            if x ['country'] in diccsalvados:
                diccsalvados[x ['country']] = diccsalvados[x ['country']] + x['recovered']
            else: 
                diccsalvados[x ['country']] =  x['recovered']


        #Generacion de Tops

        top_infectados = []
        for x in diccinfectados:
            beta = False
            if len(top_infectados)== 0:
                top_infectados.append(x)
            elif len(top_infectados)!= 0:
                for y in top_infectados:
                    if diccinfectados[y] <= diccinfectados[x]:
                        top_infectados.insert((top_infectados.index(y)),x)
                        beta = True
                        break
            if beta == False:
                top_infectados.append(x)
        top_infectados.pop(0)

        top_Muetos = []              
        for x in dicciMuertos:
            beta = False
            if len(top_Muetos)== 0:
                top_Muetos.append(x)
            elif len(top_Muetos)!= 0:
                for y in top_Muetos:
                    if dicciMuertos[y] <= dicciMuertos[x]:
                        top_Muetos.insert((top_Muetos.index(y)),x)
                        beta = True
                        break
            if beta == False:
                top_Muetos.append(x)
        top_Muetos.pop(0)          


        top_salvados = []
        for x in diccsalvados:
            beta = False
            if len(top_salvados)== 0:
                top_salvados.append(x)
            elif len(top_salvados)!= 0:
                for y in top_salvados:
                    if diccsalvados[y] <= diccsalvados[x]:
                        top_salvados.insert((top_salvados.index(y)),x)
                        beta = True
                        break
            if beta == False:
                top_salvados.append(x)
        top_salvados.pop(0) 

        ingreso = pedirNumeroEnteroValidado('''Ingrese el numero indicado si:
        1) Ver estadisticas de un Pais 
        2) Ver top de paises infectados
        3) Ver top de paises con mas muetos
        4) Ver top de paises con mas sanados
        ''')
        while ingreso != 1 and ingreso != 2 and ingreso != 3 and ingreso != 4:
            print("Coloque lo sugerido")
            ingreso = pedirNumeroEnteroValidado('''Ingrese el numero indicado si:
        1) Ver estadisticas de un Pais 
        2) Ver top de paises infectados
        3) Ver top de paises con mas muetos
        4) Ver top de paises con mas sanados
        ''')
        if ingreso ==1:
            print("="*150)
            pais = str(input("Ingrese el nombre del pais en ingles:  " ))
            pais = pais.title()
            acceso = 0
            while acceso ==0:
                if pais in diccinfectados:
                    print("-"*100)
                    print('''{} tiene:
                    {} infectados
                    {} muertos
                    {} sanados'''.format(pais,diccinfectados[pais],dicciMuertos[pais],diccsalvados[pais]))
                    acceso = 1

                elif pais not in diccinfectados:
                    print("Pais no encontrado")
                    duda= str(input("¿Quieres volver a buscar? Si[s] No[n]  "))
                    while duda.lower() != "s" and duda.lower() != "n":
                        print("Coloque lo indicado")
                        duda= str(input("¿Quieres volver a buscar? Si[s] No[n]  "))
                    if duda == "s":
                        pais = str(input("Ingrese el nombre del pais en ingles: "))
                        pais = pais.title()

                    elif duda == "n":
                        acceso = 1

        elif ingreso ==2:
            print("="*150)
            print ("Top de paises con mas infectados: ")
            ImpresiondeTop(top_infectados,diccinfectados)

        elif ingreso ==3:
            print("="*150)
            print ("Top de paises con mas muertos: ")
            ImpresiondeTop(top_Muetos,dicciMuertos)

        elif ingreso == 4:
            print("="*150)
            print ("Top de paises con mas sanados: ")
            ImpresiondeTop(top_salvados,diccsalvados)

        cuestionario = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu principal o 1 si quiere salir del programa: ")
        while cuestionario != 0 and cuestionario != 1:
            print("Coloque lo sugerido")
            cuestionario = pedirNumeroEnteroValidado("Ingrese 0 si quiere volver al menu principal o 1 si quiere salir del programa: ")
        if cuestionario ==1:
            Sesion =1


    elif eleccion ==3:
        Sesion =1
print("="*150)
print("Hasta luego")
