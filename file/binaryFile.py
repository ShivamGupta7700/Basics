import pickle

try:
    with open('sample.dat', 'wb+') as file :
        data = {
                    'name':'Shivam',
                    "age":17,
                }
        
        pickle.dump(data, file)

except Exception as e:
    print(f'Error >> {e}')