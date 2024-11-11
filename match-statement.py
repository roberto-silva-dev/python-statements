
def activity_for_day(day):
    match day:
        case "Monday":
            return "Start the week strong!"
        case "Friday":
            return "Wrap up the week!"
        case _:
            return "Make the most of your day!"
        

def grade_feedback(score):
    match score:
        case s if s >= 90:
            return "Excellent!"
        case s if s >= 70:
            return "Good job!"
        case s if s >= 50:
            return "Needs some improvement"
        case _:
            return "Keep working on it!"
        

def check_data(data):
    match data:
        # Tries to match a dictionary with "status": "error" and a "code" key.
        # If it finds it, stores the value of "code" in the variable `code`
        # and then checks if `code >= 500`.
        case {"status": "error", "code": code} if code >= 500:
            return "Critical error!"
        
        # Matches a dictionary with "status": "error" without checking "code"
        case {"status": "error"}:
            return "General error"
        
        # Matches a list with three elements where all are the same (e.g., [1, 1, 1])
        case [x, y, z] if x == y == z:
            return "All elements are the same"
        
        # If no match is found, returns a default message
        case _:
            return "Unknown format"        
        


print(activity_for_day("Monday"))
print(grade_feedback(50))
print(check_data({"status": "error", "code": 500}))