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
input = 20
output = []


#function for finding 2 number combonations for int
def split(start,tiles,shift):
  out = []
  for i in range(start,round(tiles/2)):
   
    if(shift!=[]):
      out.append(shift+[i,tiles-i])
    else:
      out.append([i,tiles-i])
  return out


#function for returning popped list
def returnpopped(myList):
  myList.pop()
  return myList

  


output = (split(1,input,[]))
splitPrevAppend = []
print(output)


#loop through every # of possible steps
for j in range(2):
  #loop through every # of possible first nums in step
  for i in range(len(output)):
    #split last element of output 
    #make sure to set start limit to 2nd last element of output
    splitPrev = split(output[i][len(output[i])-2]+1,output[i][len(output[i])-1],returnpopped(output[i]))

    print(splitPrev)
    splitPrevAppend = splitPrevAppend + splitPrev

  print("----------------------")
  output=splitPrevAppend



# timer  
time_elapsed = datetime.now() - start_time
print('Time elapsed is {}'.format(time_elapsed))

