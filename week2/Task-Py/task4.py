def get_number(index):
    term = -5 * (index // 3)
    number = index * 4 + term
    print(number) 

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70