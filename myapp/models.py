from django.db import models
from django.contrib.auth.models import User
from django.utils.dateformat import DateFormat
from django.utils import timezone


# Create your models here.

# PRODUCT ENTRY

class Product(models.Model):
    name = models.CharField(max_length=100)
    shop = models.CharField(max_length=50)
    description = models.TextField()
    keywords = models.CharField(max_length=50, blank=True) 
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, upload_to="products/", blank=True, default='image.jpg')
    video = models.ImageField(null=True, upload_to="products/", blank=True, default='video.mp4')
    digital = models.BooleanField(default=False, null=True, blank=False)
    popular = models.BooleanField(default=False, null=True, blank=False)
    
    BRAND = (
        ('luku-store', 'Luku Store'),
        ('akiba-studios', 'Akiba Studios'),
        ('default', 'Default'),
    )
    brand = models.CharField(max_length=15, choices=BRAND, null=True, default='luku-store')

    # available colors block
    AVAILABLE_COLORS = (
        ('red', 'Red'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('yellow', 'Yellow'),
        ('white', 'White'),
        ('black', 'Black'),
        ('orange', 'Orange'),
        ('grey', 'Grey'),
    )
    available_colors = models.CharField(max_length=15, choices=AVAILABLE_COLORS)
    # end of available colors block
    
    # sizes block
    SIZES = (
        ('small', 'small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ('xl', 'XL'),
        ('xxl', 'XXL'),
        ('fit', 'Fit'),
    )
    sizes = models.CharField(max_length=10, choices=SIZES)
    # end of sizes block

    def __str__(self):
        return f"{self.name}"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# END OF PRODUCT ENTRY

# BLOG ENTRY

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    summary = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255, blank=True) 
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to="blog/", default='blog.jpg')
    video = models.ImageField(null=True, blank=True, upload_to="blog/", default='blog.mp4')
    youtube = models.TextField(blank=True, null=True)

    BRAND = (
        ('luku-store', 'Luku Store'),
        ('akiba-studios', 'Akiba Studios'),
        ('default', 'Default'),
    )
    brand = models.CharField(max_length=15, choices=BRAND, null=True, default='luku-store')


    def __str__(self): 
        return f"{self.title} || {self.pub_date.strftime('%A, %B %d, %Y')}"
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def videoURL(self):
        try:
            url = self.video.url
        except:
            url = ''
        return url

# END OF BLOG ENTRY


# ABOUT US

class AboutUs(models.Model): 
    summary = models.CharField(max_length=700)
    name = models.CharField(max_length=100, default=" ")
    role = models.CharField(max_length=50, default=" ")
    instagram = models.CharField(max_length=50, default=" ")
    tiktok = models.CharField(max_length=50, default=" ")
    facebook = models.CharField(max_length=50, default=" ")
    twitter = models.CharField(max_length=50, default=" ")
    bio = models.TextField(default=" ")
    image = models.ImageField(null=True, blank=True, upload_to="about-us/", default='aboutus.jpg')
    video = models.ImageField(null=True, blank=True, upload_to="about-us/", default='aboutus.mp4')

    def __str__(self):
        return f"{self.name} || {self.role}"
    
# END OF ABOUT US

# NEWSLETTER

class Newsletter(models.Model):
    email = models.EmailField(default=" ")

    def __str__(self):
        return self.email

# END OF NEWSLETTER

# HELP

class Help(models.Model):
    privacy_policy = models.TextField()
    terms_of_service = models.TextField()
    faqs = models.TextField()
    orders_n_delivery = models.TextField()
    return_n_refunds_policy = models.TextField()
    payment_methods = models.TextField()

# END OF HELP

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.id) ('%A, %B %d, %Y')
    
    def __str__(self):
        return f'Order #{self.pk} || {self.customer} {self.date_ordered}'
    
    def __str__(self):
        date_format = DateFormat(self.date_ordered.astimezone(timezone.get_current_timezone()))
        formatted_date = date_format.format('h:iA, l jS F Y')
        return f'Order #{self.pk} || {self.customer} || Date: {formatted_date}'

    
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
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    def __str__(self):
        return f'{self.product}'
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.CharField(max_length=200, null=True)
    
    LABEL = (
        ('Home', 'Home'),
        ('Office', 'Office'),
        ('Default', 'Default'),
    )
    label = models.CharField(max_length=15, choices=LABEL, null=True, default='')
    
    
    def __str__(self):
        return self.address
    
    def __str__(self):
        return f"{self.customer.name}'s {self.label} Address"