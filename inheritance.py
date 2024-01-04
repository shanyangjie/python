class Country:
    def __init__(self,name):
        self.country=name

class City(Country):
    def __init__(self,country_name,city_name):
        super().__init__(country_name)
        self.city=city_name



classes=[]
classes.append(City("Taiwan","Taoyuan"))
classes.append(City("Korea","Seoul"))

for cls in classes:
    print(cls.city + ' of ' + cls.country )