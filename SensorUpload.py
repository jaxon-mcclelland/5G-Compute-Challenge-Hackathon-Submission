import time
import requests
import socket
from sense_hat import SenseHat

sense = SenseHat()

sense.set_imu_config(True, False, False)

humidity = sense.get_humidity()
# Offset determined by series of testing based on thermometer
temp = sense.get_temperature() - 11.54
pressure = sense.get_pressure()

raw_magnetometer_data = sense.get_compass_raw()
magnetometer_x = "{x}".format(**raw_magnetometer_data)
magnetometer_y = "{y}".format(**raw_magnetometer_data)
magnetometer_z = "{z}".format(**raw_magnetometer_data)



hostname = socket.gethostname()

endpoint = 'http://XX.XX.XX.XX:8000/'
csrf_url = endpoint + 'csrf'
client = requests.session()
client.get(csrf_url)

if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']

else:
    csrftoken = client.cookies['csrf']

requests.post(
    endpoint,
    data = {
        'csrfmiddlewaretoken': csrftoken,
        'deviceHostname': hostname,
        'humidity': humidity,
        'pressure': pressure,
        'temperature': temp,
        'magx' : magnetometer_x,
        'magy' : magnetometer_y,
        'magz' : magnetometer_z,
    }
)
