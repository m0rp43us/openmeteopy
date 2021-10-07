

class TypedList(list):

    def append(self, item):
        if item in self:
            raise TypeError('item already added to the parameters')

        super(TypedList, self).append(item)
    
    def append_all(self,item):
        for element in item:
            super(TypedList, self).append(element)

#class Errors():

