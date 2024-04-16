def book(consultants, hour, duration, criteria):
    # sort the consultants by the criteria
    if criteria == "price":
        consultants.sort(key=lambda x: x["price"])
    elif criteria == "rate":
        consultants.sort(key=lambda x: x["rate"], reverse=True)

    # find and book the available consultant
    available_consultant = None

    # check if the consultant has any appointment that overlaps with the given hour and duration
    for consultant in consultants:
        end_hour = hour + duration
        is_available = True

        for appointment in consultant.get("appointments", []):
            if (
                (hour >= appointment["start"] and hour < appointment["end"])
                or (end_hour > appointment["start"] and end_hour <= appointment["end"])
                or (hour <= appointment["start"] and end_hour >= appointment["end"])
            ):
                is_available = False
                break

        # create the appointments list and add the new appointment
        if is_available:
            available_consultant = consultant
            if "appointments" not in consultant:
                consultant["appointments"] = []
            consultant["appointments"].append({"start": hour, "end": end_hour})
            break

    if available_consultant is not None:
        print(available_consultant["name"])
    else:
        print("No Service")


consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John
