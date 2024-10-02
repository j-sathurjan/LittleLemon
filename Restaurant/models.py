from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest=models.IntegerField()
    bookingDate=models.DateTimeField()
    
    def __str__(self) -> str:
        return str(self.pk) + ") Name: "+ self.name +", No of Guests: "+str(self.no_of_guest) +", BookDate: "+ str(self.bookingDate)
    
class Menu(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(decimal_places=2, max_digits=10)
    inventory=models.SmallIntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'