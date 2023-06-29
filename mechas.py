class mechas:
    numero_de_atencion=''
    fecha='0'
    descripcion_atencion=''
    costo=0
    nombre_cliente=''

    def __int__(self):
        self.numero_de_atencion='A-000'
        self.fecha='00/00/0000'
        self.descripcion_atencion='nose que colocar aca'
        self.nombre_cliente='juanilo gigante'
        self.costo=20000

    def setnumero_de_atencion(self, codigo):
        if codigo[0:1].isalpha() and codigo[1:2]== '-' and codigo[2:4].isdigith():
            self.numero_de_atencion=codigo
            return True
        else:
            print("formato de codigo incorrecto Ej. A-014")
            return False

    def setcosto(self, costo):
        if costo >= 20000:
            self.costo=costo
            return True
        else:
            print("el costo no es >=20000 pesos")
            return False

    def setnombre_cliente(self, nombre):
        if len(nombre) >=5:
            self.nombre_cliente= nombre
            return True
        else:
            print("el nombre debe de tener un largo de 5 caracteres")
            return False