import json
import re

# read JSON file
with open("./public/taipei-attractions-assignment-1", mode="r") as file:
    parsed_main_data = json.load(file)
with open("./public/taipei-attractions-assignment-2", mode="r") as file:
    mrt_serialno_district = json.load(file)

# get spot list
get_spot_list = parsed_main_data["data"]["results"]

# open file to write
with open("spot.csv", mode="w") as file:

    for spot in get_spot_list:
        # get stitle
        stitle = spot["stitle"]

        # get district
        get_serial = spot["SERIAL_NO"]
        for serial_no_data in mrt_serialno_district["data"]:
            if serial_no_data["SERIAL_NO"] == get_serial:
                district = serial_no_data["address"]
                index = district.find("區")
                district = district[index-3:index+1]
                break

        # get longtitude and latitude
        longitude = spot["longitude"]
        latitude = spot["latitude"]

        # get ImageURL
        url_regex = r"(https?:\/\/[^\s]+\.(?:jpg|JPG))"
        filelist = spot["filelist"]
        regex_filelist = filelist.replace(r"\\", "",)
        list_regex_filelist = re.sub(r"(\.(?:jpg|JPG))", r"\1 ", regex_filelist)
        ImageURL = re.findall(url_regex, list_regex_filelist)[0]

        file.write(f"{stitle},{district},{longitude},{latitude},{ImageURL}\n")
    

   

