class Employee:

    def __init__(self):
        print('Employee created!')

    def __del__(self):
        print('Destructor called')
        
def create_object():
    print('Creating object...')
    obj = Employee()
    print('Program ended...')

create_object()