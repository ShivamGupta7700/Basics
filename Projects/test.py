subject_list = ['science', 'maths', 'cs', 'hindi', 'S.St']
marks = [int(input(f'Enter you marks {subject_list[i]} >>> ')) for i in range(5)]
total = sum(marks)
print(total)