import field



class unique(object):


    def __init__(self,items, ignore_case = False, **kwargs):
        self.items = items
        self.a=kwargs
        self.ignore_case = ignore_case
        self.uniq=set()
        
        self.index=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.ignore_case == False :
            for i in self.items:
                if(i not in self.uniq):
                    self.uniq.add(i)
                    return i
            raise StopIteration
        else:
            for i in self.items:
                try:
                    print(i)
                    if(i.upper() not in self.uniq):
                        self.uniq.add(i.upper())
                        return i
                except AttributeError:
                    if (i not in self.uniq) :
                        self.uniq.add(i)
                        return i
            raise StopIteration
                        
                
 
if __name__ == "__main__":
    goods = [                
        {'title': 'ковер', 'price': 2000, 'color': 'green'}, 
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': 'Диван для отдыха', 'color': 'black'},     
    ]          
            
    c=True
    g=[1,2,3,4,5,"D","d","a",1.5,"A"]
    a=unique(field.field(goods,"title"),c)
    a