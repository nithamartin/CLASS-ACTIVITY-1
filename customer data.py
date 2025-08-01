class Customer:
  def __init__(self, name, gender, income):
    self.name = name
    self.gender = gender
    self.income = income
  def display(self):
    print(f"Name: {self.name}, Gender: {self.gender}, Income: {self.income}")

#Create an object
customer1 = Customer("Alice", "Female", 50000)
customer2 = Customer("John", "Male", 60000)
customer1.display()
customer2.display()