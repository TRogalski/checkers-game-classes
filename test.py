def return_corresponding2(number, list_to_be_checked):
    x=1
    for element in list_to_be_checked:
        if number in element or number == element:
            return x
        else:
            x+=1
    return 0

print(return_corresponding2([4,6],[[4,6]]))
print([[2,1],[[4,6],[3,1]]].index([4,6]))
