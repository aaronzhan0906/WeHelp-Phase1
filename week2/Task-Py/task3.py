def func(*data):
    names = {}

    # make key-value pair
    for name in data:
        full_name_split = list(name)
        result = []

        # get middleName
        if len(full_name_split) % 2 == 1:

            # retain the middle character
            result = [full_name_split[len(full_name_split) // 2]]
        elif len(full_name_split) == 2:
            result = [full_name_split[1]]
        elif len(full_name_split) % 2 == 0:
            result = [full_name_split[2]]

        names[name] = "".join(result)

    # get the unique array
    unique_array = list(names.values())

    # get the unique index
    unique = []
    for element in unique_array:
        if unique_array.count(element) == 1:
            unique.append(element)

    if len(unique) == 0:
        print("沒有")
        return

    # get the key of the unique index
    for key, value in names.items():
        if value == unique[0]:
            print(key)

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安