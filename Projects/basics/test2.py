d = {
    1:'India',
    2:'Acadwdadaw'
}

l = [value for key, value in d.items() if 5< len(value) ]
print(l)