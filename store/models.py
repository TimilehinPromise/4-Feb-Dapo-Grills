from django.db import models


# Create your models here.
from django.contrib.auth.models import User 

class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits = 7, decimal_places=2)
    digital = models.BooleanField(default=False,null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("Order On The Way", "Order On The way"),
    ("Order Not Yet Recieved", "Order Not Yet Recieved"),
)

LOCATIONS = (
    ("Abule Egba", 5000),
    ("Acme", 2000),
    ("Adeniyi jones", 8000),
    ("Admiralty rd lekki phase 1", 9000),
    ("Agboyi ketu", "Abule Egba"),
    ("Agege abattior", "Abule Egba"),
    ("Agidingbi", "Abule Egba"),
    ("Ajao estate", "Abule Egba"),
    ("Akilo ogba", "Abule Egba"),
    ("Akoka UNILAG", "Abule Egba"),
    ("Akoka", "Abule Egba"),
    ("Akowonjo", "Abule Egba"),
    ("Alapere", "Abule Egba"),
    ("Alimosho", "Abule Egba"),
    ("Anthony village", "Abule Egba"),
    ("Anthony mende", "Abule Egba"),
    ("Anthony – ajao estate", "Abule Egba"),
    ("Ayobo rd", "Abule Egba"),
    ("Banana island", "Abule Egba"),
    ("Bariga", "Abule Egba"),
    ("CMD rd", "Abule Egba"),
    ("Command – Ipaja", "Abule Egba"),
    ("Dolphin estate", "Abule Egba"),
    ("Dopemu", "Abule Egba"),
    ("E-centre –Yaba ", "Abule Egba"),
    ("Egbeda", "Abule Egba"),
    ("Ejigbo", "Abule Egba"),
    ("Eko Atlantic City", "Abule Egba"),
    ("Eleko", "Abule Egba"),
    ("Eleko beach", "Abule Egba"),
    ("Fadeyi", "Abule Egba"),
    ("Festac Town", " "),
    ("Garage Ojota", " "),
    ("Gbagada General Hosptial ", " "),
    ("Gbagada Ifako", " "),
    ("Gbagada Phase 1 &2", " "),
    ("Gbagada Soluyi ", " "),
    ("Gbagada UPS", " "),
    ("Gowon Estate", " "),
    ("Idimu", " "),
    ("Ifako Agege", " "),
    ("Igando", " "),
    ("Ijesha Tedo", " "),
    ("Iju Train Station ", " "),
    ("Ikeja –Alausa", " "),
    ("Ikeja GRA", " "),
    ("Ikeja Opebi", " "),
    ("Ikeja Oba Akran", " "),
    ("Ikeja Allen Avenue", " "),
    ("Ikeja Maryland ", " "),
    ("Ikosi Ketu", " "),
    ("Ikotun", " "),
    ("Ikoyi Awolowo", " "),
    ("Ikoyi Bourdillon", " "),
    ("Ikoyi Alfred Rewane", " "),
    ("Ikoyi Glover", " "),
    ("Ikoyi Osborne", " "),
    ("Ikoyi Prisons ", " "),
    ("Ilasamaja", " "),
    ("Ilupeju Bye pass", " "),
    ("Ipaja road", " "),
    ("Ire Akari", " "),
    ("Isheri –Idimu", " "),
    ("Isolo", " "),
    ("Jakande – Isheri ", " "),
    ("Jakande – Isolo", " "),
    ("Ketu", " "),
    ("Kosofe", " "),
    ("Ladi Laki – Somolu", " "),
    ("Lagos Island", " "),
    ("Lekki Phase 1", " "),
    ("Ligali Ayorinde ", " "),
    ("Mafoluku", " "),
    ("Magodo Phase 1", " "),
    ("Magodo Phase 2", ""),
    ("Marina", ""),
    ("Marina Express", ""),
    ("Mile 12", ""),
    ("Mushin ", ""),
    ("National Theatre", ""),
    ("New Garage Gbagada", ""),
    ("Obalende", ""),
    ("Obanikoro", ""),
    ("Obanikoro Pedro", ""),
    ("Obawole", ""),
    ("Ogba", ""),
    ("Ogudu", ""),
    ("Ojodu", ""),
    ("Oke Afa", ""),
    ("Oke odo ", ""),
    ("Oko Oba", ""),
    ("Okota", ""),
    ("Olowora", ""),
    ("Omole Phase 1", ""),
    ("Omole Phase 2", ""),
    ("Onigbongbo", ""),
    ("Onike", ""),
    ("Onipanu", ""),
    ("Oniru", ""),
    ("Oregun", ""),
    ("Orile – Coker", ""),
    ("Orile –Iganmu", ""),
    ("Orile Agege", ""),
    ("Oshodi", ""),
    ("Papa AJao", ""),
    ("Shasha", ""),
    ("Shogunle – Ikeja", ""),
    ("Sungas – Shomolu", ""),
    ("Surulere – Aguda", ""),
    ("Surulere – Bode Thomas ", ""),
    ("Surulere – Idi Araba", ""),
    ("Surulere – Ojuelegba", ""),
    ("Surulere – Stadium ", ""),
    ("Surulere – Adelabu", ""),
    ("Surulere – Animashaun", ""),
    ("Surulere – Barracks", ""),
    ("Surulere – Idi oro", ""),
    ("Town Planning", ""),
    ("VI – Ahmadu Bello", ""),
    ("Victoria Island", ""),
    ("Yaba – Abule Ijesha", ""),
    ("Yaba – Alagomeji", ""),
    ("Yaba – Makoko", ""),
    ("Yaba – Market ", ""),
    ("Yaba – Oyingbo", ""),
    ("Yaba – Tejuosho", ""),
    ("Yaba – Fola Agoro", ""),
    ("Yaba – Adekunle ", ""),
    ("Yaba – Bajulaye rd", ""),
    ("Yaba – Ebutte Meta", ""),
    ("Yaba – Empire", ""),
    ("Yaba – Iddo ", ""),
    ("Yaba – Iwaya", ""),
    ("Yaba – Jibowu", ""),
    ("Yaba – Sabo ", ""),
    ("Yaba – Tech", ""),
    ("Yaba – Total", ""),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.IntegerField(null=True)
    order_status = models.CharField(max_length = 100, choices = ORDER_STATUS, default="Order Not Yet Recieved")

    def __str__(self):
        return str(self.transaction_id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.order.transaction_id)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=100,null=True)
    date_added= models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.address



    



