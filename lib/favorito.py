# lib/favorito.py

class Favorito:
    def __init__(self, user_email, codigo):
        self.user_email = user_email  # Este campo enlaza con el usuario
        self.codigo = codigo

    def toJson(self):
        return {
            "user_email": self.user_email,
            "codigo": self.codigo,
        }
