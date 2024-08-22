import json
class LibUser:
    def login(self, email, password):
        file = open('data/user.json')
        j = json.load(file)
        for x in j:
            if x['email']== email and x['password']==password:
                return True
        return False