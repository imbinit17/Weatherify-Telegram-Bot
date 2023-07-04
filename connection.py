import http.client
import dataManipulation
import dataManipulation2
import os

def getData(locationString):
    conn = http.client.HTTPSConnection("visual-crossing-weather.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': os.environ.get("RAPID_API_KEY"), 
        'X-RapidAPI-Host': "visual-crossing-weather.p.rapidapi.com"
    }

    locationURL = getLocation(locationString)
    conn.request("GET", "/forecast?aggregateHours=24&location="+locationURL+"&contentType=csv&unitGroup=us&shortColumnNames=0", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data_Decoded = data.decode("utf-8")

    return data_Decoded

def getLocation(locationString):
    i=0
    newString = ""
    while(i<len(locationString)):
        if(locationString[i]==" "):
            newString = newString + "%2C"
        else:
            newString = newString + locationString[i]

        i+=1

    return newString

def dataProcessing(data):
    errorMsg = "No rows were returned. Please verify the location and dates requested"

    response = ''

    if(data==errorMsg):
        response = '''Location not found ! \n\nPlease verify the location and try again.'''
        response = [response,1,False]
        
    else:
        array = dataManipulation.startManipulating(data)
        array = dataManipulation2.conversions(array)  

        response1 = "Location Searched For : "+array[1][0]+"\n"
        response1 += "Database Locaton : "+array[1][4]+"\n"
        response1 += "Latitude : "+array[1][2]+"\n"
        response1 += "Longitude : "+array[1][3]

        response2 = "Weather Forecast : \n\n"
        rowIndex=1
        while(rowIndex<len(array)):
            response2 += "Date : "+array[rowIndex][1]+"\n"
            response2 += "Minimum Temperature : "+array[rowIndex][7]+chr(176)+"\n"
            response2 += "Maximum Temperature : "+array[rowIndex][8]+chr(176)+"\n"
            response2 += "Minimum Temperature : "+array[rowIndex][9]+chr(176)+"\n"
            response2 += "Wind Speed : "+array[rowIndex][10]+" km/h \n"
            response2 += "Chance Of Precipitation : "+array[rowIndex][13]+" %\n"
            response2 += "Weather Condition : "+array[rowIndex][21]+"\n" + "\n"

            rowIndex+=1
        response = [response1,response2,True]

    return response
                                    

            
