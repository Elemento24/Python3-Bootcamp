class GrumpyDict(dict):
    def __repr__(self):
        print('None of your Business!')
        return super().__repr__()

    def __missing__(self, key):
        print(f'You want {key}? Well you will not found it here!')

    def __setitem__(self, key, value):
        print('You want to change the Dictionary!')
        print('Okay, fine ....')
        super().__setitem__(key, value)

    def __contains__(self, item):
        print('No, it is not here!')
        return False


data = GrumpyDict({'First': 'Tom', 'Animal': 'Cat'})
print(data)
data['City']
data['City'] = 'Tokyo'
print(data)
'City' in data
