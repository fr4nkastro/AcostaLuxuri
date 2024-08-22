class Accesorio: 
    def __init__(self, codigo, nombre, descripcion, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    def toJson(self):
        return {"codigo":self.codigo, "nombre":self.nombre,"descripcion":self.descripcion, "precio":self.precio}