import json
import field
import gen_random
import unique
import print_result
import cm_timer

@print_result.print_result
def f1(arg):
    return list(unique.unique(field.field(arg,"job-name"),True))


@print_result.print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"),arg))


@print_result.print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python",arg))


@print_result.print_result
def f4(arg):
    return dict(zip(arg,["зарплата " + str(x)+" рублей" for x in gen_random.gen_random(len(arg),100000,200000)])) 
    
if __name__ == "__main__":
    
    with open("data_light.json",encoding="utf-8") as f:
        data = json.load(f)
        with cm_timer.cm_timer1():
            f4(f3(f2(f1(data))))

