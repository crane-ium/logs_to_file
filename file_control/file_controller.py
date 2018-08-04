"""
Open and closing our file through a class
"""

class FileController(object):
    """
    Create a file

    :my_file: file that opens and closes
    """

    def __init__(self, name):
        self.name = name

    def append(self, string):
        self.file_data.append(string)
    
    def clear(self):
        self.file_data = ''

    def rewrite(self, index, string):
        """Rewrites the index line"""
        self.file_data[index] = string

    @property
    def len(self): 
        return len(self.file_data)

    def __str__(self):
        return '\n'.join(self.file_data)
    
    @classmethod
    def make_empty(cls, name):
        """Returns an obj with an empty file"""
        obj = cls(name)
        obj.my_file = open(name, 'w')
        obj.my_file.write('')
        obj.my_file.close()
        return obj 

    def __enter__(self):
        self.my_file = open(self.name, 'r+')
        self.file_data = self.my_file.read().split('\n')

    def __exit__(self, exception_type, exception_value, traceback):
        self.my_file.write(str(self))
        self.my_file.close()
    