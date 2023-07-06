# Example 1
employee_list = [ {"id":1,"name":"Sam","salary":5000, "department": "IT"}, {"id":2,"name":"Nick","salary":6000, "department": "IT"}, {"id":3,"name":"Ramesh","salary":7000, "department": "IT"}, {"id":4,"name":"Suresh","salary":8000, "department": "IT"}]

# returns the employee with the given id
def get_emplyee_by_id(id):
    for employee in employee_list:
        if employee["id"] == id:
            return employee
    return None

print(get_emplyee_by_id(1))

# Example 2
employee_dict = {
    1: {"id":1,"name":"Sam","salary":5000, "department": "IT"},
    2: {"id":2,"name":"Nick","salary":6000, "department": "IT"},
}

print(type(employee_dict))

def get_employee_from_dict(id):
    return employee_dict[id]

print(get_employee_from_dict(1))