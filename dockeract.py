# employee.py
class Employee:
    def __init__(self, empname, department, netpay):
        self.empname = empname
        self.department = department
        self.netpay = netpay

    def __repr__(self):
        return f"Employee({self.empname}, {self.department}, {self.netpay})"

# payroll.py
class Payroll:
    def __init__(self):
        self.employee_list = LinkedList()

    def add_employee(self, employee):
        self.employee_list.append(employee)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
