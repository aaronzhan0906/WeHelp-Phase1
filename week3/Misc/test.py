import json
import re

with open("./public/taipei-attractions-assignment-2", mode="r") as file:
    parsed_data = json.load(file)

attractions = parsed_data["data"]
mrt_list = []

# 遍历所有景点
for attraction in attractions:
    # 获取当前景点的 MRT 列表
    mrt_key = attraction["MRT"]
    mrt_list.extend(mrt_key.split("、"))

print(mrt_list)