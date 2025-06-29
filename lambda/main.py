from weather import get_weather

def handler(event, context):
    temp = get_weather()
    print(temp)

    return "Hello Avneet, from Lamda"
