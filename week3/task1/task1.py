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
                District = district_address[index-3:index+1].strip()  # strip() to remove white space
                break

        # get longtitude and latitude
        Longitude = spot["longitude"]
        Latitude = spot["latitude"]

        # get ImageURL
        split_urls = spot["filelist"].split("https://")
        ImageURL = "https://" + split_urls[1]

        writer.writerow([Stitle, District, Longitude, Latitude, ImageURL])
    

# open file to write mrt.csv
with open("mrt.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    # create a dictionary to store attractions near each station
    station_attractions = {}

    get_spot_list = parsed_main_data["data"]["results"]
    for spot in get_spot_list:
        # get serial_no in 1st JSON file
        get_serial = spot["SERIAL_NO"]
        for serial_no_data in mrt_serialno_district["data"]:
            if serial_no_data["SERIAL_NO"] == get_serial:
                station_name = serial_no_data["MRT"]
                station_attractions.setdefault(station_name, []).append(spot["stitle"])

    # write station and attractions to mrt.csv
    for station_name, attractions in station_attractions.items():
        writer.writerow([station_name] + attractions)