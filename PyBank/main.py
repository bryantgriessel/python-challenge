# Modules
import os
import re
import csv

# Prompt user for title lookup
#book=input("What book would you like to look for? ")

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variable to check if we found the video
found=0
count=0
values=[]
dates=[]
avals=[]
avg=0
x=1
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through not required but here in case we want to do something else with it in the future
        while found==0:
                #skipping header row and saving into value firstrow
                firstrow=next(csvreader)
                print("CSV Headers are: " +str(firstrow[0])+ " | " +str(firstrow[1]))

                for row in csvreader:
                    #append values array with proffit values. Do the same thing for dates 
                    values.append(int(row[1]))
                    dates.append(row[0])
                    count=count+1         

                if found ==0:
                        #We want to skip first row since it you can't subtract anything from it hence "[1:]"
                        for i in values[1:]:
                            #get change between current and previous and stores in array. 
                            avals.append(int(values[x])-int(values[x-1]))
                            x=x+1
                                        
                        amount=sum(values)
                        avg=sum(avals)/len(avals)
                        maxv=max(avals)
                        maxloc=avals.index(max(avals))
                        minv=min(avals)
                        minloc=avals.index(min(avals))

                        print(f'{"----------------------------"}')
                        print(f'{"Total Months: "}{count}')
                        print(f'{"Total: $"} {amount}')
                        print(f'{"Average Change: $"}{avg:.2f}')
                        #maxloc+1 because avals location is 1 higher since x started at 1
                        print(f'{"Greatest Increase: "}{dates[maxloc+1]}{" $"}{maxv}')
                        print(f'{"Greatest Decrease: "}{dates[minloc+1]}{" $"}{minv}')

                        #create txt and write to it
                        with open('output.txt', 'w') as f:
                            ln='\n'
                            f.write(f'{"Total Months: "}{count}{ln}')
                            f.write(f'{"Total: $"} {amount}{ln}')
                            f.write(f'{"Average Change: $"}{avg:.2f}{ln}')
                            f.write(f'{"Greatest Increase: "}{dates[maxloc+1]}{" $"}{maxv}{ln}')
                            f.write(f'{"Greatest Decrease: "}{dates[minloc+1]}{" $"}{minv}')
                            f.close()
                        exit()
 


