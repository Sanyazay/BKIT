from behave import Given,When,Then
from asyncbot3 import summary,average_price,first_course,first_course_price,main_course,main_course_price,dessert,dessert_price



@Given("ordering1 food with answers in bot first course - {a} main course - {b} dessert - {c}")
def given_answers(context,a,b,c):
    context.ans1=int(a)
    context.ans2=int(b)
    context.ans3=int(c)

@When("we form average price of position of check")
def make_summary(context):
    res = average_price(first_course,first_course_price,main_course,main_course_price,dessert,dessert_price,context.ans1,context.ans2,context.ans3)
    context.result=res

@Then("average price should {d}")
def compare_results(context,d):
    corres= "Средняя стоимость одной позиции = " + str(d)
    assert(context.result == corres )