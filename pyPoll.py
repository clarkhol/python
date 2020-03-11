import csv
import os

csvpath = os.path.join("Desktop","Python_Challenge","election_data.csv")

with open (csvpath) as csvfile:
    csvReader = csv.reader(csvfile)
    
    #Set totalVotes to 0
    totalVotes = 0  
    
    #Create a dictionary for listNames, this is where the names of the candidates will go.
    listNames = {}
    
    #Count total number of votes
    for row in csvReader:
        totalVotes = totalVotes + 1
        if row[2] not in listNames:
            listNames[row[2]] = 0
        #Count the number of votes each candidate received
        for key in listNames:
            if row[2] == key:
                listNames[key] +=1
    #Exclude the heading 'candidate' from the count
    listNames.pop("Candidate")

      
print ("Election Results")
print ("-----------------")
#Print total votes
print ("Total Votes:", totalVotes - 1)
print ("-----------------")
#Get the percentage of votes each candidate received and print the number of votes each candidate received.
for key in listNames:   
    print (key,":", "{:.2%}".format(round(listNames[key]/(totalVotes), 10)), "(", listNames[key],")")
print ("-----------------")
#Get the candidate with the most votes
Win = max(listNames, key=listNames.get)
print("Winner:", Win)
print ("-----------------" )



