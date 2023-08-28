class Employee:
  raise_ammount: float = 1.04
  num_of_emps: int = 0

  def __init__(self, first: str, last: str, pay: int):
    self.first = first
    self.last = last
    self.pay = pay

    Employee.num_of_emps += 1

  @property  
  def email(self):
    return "%s.%s@domain.com" % (self.first, self.last)
  
  @property
  def fullname(self):
    return "%s %s" % (self.first, self.last)
  
  @fullname.setter
  def fullname(self, input: str):
    first, last = input.split(" ")
    self.first = first
    self.last = last

  @fullname.deleter
  def fullname(self):
    self.first = None
    self.last = None

    
  def appy_raise(self):
    self.pay = int(self.pay * self.raise_ammount)

  def __repr__(self):
    return "%s: %s, %s, %d" % (self.__class__.__name__, self.first, self.last, self.pay)
    # return "{}: '{}', '{}', {}".format(self.__class__.__name__, self.first, self.last, self.pay)

  def __str__(self):
    return "%s - %s" % (self.fullname, self.email)
  
  def __add__(self, other):
    if isinstance(other, Employee):
      return self.pay + other.pay
    return NotImplemented
  
  def __len__(self):
    return len(self.fullname)


class Developer(Employee):
  raise_ammount = 1.1

  def __init__(self, first: str, last: str, pay: int, prog_lang: str):
    super().__init__(first, last, pay)
    # Employee.__init__(self, first, last, pay)

    self.prog_lang = prog_lang

  def __str__(self):
      return "%s, %s" % (super().__str__(), self.prog_lang)


class Manager(Employee):

  def __init__(self, first: str, last: str, pay: int, employees = None):
    super().__init__(first, last, pay)
    # Employee.__init__(self, first, last, pay)

    if employees is None:
      self.employees = [Employee]
    else:
      self.employees = employees

  def add_emp(self, emp: Employee):
    if emp not in self.employees:
      self.employees.append(emp)
  
  def remove_emp(self, emp: Employee):
    if emp in self.employees:
      self.employees.remove(emp)

  def print_emps(self):
    for emp in self.employees:
      print(emp.fullname)


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer("Duc", "Le", 50000, "Java")

emp_2 = Employee("Test", "User", 60000)
mgr_1 = Manager("Sue", "Smith", 90000, [dev_1, emp_2])

# print(help(Developer))
# print(dev_1.__dict__)
# print(emp_2.__dict__)


print(repr(dev_1))
print(str(dev_1))
print(dev_2)

dev_2.fullname = 'Dea Loux'
print(dev_2)

del dev_2.fullname
print(dev_2)


# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(emp_2)
# mgr_1.print_emps();


# print(isinstance(dev_2, Developer))
# print(isinstance(dev_2, Employee))
# print(isinstance(dev_2, Manager))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Employee, Developer))
# print(issubclass(Manager, Developer))