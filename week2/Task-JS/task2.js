function book(consultants, hour, duration, criteria) {
    // sort the consultants by the criteria
    if (criteria === "price") {
            consultants.sort((a, b) => a.price - b.price);
        } else if (criteria === "rate") {
            consultants.sort((a, b) => b.rate - a.rate);
        } 
        
    let availableConsultant = null;
    
    // check if the consultant has any appointment that overlaps with the given hour and duration
    for (const consultant of consultants) {
        const endHour = hour + duration;
        let isAvailable = true;
        
        for (const appointment of consultant.appointments || []) {
            if ((hour >= appointment.start && hour < appointment.end) ||
                (endHour > appointment.start && endHour <= appointment.end)||
                (hour <= appointment.start && endHour >= appointment.end)) {
                isAvailable = false;
                break;
            }
        }
        
        // create the appointments array and add the new appointment
        if (isAvailable) {
            availableConsultant = consultant;
            if (!consultant.appointments) {
                consultant.appointments = [];
            }
            consultant.appointments.push({ start: hour, end: endHour });
            break;
        }
    }
    
    if (availableConsultant !== null) {
        console.log(availableConsultant.name);
    } else {
        console.log("No Service");
    }
}
    


const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];
    
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

  