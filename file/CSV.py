import csv
import pickle
# try:
#     with open('sample.csv', 'r+', newline='') as file:
#         # fileObj = csv.writer(file, delimiter=',')
#         # l = ['shivam','17','Good','Male']
#         # fileObj.writerow(l)
#         fileread = csv.reader(file)
#         for row in fileread:
#             print(row)

# except Exception as e:
#     print(f'Error >> {e}')

with open('sample.dat', 'ab') as file:
    pickle.dump(['emp1','IT',2000],file)



with open('sample.dat', 'rb+') as file:
    l = pickle.load(file)
    print(l)
    for a in l:
        if a[1] == 'IT':
            a[2] = 3000
    pickle.dump(l, file)
