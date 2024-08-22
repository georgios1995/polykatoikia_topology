import random

totalArea = 80
areaPercentage = 0.3

maximumY = 10
minimumY = 2

maximumX = 10
minimumX = 2

area = totalArea * areaPercentage

isArea = False
areaRoomList = []
Xcomb = maximumX - minimumX + 1
Ycomb = maximumY - minimumY + 1

TotalComb = Xcomb * Ycomb
print("TotalCombinations:", TotalComb)

loops = 0

while not isArea:
    Xsize = random.randint(minimumX, maximumX)
    Ysize = random.randint(minimumY, maximumY)  # Fixed typo here
    areaRoom = Xsize * Ysize
    loops += 1  # Fixed incorrect assignment operator
    print("Loop count:", loops)
    
    areaRoomUnique=True
    
    for x,y in areaRoomList:
        if x==Xsize and y==Ysize:
         areaRoomUnique=False
        
    if areaRoom == area and areaRoomUnique:
         areaRoomList.append((Xsize, Ysize))
    
    if loops >= TotalComb:
        isArea = True  # Fixed the incorrect comparison operator

print("Matching room sizes:", areaRoomList)