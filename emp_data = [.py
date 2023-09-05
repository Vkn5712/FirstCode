emp_data = [
    {"Employee ID": "161E87", "Name": "Vishnu", "Age": 19, "Salary": 50000},
    {"Employee ID": "161F99", "Name": "Priti", "Age": 28, "Salary": 60000},
    {"Employee ID": "161F92", "Name": "Jayant", "Age": 24, "Salary": 80000},
    {"Employee ID": "171E34", "Name": "Tojus", "Age": 25, "Salary": 50500},
    {"Employee ID": "171G65", "Name": "Riya", "Age": 43, "Salary": 67000},
]

def sorting_empdata(choice):
    if choice == 1:  
        sorteddata = sorted(emp_data, key=lambda x: x["Age"])
    elif choice == 2:
        sorteddata = sorted(emp_data, key=lambda x: x["Name"])
    elif choice == 3: 
        sorteddata = sorted(emp_data, key=lambda x: x["Salary"])
    else:
        print("Invalid choice. Please select a valid sorting parameter (1, 2, or 3).")
        return
    print("\nSorted Employee Data:")
    print("Employee ID\tName\tAge\tSalary")
    for employee in sorteddata:
        print(
            f"{employee['Employee ID']}\t{employee['Name']}\t{employee['Age']}\t{employee['Salary']}"
        )
print("Sort Employee Data:")
print("1. Age")
print("2. Name")
print("3. Salary")
choice = int(input("Enter your option how you want to sort 1/2/3: "))
sorting_empdata(choice)