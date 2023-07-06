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

    # Loop through looking for the video
        while found==0:
                firstrow=next(csvreader)
                print("CSV Headers are: " +str(firstrow[0])+ " | " +str(firstrow[1]))
                for row in csvreader:
                    #dates = re.split(r'-', row[0])
                    #print(Dates)
                    #print(row[0]+" "+ row[1])
                    values.append(int(row[1]))
                    dates.append(row[0])
                    count=count+1         
                #if book.lower() == 'exit':
                      #  print("exiting")
                      #  exit()
                if found ==0:
                        for i in values[1:]:
   
                            avals.append(int(values[x])-int(values[x-1]))
                            x=x+1                
                        amount=sum(values)
                        avg=sum(avals)/len(avals)
                        maxv=max(avals)
                        maxloc=avals.index(max(avals))
                        minv=min(avals)
                        minloc=avals.index(min(avals))

                        print(f'{"Total Months: "}{count}')
                        print(f'{"Total: $"} {amount}')
                        print(f'{"Average Change: $"}{avg:.2f}')
                        print(f'{"Greatest Increase: "}{dates[maxloc+1]}{" $"}{maxv}')
                        print(f'{"Greatest Decrease: "}{dates[minloc+1]}{" $"}{minv}')
                        with open('output.txt', 'w') as f:
                            ln='\n'
                            f.write("CSV Header = " +str(firstrow[0])+ " | " +str(firstrow[1])+"\n")
                            f.write(f'{"Total Months: "}{count}{ln}')
                            f.write(f'{"Total: $"} {amount}{ln}')
                            f.write(f'{"Average Change: $"}{avg:.2f}{ln}')
                            f.write(f'{"Greatest Increase: "}{dates[maxloc+1]}{" $"}{maxv}{ln}')
                            f.write(f'{"Greatest Decrease: "}{dates[minloc+1]}{" $"}{minv}')
                            f.close()
                        exit()
                      # print(book)

                #book=input("What book would you like to look for? ")


            # Set variable to confirm we have found the video

    # If the book is never found, alert the user
