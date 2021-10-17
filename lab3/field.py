
def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            for j in i: # i - один словарь из списка j - ключ от словаря 
                    if j==args[0]:
                        yield i[j]
    else:
        for i in items:
            a={}
            for j in i:
                for h in args:
                    if(j==h):
                        a[h]=i[h]
            yield a

if __name__ == "__main__":
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    for i in field(goods,"title"):
        print(i)
    for i in field(goods,"title","price"):
        print(i)

                      
