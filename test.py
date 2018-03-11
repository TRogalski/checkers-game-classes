



position=[7,0]

possible_moves=[[-1,1],[1,-1],[-1,-1],[1,1]]

z=[]
for item in possible_moves:
    for multiplier in range(1,8):
        z.append([multiplier*coordinate for coordinate in item])




#print(possible_moves)
final=[]
for item in z:
    final.append([x+y for x,y in zip(position,item)])

print([i for i in final if i[0]>=0 and i[0]<=7 and i[1]>=0 and i[1]<=7])


        
