#basicWeatherDataLookUp
cities = {
    'Gujarat': {"temp": 27,"precipitation" : 10,"wind" : 22,"weather" : 'cloudy'},
    'Maharashtra': {"temp": 32,"precipitation" : 20,"wind" : 32,"weather" : 'rainy'},
    'Rajasthan': {"temp": 34,"precipitation" : 30,"wind" : 42,"weather" : 'sunny'},
    
}
def weatherlookup(city_name):
   
    format=lambda a:(f"city : {city_name}\n"
                     f"temparaure :{a['temp']}\n"
                     f"precipitation : {a['precipitation']}\n"
                     f"wind: {a['wind']}\n"
                     f"weather :{a['weather']}")
    if city_name in cities:
        outputt=cities[city_name]
        return format(outputt)
    else:
        return "Error: City not found"
def mainmethod():
    city_name = input("Enter a city name: ")
    report = weatherlookup(city_name)
    print(report)

mainmethod()    


