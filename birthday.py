class birthdayboy:
    def _ _init_ _(self,name,age):
         self.name=name
         self.age=age
    def birthday(self):
        self.age+=1
        
birthday_person=birthdayboy(name="JOHN",age=25 )
birhday_person.birthday()
print(f"{birthday_person.name}'s new age after the birthday: {birthday_person.age}")
