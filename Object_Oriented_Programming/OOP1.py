class Customers:
    """
    name = ""
    membership_type = ""

cust1 = Customers()
cust1.name = "Irene"
cust1.membership_type = "Gold"

print(cust1.name)
print(cust1.membership_type)

    """

    def __init__(self, name, status, membership_type):
        self.name = name
        self.status = status
        self.membership_type = membership_type

    def degree(self, course, level, gender):
        self.status = course
        self.level = level
        self.gender = gender

    def update_membership(self, new_membership):
        self.membership_type = new_membership


customer1 = [Customers('Irene', 'regular', 'premium gold'), Customers('Nelson', 'part-time', 'premium bronze')]
# print(customer1[0].name, customer1[0].membership_type)
customer1[0].update_membership('Bronze')
# print(customer1[0].membership_type)

customer2 = Customers("Computer Science", "senior", "female")
print(customer2.status)
