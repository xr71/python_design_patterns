import pytest

# lets say a house where hvac and electricians come to visit

# new operations to be performed on an existing class
# operations on a composite object

class House(object):

    def accept(self, visitor):
        # trigger the visitor operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on", hvac_specialist)

    def work_on_elec(self, elec_specialist):
        print(self, "worked on", elec_specialist)

    def __str__(self):
        return self.__class__.__name__


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)

class ElecSpecialist(Visitor):
    def visit(self, house):
        house.work_on_elec(self)

myhvac = HvacSpecialist()
myelec = ElecSpecialist()

myhouse = House()
myhouse.accept(myhvac)

