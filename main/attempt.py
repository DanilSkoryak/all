
class GuitarFabric:
    def __init__(self, brand, type, color):
        self._brand = brand
        self._type = type
        self._color = color
    
    def get_my_pack(self):
        return self._brand, self._type, self._color


class Orders:
    def __init__(self, name, last_name, adrese, tel_num):
        self.name = name
        self.last_name = last_name
        self.adrese = adrese
        self.tel_num = tel_num
        
    def show_data(self):
        return self.name, self.last_name, self.adrese, self.tel_num
        

class Pack:
    def __init__(self):
        self.date = {}

    def __getitem__(self, item):
        self.date[item]
    
    def __setitem__(self, key, val):
        self.date[key]=val


fabric = GuitarFabric('Fender 20', 'TE', 'White')

order = Orders('Tomas', 'Gujom', 'Frankfurt Str.27', '+1232663342')

pack = Pack()
pay = pack[order.show_data]=fabric.get_my_pack()
print(pay)