import os
import time
import heapq

# Employee database
employees = [
    {"id": 101, "name": "Bruce Wayne", "salary": 50000, "department": "Finance"},
    {"id": 102, "name": "Clark Kent", "salary": 40000, "department": "IT"},
    {"id": 103, "name": "Diana Prince", "salary": 3000, "department": "Marketing"},
    {"id": 104, "name": "Barry Allen", "salary": 50000, "department": "HR"}
]

# Graph representing the company network (departments as nodes)
company_network = {
    "Finance": {"IT": 2, "HR": 4},
    "IT": {"Finance": 2, "Marketing": 3},
    "Marketing": {"IT": 3, "HR": 6},
    "HR": {"Finance": 4, "Marketing": 6}
}

def clear_screen():
    """Clears the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_next_id():
    """Gets the next available employee ID"""
    return max(emp["id"] for emp in employees) + 1 if employees else 101

def add_employee():
    """Adds a new employee"""
    print("\n--- Add New Employee ---")
    print("DEPARTEMENTS AVAILABLE: HR, IT, Finance, Marketing\n")
    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()
   
    while True:  # Ensure salary is a valid number
        try:
            salary = int(input("Enter salary: "))
            break
        except ValueError:
            print("Invalid salary. Please enter a number.")

    new_id = get_next_id()  # Get next available ID
    employees.append({"id": new_id, "name": name, "salary": salary, "department": department})
   
    print(f"\n✅ Employee added successfully! New ID: {new_id}\n")
    time.sleep(1.5)
    clear_screen()

def search_employee():
    """Search for an employee by ID"""
    while True:
        try:
            search = int(input("\nEnter Employee ID to search (or 0 to return): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if search == 0:
            return  # Go back to menu

        employee = next((emp for emp in employees if emp["id"] == search), None)

        if employee:
            salary = employee['salary']

            # Fixed deductions for all employees
            sss = 500
            pagibig = 500
            philhealth = 400
            tax = salary * 0.05 if salary > 25000 else 0  # 5% tax only if salary > 25000

            total_deductions = sss + pagibig + philhealth + tax
            net_salary = salary - total_deductions

            print(f"\nID: {employee['id']}, \nName: {employee['name']}, \nSalary: {salary}, \nDepartment: {employee['department']}\nDeductions: \nSSS: {sss}, \nPagibig: {pagibig}, \nPhilhealth: {philhealth}, \nTax: {tax}, \nNet Salary: {net_salary}")
        else:
            print("Employee not found.")

        choice = input("Search another employee? (yes/no): ").strip().lower()
        if choice != 'yes':
            return
        
#bubble sort algo
def bubble_sort_by_salary(order="asc"):
    """Sorts employees by salary using Bubble Sort"""
    n = len(employees)
    for i in range(n):
        for j in range(0, n-i-1):
            if (order == "asc" and employees[j]["salary"] > employees[j+1]["salary"]) or \
               (order == "desc" and employees[j]["salary"] < employees[j+1]["salary"]):
                employees[j], employees[j+1] = employees[j+1], employees[j]

def print_all_employees():
    """Prints all employees with sorting options"""
    print("\n--- Employee List ---")
    sort_choice = input("Sort by (1) ID, (2) Salary? ").strip()
    order = input("Ascending (A) or Descending (D)? ").strip().lower()

    if sort_choice == "2":
        bubble_sort_by_salary("asc" if order == "a" else "desc")
    else:
        employees.sort(key=lambda x: x["id"], reverse=(order == "d"))

    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Salary: {emp['salary']}, Department: {emp['department']}")
    print("\n")

# Dijkstra's algorithm
def dijkstra(graph, start):
    """Finds shortest paths from the start department to all other departments"""
    print("\nDEPARTMENTS AVAILABLE: HR, IT, Finance, Marketing\n")
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]  # Priority queue (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > shortest_paths[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

def find_shortest_path():
    """Finds shortest path between departments"""
    print("\n--- Find Shortest Path Between Departments ---")
    start = input("Enter start department: ").strip()
    if start not in company_network:
        print("Invalid department.")
        return
    
    paths = dijkstra(company_network, start)
    print(f"\nShortest paths from {start}:")
    for department, distance in paths.items():
        print(f"To {department}: {distance} units")
    
    print("\n")

# Start of the program
def welcome_screen():
    for line in [
        "+===================================+",
        "|                                   |",
        "|            Welcome to             |",
        "|               the                 |",
        "|     Employee Management System    |",
        "|                                   |",
        "+===================================+"
    ]:
        print(line)

welcome_screen()
time.sleep(2.5)
clear_screen()

# Main menu
while True:
    print("Employee Management System")
    print("===========================")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Print All Employees")
    print("4. Find Shortest Path (Dijkstra's Algorithm)")
    print("0. Exit")

    option = input("Choose an option: ").strip()

    if option == "1":
        add_employee()
    elif option == "2":
        search_employee()
    elif option == "3":
        print_all_employees()
    elif option == "4":
        find_shortest_path()
    elif option == "0":
        print("Exiting program. Goodbye!")
        time.sleep(1.5)
        clear_screen()
        break
    else:
        print("Invalid option. Please try again.")