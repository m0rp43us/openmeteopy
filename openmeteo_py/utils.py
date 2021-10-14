

class TypedList(list):

    def append(self, item):
        if item in self:
            raise TypeError('item already added to the parameters')

        super(TypedList, self).append(item)
    
    def append_all(self,item):
        for element in item:
            super(TypedList, self).append(element)

class ApiCallError(Exception):

    def __init__(self, response):
        self.response = response
        #super().__init__(self.res)

    def __str__(self):
        return f'{self.response["reason"]}'

class FilepathNotFilled(Exception):
    def __init__(self):
        response = "Forgot to fill the filepath"
        self.response = response
        #super().__init__(self.res)
    
    def __str__(self):
        return f'{self.response}'

class FileOptionError(Exception):
    def __init__(self):
        response = "file number not in the options"
        self.response = response
        #super().__init__(self.res)
    
    def __str__(self):
        return f'{self.response}'