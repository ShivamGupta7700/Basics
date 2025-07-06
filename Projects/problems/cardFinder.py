def locate_card(cards , query:int):
    pass

test = {
    'inputs':{
        'cards': [16, 14, 11, 5 , 4, 3, 2 , 1],
        'query':5
    },
    'output':3
}

print(locate_card(**test['inputs'])==test['output'])
