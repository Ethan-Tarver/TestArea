
page = 0
list =0
while True:

    page +=1

    print("page:%s" %page)
    for n in range(20):
        list +=1
        print(list)
    if list == 327:
        break