class Meta(type):
    
    number = -1
    def __new__(*args,**kwargs):
        
        return type.__new__(*args,**kwargs)

    def __call__(cls,*args,**kwargs):
        instance = object.__new__(cls)
        return instance
        
    def __init__(self,data,*args,**kwargs):
        self.data = data
        Meta.number += 1
        self.class_number = Meta.number
        

    
Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data
        

class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


print(Cls1.class_number)
print(Cls2.class_number)
assert (Cls1.class_number, Cls2.class_number) == (0, 1)

a, b = Cls1(''), Cls2('')
print(a.class_number)
print(b.class_number)
assert (a.class_number, b.class_number) == (0, 1)

