class Vista():
    def __init__(self):
        self.menu()

    def menu(self):
        print("1 para añadir al fichero dos entradas que usted elija")
        print("2 para ver el archivo escrito")
        print("3 para salir")

        entrada = 0

        while entrada != 1 or entrada != 2 or entrada != 3:
            try:
                entrada = int(input("Introduzca una opcion: "))
                if entrada == 1:
                    self.entradaDatos()
                elif entrada == 2:
                    self.verArchivo()
                elif entrada == 3:
                    print("Vuelva pronto o no")
                    break
                else:
                    print("Introduzca uno de los valores posibles por favor")
            except:
                print("Introduzca un numero entero por favor")
            

    def entradaDatos(self):
        self.entrada1 = str(input("Introduzca la primera entrada: "))
        self.entrada2 = str(input("Introduzca la segunda entrada: "))
        controlador = Controlador(self.entrada1, self.entrada2)
        Modelo(controlador.mayus1, controlador.mayus2)
    
    def verArchivo(self):
        try:
            f = open("Entrada.txt", "r")
            print(f.read())
            f.close()
        except:
            print("IMPOSIBLE ABRIR EL ARCHIVO")
        
class Controlador():
    def __init__(self, entrada1, entrada2):
        self.mayus1 = str(entrada1).upper()
        self.mayus2 = str(entrada2).upper()

class Modelo():
    def __init__(self, mayus1, mayus2):
        self.escribirArchivo(mayus1, mayus2)
    
    def escribirArchivo(self, mayus1, mayus2):
        f = open("Entrada.txt", "a")
        f.write(mayus1 + " " + mayus2)
        f.write("\n")
        f.close()
        print("Escrito al fichero con exito")



Vista()
