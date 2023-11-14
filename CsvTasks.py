import pandas

def firstQuestion():
    max = 0
    for row in data:
        if row[1] == "A100600" and row[4] > max:
            max = row[4]
    return max

def secondQuestion():
    count = 0
    for row in data:
        if row[1] == "A105900":
            count += 1
    return count

def thirdQuestion():
    totalValue = 0.0
    count = 0
    for row in data:
        if row[1] == "A123100":
            totalValue += row[4]
            count += 1
    return round(totalValue/count)

def fourthQuestion():
    topThree = [0.0] * 3
    sortedData = sorted(data, key=lambda entry: entry[4], reverse=True)
    
    for i in range(0,3):
        topThree[i] = sortedData[i][4]
        
    return sum(topThree)

def fifthQuestion():
    secondValues = [0.0]
    for i in range (0,len(data),2):
        if data[i][1] == "A119500":
            secondValues.append(data[i][4])
    
    secondValues.remove(0)
    return sum(secondValues)
    

# Global variable, can be accessed from functions, no need to pass.
# anzsic06,Area,year,geo_count,ec_count
data = pandas.read_csv("data.csv").values.tolist()

print("1.jautajums, atbilde: ", firstQuestion())
print("2.jautajums, atbilde: ", secondQuestion())
print("3.jautajums, atbilde: ", thirdQuestion())
print("4.jautajums, atbilde: ", fourthQuestion())
print("5.jautajums, atbilde: ", fifthQuestion())