
from __future__ import annotations
from abc import ABC, abstractmethod

'''Создатель транспорта'''
class Creator(ABC):
   
    

    @abstractmethod
    def factory_method(self,delivertype,boxtype,weight):
        
        pass

    def creation(self,delivertype,boxtype,weight):
        product = self.factory_method(delivertype,boxtype,weight)
        product=product.deliver()
        return product #в данном случае возвращает строку с информацией о доставке


class TruckCreator(Creator):
    

    def factory_method(self,delivertype,boxtype,weight) -> Transport:
        return Truck(delivertype,boxtype,weight)


class ShipCreator(Creator):
    def factory_method(self,delivertype,boxtype,weight) -> Transport:
        return Ship(delivertype,boxtype,weight)


'''Создатель транспорта'''
'''Транспор'''
class Transport(ABC):
    
    
    @abstractmethod
    def deliver(self,delivertype,boxtype,weight):
        pass
    
    def __init__(self,deliverytype,boxtype,weight):
        self.deliverytype=deliverytype
        self.boxtype=boxtype
        self.weight=weight

class Truck(Transport):

    def deliver(self):
        result = "Ваша посылка отправлена {0}\nТип доставки: {1}\nТип коробки: {2}\nВес посылки {3} кг".format("грузовой машиной",self.deliverytype,self.boxtype,self.weight)
        return result

class Ship(Transport):
    def deliver(self):
        result = "Ваша посылка отправлена {0}\nТип доставки: {1}\nТип коробки: {2}\nВес посылки {3} кг".format("морским судном",self.deliverytype,self.boxtype,self.weight)
        return result


'''Транспорт'''



    
    
    