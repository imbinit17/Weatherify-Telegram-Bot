import supplementaryFunctions 

array = [["Adress","Date Time","Latitude","Longitude","Resolved Address","Name","Wind Direction","Minimum Temperature","maximum Temperature","Temperature","Wind Speed","Cloud Cover","Heat Index","Chance of Precipitation (%)","Precipitation","Sea Level Pressure","Snow Depth","Snow","Relative Humidity","Wind Gust","Wind Chill","Conditions"]]

    

def startManipulating(data):
    i=0
    actualData = ""
    while(i<len(data)):
        if(data[i]=='"'):
            actualData = supplementaryFunctions.substring(data,i,len(data)-1)
            i = len(data)
        i += 1

    array2 = actualData.split("\n")
    rowsInData = len(array2)
    array = buildArray(rowsInData)

    rowIndex = 1
    while(rowIndex<rowsInData):
        array[rowIndex] = gettingData(array2[rowIndex-1])
        rowIndex += 1

    return array    

def buildArray(rows):
    # Important step
    newArray = [[None for a in range(22)] for b in range(rows)]

    # its alternative newArray = [None * 22]*(rows+1)    just duplicates entire column

    array = ["Adress","Date Time","Latitude","Longitude","Resolved Address","Name","Wind Direction","Minimum Temperature","maximum Temperature","Temperature","Wind Speed","Cloud Cover","Heat Index","Chance of Precipitation (%)","Precipitation","Sea Level Pressure","Snow Depth","Snow","Relative Humidity","Wind Gust","Wind Chill","Conditions"]      

    columnIndex = 0
    while(columnIndex<22):
        newArray[0][columnIndex] = array[columnIndex]
        columnIndex+=1
    
    return newArray

def gettingData(string):
    tempArray = [""]*22

    #getting first element
    tempArray[0] = addContent(string)
    string = nextString(string)
    string = nextString(string) #done on purpose

    #getting second element
    tempArray[1] = addContent(string)
    string = nextString(string)

    string = string.split(",",3)

    #getting 3rd and 4th element
    tempArray[2] = string[1]
    tempArray[3] = string[2]
    string = string[3]

    #getting 5th element
    tempArray[4] = addContent(string)
    string = nextString(string)
    string = nextString(string) #done on purpose

    #getting 6th element
    tempArray[5] = addContent(string)
    string = nextString(string)

    string = string.split(",")


    # getting 7th to 21st element
    tempArray[6] = string[1]
    tempArray[7] = string[2]
    tempArray[8] = string[3]
    tempArray[9] = string[4]
    tempArray[10] = string[5]
    tempArray[11] = string[6]
    tempArray[12] = string[7]
    tempArray[13] = string[8]
    tempArray[14] = string[9]
    tempArray[15] = string[10]
    tempArray[16] = string[11]
    tempArray[17] = string[12]
    tempArray[18] = string[13]
    tempArray[19] = string[14]
    tempArray[20] = string[15]

    string = string[16]
    
    #getting final/22nd element
    tempArray[21] = addContent(string)

    return tempArray


def addContent(string):
    #   string received starting from "

    word = ""

    index = 1
    while(index<len(string)):
        if(string[index]!='"'):
            word += string[index]
            index+=1

        elif(string[index]=='"'):
            index = len(string)

    return word

def nextString(string):
    index = 1
    newString = ""
    while(index<len(string)-1):
        if(string[index]!='"'):
            index += 1

        else:
            newString = supplementaryFunctions.substring(string,index,len(string)-1)
            index = len(string)
            
    return newString
    
         


                       
