"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isSalaryWage, salaryValue, hoursWorked, hourlyWage,
                  isCommissionFixed, commissionValue, contractsWorked, contractCommission):
        self.name = name
        self.isSalaryWage = isSalaryWage
        self.salaryValue = salaryValue
        self.hoursWorked = hoursWorked
        self.hourlyWage = hourlyWage
        self.isCommissionFixed = isCommissionFixed
        self.commissionValue = commissionValue
        self.contractsWorked = contractsWorked
        self.contractCommission = contractCommission

    def get_pay(self):
        wage = 0
        if self.isSalaryWage:
            wage += self.salaryValue
        else:
            wage += self.hoursWorked * self.hourlyWage
        
        if self.isCommissionFixed:
            wage += self.commissionValue
        else:
            wage += self.contractsWorked * self.contractCommission
        return wage


    def __str__(self):
        string =  self.name + " works on a "
        if self.isSalaryWage:
            string += "monthly salary of " + str(self.salaryValue)
        else:
            string += "contract of " + str(self.hoursWorked) + " hours at " + str(self.hourlyWage) + "/hour"
        if self.isCommissionFixed:
            string += " and receives a bonus commission of " + str(self.commissionValue)
        else:
            if self.contractsWorked > 0:
                string +=  " and receives a commission for " + str(self.contractsWorked) + " contract(s) at " + str(self.contractCommission) + "/contract"
        string += ".  Their total pay is " + str(self.get_pay()) + "."
        return string


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', True, 4000, 0, 0, False, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', False, 0, 100, 25, False, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', True, 3000, 0, 0, False, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', False, 0, 150, 25, False, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 2000, 0, 0, True, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', False, 0, 120, 30, True, 600, 0, 0)
