
import requests
# For creating visual plots
import matplotlib.pyplot as plt
# Extension for creating map-based graphics
from mpl_toolkits.basemap import Basemap

"""Function that returns the current location of the ISS"""
def iss_location():
    response = requests.get("http://api.open-notify.org/iss-now.json")

    # Check if the HTTP status code indicates success
    # If successful, save the JSON response as a dictionary in the variable
    if response.status_code == 200:
        data = response.json()
        iss_position = data['iss_position']
        return iss_position
    else:
        return None



"""creates a map"""
#def iss_map():
