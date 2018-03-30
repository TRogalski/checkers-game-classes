

def return_corresponding(number,list_to):
    x=1
    for i in list_to:
        if number in i or number==i:
            return x
        x+=1
    return False        


        
print(return_corresponding([3,4],[[[3,4],[4,6]],[1,4]]))
