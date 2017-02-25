import re

from urllib import request

#http://www.weather-forecast.com/locations/Nakuru/forecasts/latest
while True:
    
    try:
    
        city = input("Enter city: ")
        
        url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
        
        data = request.urlopen(url).read().decode('utf-8')
        
        #print(data)
        
        m = re.search('<span class="phrase">', data)
        
        start = m.end()
        
        data = data[start:]
        
        m = re.search("</span>", data)
        
        end = m.start()
        
        print(city.capitalize() + " Weather Forecast")
        
        print ("-" * (len(city)+17 ))
        
        print (data[0:end])
        
    except:
        
        print("Invalid City.")
        
        break
    
