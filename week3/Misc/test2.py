import json

with open("./public/taipei-attractions-assignment-2", mode="r") as file:
    parsed_data = json.load(file)

attractions = parsed_data["data"]
attractions_dict = {}

for attraction in attractions:      
    mrt_key = attraction["MRT"]
    full_address = attraction["address"]
    index = full_address.find("區") 
    mrt_district = full_address[index-3:index+1]  # get district information, "xx區"
    mrt_key = mrt_key + "站"
    attractions_dict[mrt_key] = mrt_district

    serial_no = attraction["SERIAL_NO"]

print(attractions_dict, serial_no)