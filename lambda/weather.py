import urllib.request

def get_weather():
    url = "https://wttr.in/Seattle?format=3"
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode().strip()
    except Exception as e:
        return f"Error: {str(e)}"

