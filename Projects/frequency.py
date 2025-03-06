from collections import Counter
lst = list(map(int, input("Enter numbers: ")))
print(lst)
freq = Counter(lst)
print("Frequencies:", freq)
