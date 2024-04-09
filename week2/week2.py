# Task 1
print("=== Task 1 ===")
import re

def find_and_print(messages, current_station):
    station_and_distance = {
        "Songshan": 1,
        "Nanging Sanmin": 2,
        "Taipei Arena": 3,
        "Namjing Fuxing": 4,
        "Songjiang Nanjing": 5,
        "Zhongshan": 6,
        "Beiman": 7,
        "Ximen": 8,
        "Xiaonanmen": 9,
        "Chiang Kai-Shek Memorial Hall": 10,
        "Guting": 11,
        "Taipower Building": 12,
        "Gongguan": 13,
        "Wanlong": 14,
        "Jingmei": 15,
        "Dapinglin": 16,
        "Qizhang": 17,
        "Xiaobitan": 18,
        "Xindian City Hall": 18,
        "Xindian": 19
    }

    # dealing with issues related to metro branch lines.
    if current_station == "Xindian City Hall" or current_station == "Xindian":
        station_and_distance["Xiaobitan"] = 16
    elif current_station == "Xiaobitan":
        station_and_distance["Xindian City Hall"] = 16
        station_and_distance["Xindian"] = 17
    else:
        station_and_distance["Xiaobitan"] = 18
        station_and_distance["Xindian City Hall"] = 18
        station_and_distance["Xindian"] = 19

    # create a regex to match the station name from the message
    station_regex = re.compile('|'.join(station_and_distance.keys()), re.IGNORECASE)
    closest_person = ""
    min_distance = float('inf')

    # iterate over the messages and find the closest person
    for person, message in messages.items():
        match = station_regex.search(message)
        if match:
            station = match.group(0)
            distance = abs(station_and_distance[current_station] - station_and_distance[station])
            if distance < min_distance:
                min_distance = distance
                closest_person = person

    if closest_person:
        print(closest_person)


messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian





# Task 2
print("=== Task 2 ===")
def book(consultants, hour, duration, criteria):
    # sort the consultants by the criteria
    if criteria == "price":
        consultants.sort(key=lambda x: x['price'])
    elif criteria == "rate":
        consultants.sort(key=lambda x: x['rate'], reverse=True)
        
    # find and book the available consultant
    available_consultant = None
        
    # check if the consultant has any appointment that overlaps with the given hour and duration
    for consultant in consultants:
        end_hour = hour + duration
        is_available = True
        
        for appointment in consultant.get('appointments', []):
            if  (hour >= appointment['start'] and hour < appointment['end']) or \
                (end_hour > appointment['start'] and end_hour <= appointment['end']) or \
                (hour <= appointment['start'] and end_hour >= appointment['end']):
                is_available = False
                break
        
        # create the appointments list and add the new appointment
        if is_available:
            available_consultant = consultant
            if 'appointments' not in consultant:
                consultant['appointments'] = []
            consultant['appointments'].append({'start': hour, 'end': end_hour})
            break
    
    if available_consultant is not None:
        print(available_consultant['name'])
    else:
        print("No Service")


consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John





# Task 3
print("=== Task 3 ===")
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





# Task 4
print("=== Task 4 ===")
def get_number(index):
    term = -5 * (index // 3)
    number = index * 4 + term
    print(number) 

get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70





# Task 5
print("=== Task 5 ===")
def find(spaces, stat, n):
    for i in range(len(spaces)):
        if stat[i] == 0:
            spaces[i] = 0
    
    min_space_index = -1
    min_difference = float('inf')

    for i in range(len(spaces)):
        difference = spaces[i] - n

        if difference >= 0 and difference < min_difference:
            min_difference = difference
            min_space_index = i

    print(min_space_index)


find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2