

def conversions(array):
    rows = len(array)

    rowIndex = 1
    while(rowIndex<rows):
        array[rowIndex][7] = fahrenheitToCelsius(array[rowIndex][7])
        array[rowIndex][8] = fahrenheitToCelsius(array[rowIndex][8])
        array[rowIndex][9] = fahrenheitToCelsius(array[rowIndex][9])

        array[rowIndex][1] = dateConversion(array[rowIndex][1])
        rowIndex += 1

    return array

def fahrenheitToCelsius(tempFahrenheit):
    tempCelsius = (float(tempFahrenheit)-32)*(5/9)
    tempCelsius = round(tempCelsius,2)
    return str(tempCelsius)

def dateConversion(dateString):
    #from mm/dd/yyyy to dd/mm/yyyy

    date = dateString.split("/")

    newDate = date[1]+"/"+date[0]+"/"+date[2]

    return newDate
        
    
