def substring(string,startIndex,endIndex):
    i = startIndex
    newString = ""
    while(startIndex<=endIndex):
        newString = newString + string[startIndex]
        startIndex = startIndex + 1

    return newString

#   Some advices :
#   indexing is like 0,1,2,....len(string)-1
#   returnedString will have characters ----->
#       from startIndex provided
#       and exactly upto returnIndex


