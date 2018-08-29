from mongoengine import *
import mlab

class Customer(Document):
    name = StringField()
    age = StringField()
    address = StringField()
    ref = StringField()
    meta = {'collection': 'customers', "strict": False}

mlab.connect()

customer_list = Customer.objects
# for ref in customer_list:
#     print (len(ref))

print(len(customer_list(ref__icontains="ads")))
print(len(customer_list(ref__icontains="wom")))
print(len(customer_list(ref__icontains="events")))


