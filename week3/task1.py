import json
import re
import csv

# read JSON file
with open("./public/taipei-attractions-assignment-1", mode="r") as file:
    parsed_main_data = json.load(file)
with open("./public/taipei-attractions-assignment-2", mode="r") as file:
    mrt_serialno_district = json.load(file)

# open file to write
with open("spot.csv", mode="w", newline='') as file:
    writer = csv.writer(file)

    get_spot_list = parsed_main_data["data"]["results"]
    for spot in get_spot_list:
        # get stitle
        Stitle = spot["stitle"]

        # get district
        get_serial = spot["SERIAL_NO"]
        for serial_no_data in mrt_serialno_district["data"]:
            if serial_no_data["SERIAL_NO"] == get_serial:
                district_address = serial_no_data["address"]
                index = district_address.find("區")
                District = district_address[index-3:index+1]
                break

        # get longtitude and latitude
        Longitude = spot["longitude"]
        Latitude = spot["latitude"]

        # get ImageURL
        url_regex = r"(https?:\/\/[^\s]+\.(?:jpg|JPG))"
        filelist = spot["filelist"]
        regex_filelist = filelist.replace(r"\\", "")
        list_regex_filelist = re.sub(r"(\.(?:jpg|JPG))", r"\1 ", regex_filelist)
        ImageURL = re.findall(url_regex, list_regex_filelist)[0]

        writer.writerow([Stitle, District, Longitude, Latitude, ImageURL])
    
# create a list to store all station names
station_names = []

# create regex for station name
for entry in mrt_serialno_district["data"]:
    station_names.extend(entry["MRT"].split("、"))

station_regex = '|'.join(map(re.escape, station_names))

# open file to write mrt.csv
with open("mrt.csv", mode="w") as file:
    writer = csv.writer(file)

    # create a dictionary to store attractions near each station
    station_attractions = {}

    for station in parsed_main_data["data"]["results"]:
        get_info = station["info"]
        get_station_name = re.findall(station_regex, get_info)
        if get_station_name:
            station_attractions[get_station_name[0]] = station_attractions.get(get_station_name[0], []) + [station["stitle"]]
        else:
            continue

    # write station and attractions to mrt.csv
    for station_name, attractions in station_attractions.items():
        writer.writerow([station_name, ", ".join(attractions)])