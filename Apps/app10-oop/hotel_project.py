import pandas as pd

df = pd.read_csv("hotels.csv", dtype = {"id":str}) # only the id columns will be treated as string
print(df)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Booy a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        """Checking the hotel's availability"""
        availability = df.loc[df["id"] == self.hotel_id]["available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

class ReservationTicket:
    def __init__(self, customer_name, hotel_object): 
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank your for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content

hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    hotel.book()
    name = input("Enter your name bro: ")
    reservation_ticket = ReservationTicket(customer_name = name, hotel_object = hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")