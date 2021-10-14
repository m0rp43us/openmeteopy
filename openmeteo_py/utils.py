

class TypedList(list):
    """
    Typelist class

    helps to check if a parameter is already in the payload list then appends the new parameter

    """

    def append(self, item):
        if item in self:
            raise TypeError('item already added to the parameters')

        super(TypedList, self).append(item)
    
    def append_all(self,item):
        for element in item:
            super(TypedList, self).append(element)

class ApiCallError(Exception):
    """
    Response Api exception

    raises an error if the api responds with one

    """

    def __init__(self, response):
        self.response = response
        #super().__init__(self.res)

    def __str__(self):
        return f'{self.response["reason"]}'

class FilepathNotFilled(Exception):

    """
    Filepath exception

    raises an error if the filepath is not filled but the file option is

    """
    def __init__(self):
        response = "Forgot to fill the filepath"
        self.response = response
        #super().__init__(self.res)
    
    def __str__(self):
        return f'{self.response}'

class FileOptionError(Exception):
    """
    FileOption exception

    raises an error if the file number option is wrong
    """
    def __init__(self):
        response = "file number not in the options"
        self.response = response
        #super().__init__(self.res)
    
    def __str__(self):
        return f'{self.response}'