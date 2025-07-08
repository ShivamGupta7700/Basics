import csv

try:
    with open('sample.csv', 'r+', newline='') as file:
        # fileObj = csv.writer(file, delimiter=',')
        # l = ['shivam','17','Good','Male']
        # fileObj.writerow(l)
        fileread = csv.reader(file)
        for row in fileread:
            print(row)

except Exception as e:
    print(f'Error >> {e}')