#0/02/2024
# Ejemplo de tutoria
# Dwight Sutherland
# Simulador de creacion de personanjes tipo WoW


#________________________________Base de datos de personajes_______________________________________________________
personajes = {
    "raza":{
        
        "humanos":{
            "clase":{
                "guerrero":{
                    "stats":{
                        "vida": "1200",
                        "mana": "900"
                    }
                },
                "mago":{
                    "stats":{
                        "vida": "800",
                        "mana": "1200"
                    }
                },
            }
        },
        
        "orcos":{
            "clase":{
                "chaman":{
                    "stats":{
                        "vida": "900",
                        "mana": "1500"
                    },
                },
                "brujo":{
                    "stats":{
                        "vida": "800",
                        "mana": "1200"
                    },
                }
            }
            
            
        },
        
        "elfos":{
            "clase":{
                "druida":{
                    "stats":{
                        "vida": "2000",
                        "mana": "1300"
                    }
                },
                "mago":{
                    "stats":{
                        "vida": "600",
                        "mana": "1800"
                    }
                },
            }
        
        }
    }
}


#__________________________________________librerias_______________________________________________________
import uuid
import json
import os
from time import sleep

#__________________________________________Variables globales______________________________________________
data = {}
data["personajes_creados"] = []


    
#__________________________________________clases_______________________________________________________

class personaje():
    
    def __init__(self, nombre, raza, clase, vida, mana):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.mana = mana
        
    #__________________________________________Getters_______________________________________________________
        
    def get_nombre(self):
        return self.nombre
    def get_raza(self):
        return self.raza
    def get_clase(self):
        return self.clase
    def get_vida(self):
        return self.vida
    def get_mana(self):
        return self.mana
    
    #__________________________________________Setters_______________________________________________________
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_raza(self, raza):
        self.raza = raza
    def set_clase(self, clase):
        self.clase = clase
    def set_vida(self, vida):
        self.vida = vida
    def set_mana(self, mana):
        self.mana = mana
        
        
    def guardar_personaje(self, datos):
        data["personajes_creados"].append(datos)            # agrega datos a la lista de personajes creados
        pjs = data["personajes_creados"]
        archivo = open("personajes.json", "w")        # abre el archivo en modo escritura
        json.dump(pjs, archivo, indent=4)                       # guarda los datos en el archivo
        
    def ver_personajes(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        archivo = open("personajes.json", "r")        # abre el archivo en modo lectura
        pjs = json.load(archivo)                       # carga los datos del archivo
        print("\nPersonajes creados\n")
        for pj in pjs:
            print(f'ID: {pj["id"]}')
            print(f'Nombre: {pj["nombre"]}')
            print(f'Raza: {pj["raza"]}')
            print(f'Clase: {pj["clase"]}')
            print(f'Vida: {pj["vida"]}')
            print(f'Mana: {pj["mana"]}')
            print("\n")
        archivo.close()
        wait = input("\nPresione enter para continuar")
        
        
    def crear_personaje(self, raza, clase):
        vida = personajes["raza"][raza]["clase"][clase]["stats"]["vida"]
        mana = personajes["raza"][raza]["clase"][clase]["stats"]["mana"]
        nombre = input("\nIngrese el nombre del personaje\n > ")
        nuevo_personaje = personaje(nombre, raza, clase, vida, mana)
        datos = {
            "id": str(uuid.uuid4()),   # Genera un id unico con la libreria uuid utilizando el metodo uuid4
            "nombre": nuevo_personaje.get_nombre(),
            "raza": nuevo_personaje.get_raza(),
            "clase": nuevo_personaje.get_clase(),
            "vida": nuevo_personaje.get_vida(),
            "mana": nuevo_personaje.get_mana(),
        }
        
        self.guardar_personaje(datos)
        print("\nPersonaje creado con exito")
        wait = input("\nPresione enter para continuar")

        
    def menu_creacion(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nBienvenido al creador de personajes\n")
        print("Seleccione la raza de su personaje\n")
        print("1. humanos")
        print("2. orcos")
        print("3. elfos")
        raza = input("\n > ")
        raza = raza.lower()
        
        try:
            if raza == "1" or raza == "humanos":
                print("\nSeleccione la clase de su personaje\n")
                print("1. guerrero")
                print("2. mago")
                clase = input("\n > ")
                clase = clase.lower()
                raza = "humanos"
                
                if clase == "1" or clase == "guerrero":
                    clase = "guerrero"
                    self.crear_personaje(raza, clase)
                elif clase == "2" or clase == "mago":
                    clase = "mago"
                    self.crear_personaje(raza, clase)
                else:
                    print("\nComando no valido en la seleccion de clase")
                    return
                
                
            elif raza == "2" or raza == "orcos":                
                print("\nSeleccione la clase de su personaje\n")
                print("1. chaman")
                print("2. brujo")
                clase = input("\n > ")
                clase = clase.lower()
                raza = "orcos"
                
                if clase == "1" or clase == "chaman":
                    clase = "chaman"
                    self.crear_personaje(raza, clase)
                elif clase == "2" or clase == "brujo":
                    clase = "brujo"
                    self.crear_personaje(raza, clase)
                else:
                    print("\nComando no valido en la seleccion de clase")
                    return
                
                
                
            elif raza == "3" or raza == "elfos":
                print("\nSeleccione la clase de su personaje\n")
                print("1. druida")
                print("2. mago")
                clase = input("\n > ")
                clase = clase.lower()
                raza = "elfos"
                
                if clase == "1" or clase == "druida":
                    clase = "druida"
                    self.crear_personaje(raza, clase)
                    
                elif clase == "2" or clase == "mago":
                    clase = "mago"
                    self.crear_personaje(raza, clase)
                    
                else:
                    print("\nComando no valido en la seleccion de clase")
                    return
                
            else:
                print("\ncomando no valido en la seleccion de raza")
                return
        except Exception as e:
            print(f'Error: {e} at menu_creacion')
            sleep(5)
        
        
        
    def interfaz(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nBienvenido al simulador de creacion de personajes\n")
            print("1. Crear personaje")
            print("2. Ver personajes creados")
            print("3. Salir ")
            opcion = input("\n > ")
            opcion = opcion.lower()
            
            try:
                if opcion == "1" or opcion == "crear personaje":
                    self.menu_creacion()
                elif opcion == "2" or opcion == "ver personajes creados":    
                    self.ver_personajes()
                elif opcion == "3" or opcion == "salir":
                    print("\nAdios")
                    quit()
                else:
                    print("\nComando no valido en la seleccion de opcion")
                    return
            except Exception as e:
                print(f'Error: {e} at interfaz')
                sleep(5)
        
    
    
    
    
#__________________________________________Metodos_______________________________________________________


    


#__________________________________________Main_______________________________________________________



#driver

if __name__=='__main__':        # Sirve para que el codigo se ejecute solo si se llama desde este archivo
    pj = personaje("", "", "", "", "")
    pj.interfaz()
    
    