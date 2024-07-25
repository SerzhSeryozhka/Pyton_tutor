# _________Task_1____________
company = {
   "HR": {"employees": ["Alice", "Bob"]},
   "Engineering": {"employees": ["Charlie", "Dave"]},
   "Marketing": {"employees": ["Eve", "Frank"]}
}
def is_employee_in_department(company, office, worker):

    if office in company[office] and worker in office[worker]:
            return True
    else:
          return False
# Примеры использования
print(is_employee_in_department(company, "HR", "Alice"))  # Output: True
print(is_employee_in_department(company, "Engineering", "Alice"))  # Output: False
