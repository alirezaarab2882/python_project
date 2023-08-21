class Karmand:


    riase_amunt=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    def full_name(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay=int(self.pay*Karmand.riase_amunt)
emp1=Karmand('ali','arab',300)
emp2=Karmand('MOhammad','molaee',400)



print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

print(emp2.pay)
emp2.apply_raise()
print(emp2.pay)
