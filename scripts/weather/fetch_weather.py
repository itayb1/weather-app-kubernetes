import os
import requests
from time import sleep, time


FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL"))
CITY = os.getenv("CITY")
HTML_LOCATION = os.getenv("HTML_LOCATION")

API_KEY = os.getenv("API_KEY")

INITIAL_DELAY = 45

API_URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"


class ApiException(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message


def fetch_weather():
    try:
        r = requests.get(API_URL, verify=False)
        if r.status_code == 200:
            return r.text
        else:
            raise ApiException(r.status_code, "Couldn't fetch weather")
    except ApiException as e:
        return f"{e.status_code} - {e.message}"
    except Exception as e:
        return f"Unknown error - {str(e)}"


def main():
    while 1:
        result = fetch_weather()
        with open(f"{HTML_LOCATION}/index.html", "w") as f:
            f.write(result)
            f.write(f" - {time()}")
        sleep(FETCH_INTERVAL)


if __name__ == '__main__':
    main()
