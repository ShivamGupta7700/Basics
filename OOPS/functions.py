def cars(name: str, info: dict[str,int|str]) ->None:
    print(name, info)
    if not isinstance(name, str):
        raise TypeError('not good')
    print(type(name))

cars("shivam",{"engine": [3789012]})