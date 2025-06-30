import csv

try:
    with open('sample.csv', 'w', newline='') as file:
        fileObj = csv.writer(file, delimiter=',')
        l = ['shivam','17','Good','Male']
        fileObj.writerow(l)

except Exception as e:
    print(f'Error >> {e}')