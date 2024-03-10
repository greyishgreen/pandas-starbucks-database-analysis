import numpy as np
import pandas as pd 
sb = pd.read_json("https://raw.githubusercontent.com/mmcloughlin/starbucks/master/locations.json")
my_location= [28.979530, 41.015137]  #longitude , latitude
sbx= sb['longitude']
sby= sb['latitude']
storeids=sb['store_id']
liste=[]

for i in range(25133):#length of indeces
  lists=[]
  lists.append(sbx[i])
  lists.append(sby[i])
  lists.append(storeids[i])
  liste.append(lists)


distances=[]
for i in liste:
  xdistance= i[0]-my_location[0]
  ydistance= i[1]-my_location[1]
  distance=(xdistance**2)+(ydistance**2)
  distance=distance**0.5
  distances.append(distance)


sorted_with_index = sorted(enumerate(distances), key=lambda x: x[1])
sorted_values = [value for index, value in sorted_with_index]
sorted_indexes = [index for index, value in sorted_with_index]

print("Original List:", distances)
print("Sorted Values:", sorted_values)
print("Sorted Indexes:", sorted_indexes)


closest_stores=[]
for i in sorted_indexes:
  closest_stores.append(sb.iloc[[i]])
closest_stores[:5]