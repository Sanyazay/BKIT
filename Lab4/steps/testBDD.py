from behave import Given,When,Then
from Logistic_company import TruckCreator



@Given("ordering delivery for box with parametres deliverytype: {a} boxtype: {b} weight: {c}")
def given_check(context,a,b,c):
    context.deliverytype = a
    context.boxtype = b
    context.weight = c
    


@When("we create truck delivery")
def delivery_creation(context):
    result = TruckCreator().creation(context.deliverytype,context.boxtype,context.weight)
    context.result=result

@Then("delivery check should be with given parameters")
def compare_results(context):
    assert(context.result == "Ваша посылка отправлена {0}\nТип доставки: {1}\nТип коробки: {2}\nВес посылки {3} кг".format("грузовой машиной",context.deliverytype,context.boxtype,context.weight))
