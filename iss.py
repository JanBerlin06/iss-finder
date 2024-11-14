# for API communication
from http.client import responses

import requests
# for creating graphics
import matplotlib.pyplot as plt
# extension for creeating graphic maps
from mpl_toolkits.basemap import Basemap

"""function returns the iss location"""
def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    # if HTTP Status OK
    # save JSON as a Dictonary in variable
    if response.status_code == 200:
        data = response.json()
        iss_position = data['iss_position']
        return iss_position
    else:
        return None

"""creates a map"""
def iss_map():
