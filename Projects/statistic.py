s = input("Enter a sentence: ")
vowels = sum(1 for c in s if c.lower() in "aeiou")
digits = sum(1 for c in s if c.isdigit())
print("Vowels:", vowels, "Digits:", digits)
