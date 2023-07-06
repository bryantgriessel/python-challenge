# Modules
import os
import re
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
found=0
count=0
avg=0
x=1
Charles=0
Diana=0
Raymon=0
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through not required but here in case we want to do something else with it
        while found==0:
            #skipping header row and saving into value firstrow Not requried but i figured might as well store it as var than skip it
            firstrow=next(csvreader)
            print("CSV Headers are: " +str(firstrow[0])+ " | " +str(firstrow[1])+ " | "+str(firstrow[2]) )
            for row in csvreader:
                #check name in row 2 and increment the name to keep count of votes
                if str(row[2])=="Charles Casper Stockham":
                     Charles=Charles+1
                elif str(row[2])=="Diana DeGette":
                     Diana=Diana+1
                elif str(row[2])=="Raymon Anthony Doane":
                     Raymon=Raymon+1
            #count represents total number of votes
                count=count+1 
                           
            found =1 
            if found ==1:      

                #get percent of votes per candidate
                Charlesp=(Charles/count)*100
                Dianap=(Diana/count)*100
                Raymonp=(Raymon/count)*100
                #determine max vote and store in winner
                winner = max([Charles,Diana,Raymon])
               
                print(f'{"----------------------------"}')
                print(f'{"Total Votes: "}{count}')
                print(f'{"----------------------------"}')
                print(f"Charles Casper Stockham: %{Charlesp:.3f} ({Charles})")
                print(f"Diana DeGette: %{Dianap:.3f} ({Diana})")
                print(f"Raymon Anthony Doane: %{Raymonp:.3f} ({Raymon})")
                print(f'{"----------------------------"}')
                #check  which voter count winner is == to and determine the winners name
                if winner == Charles:
                     print(f'{"Winner: Charles Casper Stockham"}')
                elif winner == Diana:
                     print(f'{"Winner: Diana DeGette"}')
                elif winner == Raymon:
                     print(f'{"Winner: Raymon Anthony Doane"}')
                #write to txt file
                with open('output.txt', 'w') as f:
                    f.write(f"Total Votes: {count} \n")
                    f.write(f'{"----------------------------"}\n')
                    f.write(f"Charles Casper Stockham: %{Charlesp:.3f} ({Charles}) \n")
                    f.write(f"Diana DeGette: %{Dianap:.3f} ({Diana}) \n")
                    f.write(f"Raymon Anthony Doane: %{Raymonp:.3f} ({Raymon}) \n")
                    f.write(f"---------------------------- \n")
                    #check  which voter count winner is == to and determine the winners name
                    if winner == Charles:
                        f.write(f"Winner: Charles Casper Stockham \n")
                    elif winner == Diana:
                        f.write(f"Winner: Diana DeGette \n")
                    elif winner == Raymon:
                        f.write(f"Winner: Raymon Anthony Doane")
                        

    
