class travell:
    
    def __init__(self,country,city,month):
        self.country = country
        self.city = city
        self.month = month
    def meth_1(self):
        print("which country would you like trvael "+self.country)
        print("which city " +self.city)
        print("when " +self.month)

    def meth_2(self):
        self.country = "Italy"
        self.city = "Rome"
        self.month = "June"
