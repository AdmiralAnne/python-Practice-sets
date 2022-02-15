import requests
API_KEY = "ce85aa5b8da810424a5d87693443222b"
# install a module that sends requests to the API

# where are we sending the request to ?---THE END POINT
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#some queries -like city
city = input("enter a city name: ")

#build a URL that includes URL + queries
request_url=f"{BASE_URL}?appid={API_KEY}&q={city}" 
#we have generated out api call url ~ yeehaww

# time to send a request to the url~ GET req in this case
response=requests.get(request_url) # get-data-from-request_url-JSON file

# check before we process
# "status code" 200-- successful 

if response.status_code == 200:
    data = response.json() # get the json data as a Python Dictionary-- with key: value pair style data
    # collect some basic inforamtion- Discribtion 
    weather = data['weather'][0]['description'] #access the json stored as a dictionary
    # Temperature
    temperature = round(data['main']['temp']-273.15, 2)
    print("City: ", city)
    print("weather: ",weather)
    print("Temp: ",temperature, " celcius")

else:
    print("an error occureed. Sorry Boss ~")

# now~ we have all the data we need. Time to Print the information hehee
