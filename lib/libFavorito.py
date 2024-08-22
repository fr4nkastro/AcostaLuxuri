# lib/libFavorito.py

from lib.favorito import Favorito
import json

class LibFavorito:
    def create(self, user_email='johellydilia14@gmail.com', codigo=''):
        favorito = Favorito(user_email, codigo, )
        file = open("data/favoritos.json")
        j = json.load(file)
        j = j + [favorito.toJson()]
        file = open("data/favoritos.json", "w")
        json.dump(j, file, ensure_ascii=False, indent=4)
        file.close()
        return True

    def get_favoritos_by_user(self, user_email):
        file = open("data/favoritos.json")
        j = json.load(file)
        list = []
        for x in j:
            if x['user_email'] == user_email:
                list.append(Favorito(x['user_email'], x['codigo'], x['descripcion']))
        return list

    def eliminar_favorito(self, user_email, codigo):
        file = open("data/favoritos.json")
        j = json.load(file)
        for i in range(len(j)):
            if j[i]['user_email'] == user_email and j[i]['codigo'] == codigo:
                j = j[:i] + j[i+1:]
                file = open("data/favoritos.json", "w")
                json.dump(j, file, ensure_ascii=False, indent=4)
                file.close()
                return True
        return False
