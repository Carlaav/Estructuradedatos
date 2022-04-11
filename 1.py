
class Bloque: 
    # Un bloque es un conjunto de instrucciones ejecutadas 
    # unas detrás de otras. 
    def __init__(self): 
        # Por defecto, un bloque no contiene ninguna instrucción. 
        self.instrucciones = [] 
 
    def agregarInstruction(self, instruccion):
        self.instrucciones.append(instruccion)

    def hacerInstrucciones(self):
        for instruccion in self.instrucciones:
            instruccion.codigo()
            self.instrucciones.remove(instruccion)
 
class Si: 
    # Representa una instrucción 'if'. 'condicion' es una cadena 
    # de caracteres que contiene la evaluación de la condición, 
    # 'entonces' es el bloque de instrucciones ejecutadas si la condición 
    # se verifica, 'si_no' es el bloque de instrucciones ejecutadas 
    # si no se verifica. 
 
    def __init__(self, condicion, entonces, si_no): 
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no

    def parte_izquierda(self, datos):
        espacios = datos.split(" ")
        evaluacion = int(espacios[0]) + int(espacios[2])
        return evaluacion
    
    def codigo(self):
        izq = self.parte_izquierda(self.condicion)
        der = int(self.condicion.split(" ")[4])
        if izq == der:
            self.entonces.codigo()
        else:
            self.si_no.codigo()
 
class MientrasQue: 
    # Representa una instrucción 'while'. 
    # 'condicion' es una cadena que contiene el valor evaluado 
    # para decidir si el bucle continúa o no, 
    # 'bloque' es la secuencia de instrucciones ejecutadas en bucle. 
    def __init__(self, condicion, bloque): 
        self.condicion = condicion 
        self.bloque = bloque
        self.codigo()
        

    def codigo(self):
        while self.condicion:
            self.bloque.hacerInstrucciones()
            if len(self.bloque.instrucciones) == 0:
                break

 
class Mostrar: 
    # Una instrucción para mostrar un mensaje 
    # en salida estándar. 
    def __init__(self, mensaje): 
        self.mensaje = mensaje

    def codigo(self):
        print(self.mensaje)



#Funciona solo para el ==, se pueden cambiar los valores sin problemas y funciona igual que es lo que se pide
    
mostrar_ok = Mostrar('"OK"')
mostrar_ko = Mostrar('"KO"')
alternativa = Si("2 + 2 == 4", mostrar_ok, mostrar_ko)
bloque_alternativa = Bloque()
bloque_alternativa.agregarInstruction(alternativa)


bucle = MientrasQue(True, bloque_alternativa)