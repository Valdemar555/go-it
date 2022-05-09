from abc import ABCMeta, abstractmethod
import json
import pickle

class SerializationInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def load_data(self):
        pass


class SaveToBin(SerializationInterface):
    
    def save_data(self):
        some_data = {"name":"Jack", "age":21, "brothers":("Mark","Mike")}
        file_name = 'data.bin'
        with open(file_name, "wb") as fh:
            pickle.dump(some_data, fh)

    def load_data(self):
        file_name = 'data.bin'
        with open(file_name, "rb") as fh:
            unpacked = pickle.load(fh)
      

class SaveToJS(SerializationInterface):
    
    def save_data(self):
        some_data = {"name":"Jack", "age":21, "brothers":("Mark","Mike")}
        file_name = 'data.json'

        with open(file_name, "w") as fh:
            json.dump(some_data, fh)

    def load_data(self):
        file_name = 'data.json'
        with open(file_name, "r") as fh:
            unpacked = json.load(fh)

#a = SaveToBin()
#a.save_data()
#a.load_data()
#b = SaveToJS()
#b.save_data()
#b.load_data()