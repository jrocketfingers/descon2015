import wifi
import threading
import requests
import json
import castclient.settings
from uuid import getnode

def report():
    stations = wifi.Cell.all('wlan0')

    tags = [{"name": station.ssid,
             "signal": station.signal} for station in stations
             if station.ssid.startswith("tag-")]

    print(tags)

    try:
        requests.post("http://151.216.40.36:8000/report/",
                      data={
                         "tags": json.dumps(tags),
                      })

    except:
        print("Failed to contact the server.")

    threading.Timer(1, report).start()

if __name__ == "__main__":
    print(castclient.settings.CLIENT_NAME)
    report()

