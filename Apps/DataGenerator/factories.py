import factory
from factory.django import DjangoModelFactory
from Apps.User.models import CustomerUser, StaffUser
from Apps.Hotel.models import HotelModel
from Apps.Room.models import RoomType, Room, RoomStatus
from Apps.Booking.models import RoomBooking
from Apps.Checkout.models import Billing
from random import randint


class CustomerUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomerUser

    Name = factory.Faker('name')
    Username = factory.Faker('user_name')
    Password = factory.Faker('password')
    ID_No = factory.LazyAttribute(lambda x: "%d%d%d%d%d%d%d%d%d" % (randint(1,9), randint(0, 9), randint(0, 9), randint(0, 9), 
    randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9)))
    Address = factory.Faker('address')
    PhoneNumber = factory.Faker('phone_number')
    Email = factory.Faker('email')
    

class HotelModelFactory(DjangoModelFactory):
    class Meta: 
        model = HotelModel

    HotelName = factory.Faker('company')
    StarType = factory.LazyAttribute(lambda x: randint(1, 5))
    HouseNumber = factory.LazyAttribute(lambda x: randint(0, 1000))
    Street = factory.Faker('last_name')
    District = factory.Faker('last_name')
    City = factory.Faker('city')
    AveragePrice = factory.LazyAttribute(lambda x: int( randint(100000, 5000000) / 10000 ) * 10000)  


class StaffUserFactory(DjangoModelFactory):
    class Meta:
        model = StaffUser

    Name = factory.Faker('name')
    Username = factory.Faker('user_name')
    Password = factory.Faker('password')
    HotelCode = factory.SubFactory(HotelModelFactory)
    

class RoomTypeFactory(DjangoModelFactory):
    class Meta:
        model = RoomType
    
    RoomTypeName = factory.Faker('name')
    HotelCode = factory.SubFactory(HotelModelFactory)
    UnitPrice = factory.LazyAttribute(lambda x: int( randint(100000, 5000000) / 10000 ) * 10000)
    VacancyAmount = factory.LazyAttribute(lambda x: randint(1, 15))

class RoomFactory(DjangoModelFactory):
    class Meta:
        model = Room

    RoomType = factory.SubFactory(RoomTypeFactory)
    RoomNumber = factory.LazyAttribute(lambda x: randint(1, 15))

class RoomStatusFactory(DjangoModelFactory):
    class Meta:
        model = RoomStatus

    RoomCode = factory.SubFactory(RoomFactory)
    Date = factory.Faker('date')
    Status = factory.LazyAttribute(lambda x: randint(0, 2))

class RoomBookingFactory(DjangoModelFactory):
    class Meta:
        model = RoomBooking

    RoomTypeCode = factory.SubFactory(RoomTypeFactory)
    CustomerCode = factory.SubFactory(CustomerUserFactory)
    StartDate = factory.Faker('date')
    EndDate = factory.Faker('date')
    BookingDate = factory.Faker('date')
    UnitPrice = factory.LazyAttribute(lambda x: int( randint(100000, 5000000) / 10000 ) * 10000) 
    Status = factory.LazyAttribute(lambda x: randint(1, 2))

class BillingFactory(DjangoModelFactory):
    class Meta:
        model = Billing

    PaymentDate = factory.Faker('date')
    TotalAmount = factory.LazyAttribute(lambda x: int( randint(100000, 5000000) / 10000 ) * 10000)
    RoomBookingCode = factory.SubFactory(RoomBookingFactory)
