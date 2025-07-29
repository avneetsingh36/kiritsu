from calc import return_five

def handler(event, context):
    num = return_five()
    print(num)

    return f'Hello Avneet, from Lamda - here is your num -> {num}'
