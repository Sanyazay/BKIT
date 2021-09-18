import sys
import math

def get_coef(a):
    print("Коэфициент {} введен некоректно или отсутствует, введите его заново".format(a))
    try:
        a = float(input())
        return a;
    except ValueError:
        a = get_coef(a)
        return a;

def check_coef():
    s = sys.argv
    coef=["A","B","C"]
    for i in range(1,4):
        try:
           coef[i - 1] =  float(s[i])
        except (ValueError,IndexError):
            coef[i - 1] = get_coef(coef[i - 1])
    return coef
def solve(a,b,c):
    
    if(a == 0 and b == 0 and c == 0):
        print(" x - любое число")
        return 0
    elif(a == 0 and b == 0 and c != 0):
        print("x-пустое множество")
        return 0
    elif(a == 0 and b != 0 and c == 0):
        print("x=0")
        return 0
    elif(a != 0 and b == 0 and c == 0):
        print("x=0")
        return 0
    elif(a == 0 and b != 0 and c != 0):

        
       
        if(-c/b>0):
            print("x - {}".format(math.sqrt(-1.0*c/b)))
            print("x - {}".format(-math.sqrt(-1.0*c/b)))
            return 0
        else:
            print("x - пустое множество")
            return 0
    elif(a != 0 and b == 0 and c != 0):

        if(-c / a < 0):
            print("x - пустое множество")
            return 0
        else:
            if(-math.sqrt(-c/a)>0):
                print(" x - {}".format(math.sqrt(-math.sqrt(-c/a))))
                print("x - {}".format(-math.sqrt(-math.sqrt(-c/a))))
                return 0
            
    else:
        d=b * b - 4 * a * c
        if(d == 0):
            if((-b / (2 * a))==0):
                print("x - 0")
                return 0
            elif((-b / (2 * a))<0):
                print("x - пустое множество")
                return 0
            else:
                print("x - {}".format(math.sqrt(-b / (2 * a))))
                print("x - {}".format(-math.sqrt(-b / (2 * a))))
                return 0
            
        elif(d < 0):
            print("x -  пустое множество")
            return 0
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            if(x1 > 0):
                print("x - {}".format(math.sqrt(x1)))
                print("x - {}".format(-math.sqrt(x1)))
            if(x2 > 0):
                print("x - {}".format(math.sqrt(x2)))
                print("x - {}".format(-math.sqrt(x2)))
            if(x1==0):
                print("x - 0")
            if(x2==0):
                print("x - 0")
            
            
    return 0




def main():
    coef = check_coef()
    print(coef)
    solve(coef[0],coef[1],coef[2])
    
    
if __name__ == '__main__':
    main()



