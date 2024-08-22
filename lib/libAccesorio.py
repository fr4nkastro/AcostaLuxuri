from lib.accesorio import Accesorio
import json
class LibAccesorio:
    def create(self, codigo, nombre, descripcion, precio):
        accesorio = Accesorio(codigo, nombre, descripcion, precio)
        file = open("data/accesorios.json")
        j = json.load(file)
        j = j + [accesorio.toJson()]
        file = open("data/accesorios.json","w")
        json.dump(j,file,ensure_ascii=False, indent=4)
        file.close()
        return True
    
    def get_accesorios(self):
        file = open("data/accesorios.json")
        j = json.load(file)
        list = []
        for x in j:
            list.append(Accesorio(x['codigo'],x['nombre'],x['descripcion'],x['precio']))
        return list 
    
    def get_accesorios_by_codigo(self, codigo):
        file = open("data/accesorios.json")
        j = json.load(file)
        for x in j: 
            if(x['codigo']==codigo):
                return Accesorio(x['codigo'],x['nombre'],x['descripcion'],x['precio'])
        return None
    
    def edit(self, codigo, nombre, descripcion, precio):
        file = open("data/accesorios.json")
        j = json.load(file)
        for x in j: 
            if(x['codigo']==codigo):
                x['nombre'] = nombre
                x['descripcion']= descripcion
                x['precio']= precio
                file = open("data/accesorios.json","w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def eliminar(self, codigo):
        file = open("data/accesorios.json")
        j = json.load(file)
        for i in range(0,len(j)): 
            if(j[i]['codigo']==codigo):
                j = j[:i]+ j[i+1:]
                file = open("data/accesorios.json","w")
                json.dump(j,file,ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
    
    def get_accesorios_by_descripcion(self, descripcion):
        file = open("data/accesorios.json")
        j = json.load(file)
        list = []
        for x in j: 
            if(x['descripcion']==descripcion):
                list.append(Accesorio(x['codigo'],x['nombre'],x['descripcion'],x['precio'])) 
        return list
