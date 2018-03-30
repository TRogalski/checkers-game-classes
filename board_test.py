x=[[[4, 2], [5, 1], [6, 0]],[1,1],[5,1]]

check=[5,1]


for i in x:
    if check in i or check==i:
        print("jest",x.index(i))
        break
