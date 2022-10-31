class Cliente:
    def __init__ (self,nombre,apellido,fecha_de_nacimiento,dni):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_de_nacimiento
        self.dni = dni

class Despegar:
    def __init__ (self):
        self.bancas = []
        self.compras = []
    
    def agregar_banca(self,nuevo_banca):
        self.bancas.append(nuevo_banca)

    def comprar_banca(self,comprador,numero_banca):
        for banca in self.bancas:
            if banca.numero() == numero_banca and not banca.vendido() and not banca.reservado() or banca.numero() == numero_banca and not banca.vendido() and comprador.dni == banca.reserva["dni"]:
                banca.pasajero(comprador)
                self.compras.append({"nombre":comprador.nombre,
                                     "apellido":comprador.apellido,
                                     "dni":comprador.dni,
                                     "banca nro":banca.numero
                                    })

    def reservar_banca(self,comprador):
        for banca in self.bancas:
            if not banca.vendido() and not banca.reservado():
               banca.reserva_pasajero(comprador)
               self.reservas.append({"nombre":comprador.nombre,
                                     "apellido":comprador.apellido,
                                     "dni":comprador.dni,
                                     "banca nro":banca.numero
                                    })

    def desreservar_banca(self,numero_banca):
        for banca in self.bancas:
            if banca.numero() == numero_banca and banca.reservado():
               banca.desreservar()    

class Banca:
    def __init__ (self,numero_banca):
        self.numero_banca = numero_banca
        self.comprador = None
        self.vendido = False
        self.esta_reservado = False
        self.reservas = []

    def desreservar(self):
        self.comprador = None
        self.esta_reservado = False

    def numero(self):
        return self.numero_banca   

    def esta_vendido(self):
        return self.esta_vendido

    def reservado(self):
        return self.esta_reservado    

    def pasajero(self,pasajero):
        self.comprador = pasajero 
        self.esta_vendido = True

    def reserva_pasajero(self,pasajero):
        self.comprador = pasajero
        self.esta_reservado = True          




           