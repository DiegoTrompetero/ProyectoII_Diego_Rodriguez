import ast
ruta =  "c:/Users/diego/OneDrive/Documentos/ProyectoII_Diego_Rodriguez/BasedePersonas.txt"

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
    ciudad =str(input("Colque la ciudad donde estara en cuarentena:"))
    direccion = str(input("Colque la direccion donde estara en cuarentena: "))
    doctor = str(input("Ingrese el nombre del doctor encargado: "))
    BasedeDatos[Nombre_completo] = Infectado(Nombres, Apellidos, Edad, Status, direccion, ciudad,  estado, doctor).orden()

print("Usuario Ingresado")
actualizaBD(BasedeDatos)