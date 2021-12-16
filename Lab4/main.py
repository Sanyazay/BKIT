
import Logistic_company


if __name__ == "__main__":
    print("Выберите вид транспорта для доставки:\n1)Доставка наземным транспортом\n2)Доставка морским транспортом")
    transporttype=int(input())
    print("Выберите тип доставки:\n1)Экспресс\n2)Обычная")
    deliverytype=int(input())
    if deliverytype == 1:
        deliverytype = "экспресс"
    else:
        deliverytype = "обычная"
    print("Выберите тип коробки:\n1)Безопасная(для хрупких грузов)\n2)Обычная")
    boxtype=int(input())
    if boxtype == 1:
        boxtype = "безопасная(для хрупких грузов)"
    else:
        boxtype = "обычная"
    print("Введите вес посылки в килограммах")
    weight=int(input())
    if transporttype == 1 :
        print(Logistic_company.TruckCreator().creation(deliverytype,boxtype,weight))
    else:
        print(Logistic_company.ShipCreator().creation(deliverytype,boxtype,weight))