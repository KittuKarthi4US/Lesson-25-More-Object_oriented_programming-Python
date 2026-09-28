class IOstring:

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input('Enter a string : ')

    def print_string(self):
        print('The string is : ',self.str1.upper())

obj = IOstring()
obj.get_string()
obj.print_string()
