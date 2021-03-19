"""

Authors: Me
Start: 3.14.2021
Last Push: 3.14.2021
Description: Solution to the Staircase problem

"""

# import
from datetime import datetime

# variables
start_time = datetime.now()
input = 12
output = []


#function for finding 2 number combonations for int
def split(start,tiles,shift):
  output = []
  for i in range(start,round(tiles/2)):
    if(shift>0):
      output.append([shift,i,tiles-i])
    else:
      output.append([i,tiles-i])
  return output


  


output = (split(1,input,-1))
print(output)


#loop through every # of possible first nums in step
for i in range(len(output)):
  splitPrev = split(i+2,output[i][1]-i,i+1)
  print(splitPrev)


# print(output)
# print('Length of Output is {}'.format(len(output)))



# timer  
time_elapsed = datetime.now() - start_time
print('Time elapsed is {}'.format(time_elapsed))
