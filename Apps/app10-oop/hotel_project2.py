import pandas as pd

df = pd.read_csv("hotels.csv", dtype = {"id":str}) # only the id columns will be treated as string
df2 = df.to_string(index = False)

class Hotel:
    # class variables
    watermark = "The Real Estate Company"
    def __init__(self, hotel_id):
        # instance variables
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        """Checking the hotel's availability"""
        availability = df.loc[df["id"] == self.hotel_id]["available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        
    @classmethod    
    def get_hotel_count(cls, data):
        return len(data)

class ReservationTicket:
    def __init__(self, customer_name, hotel_object): 
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank your for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}"""
        return content
    
    # property
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount * 1.2
    

hotel1 = Hotel(hotel_id = "188")
hotel2 = Hotel(hotel_id = "134")

print(hotel1.watermark)
print(hotel1.name)
print(hotel2.name)

print(Hotel.get_hotel_count(data = df))

ticket = ReservationTicket(customer_name = "luca rossi ", hotel_object = hotel1)
print(ticket.the_customer_name)

converted = ReservationTicket.convert(10)
print(converted)