ages =[13,15,17,19,21,23]
print (ages)
print(ages[0])
print(ages[1])
print(ages[3])
print(ages[4])
print(ages[5])




for i in range(5):
  print(i)
  print(f"value for ages is {i}",ages[i])
  

#list
list = [5,10,"Deborah",55.5,False]
for i in range (5):
   print(f"value for[{i}]",list[i])
print("--------------")
# modification
list[2] = "Akash"
list[3] = "66.6"
for i in range (5):
     print(f"value for[{i}]",list[i])
print("-------------------")



fruitlist = ["Watermelon","Orange","Apple","Grape","Tangerine"]
print(fruitlist)

lenghtOfFruitList = len(fruitlist)
print(fruitlist)
 
for i in range (lenghtOfFruitList):
 print(f"value for fruitlist[{i}]",fruitlist[i])

for fruit in fruitlist :
   print (fruit)
print("----------")



