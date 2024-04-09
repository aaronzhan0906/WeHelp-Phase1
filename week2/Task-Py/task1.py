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