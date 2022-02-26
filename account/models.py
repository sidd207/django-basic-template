from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Code(models.Model):
    TYPE = (
        ('C', 'C'),
        ('S', 'S'),
    )
    STATES = (
        ("Andhra Pradesh", "Andhra Pradesh" ),
        ("Arunachal Pradesh", "Arunachal Pradesh"),
        ("Assam", "Assam"),
        ("Bihar","Bihar" ),
        ("Chhattisgarh", "Chhattisgarh" ),
        ("Goa", "Goa"),
        ("Gujarat","Gujarat" ),
        ("Haryana", "Haryana"),
        ("Himachal Pradesh","Himachal Pradesh" ),
        ("Jammu and Kashmir", "Jammu and Kashmir"),
        ("Jharkhand", "Jharkhand"),
        ("Karnataka", "Karnataka"),
        ("Kerala", "Kerala"),
        ("Madhya Pradesh","Madhya Pradesh" ),
        ("Maharashtra", "Maharashtra"),
        ("Manipur", "Manipur"),
        ("Meghalaya", "Meghalaya"),
        ("Mizoram", "Mizoram"),
        ("Nagaland", "Nagaland"),
        ("Odisha","Odisha" ),
        ("Punjab", "Punjab"),
        ("Rajasthan", "Rajasthan"),
        ("Sikkim", "Sikkim"),
        ("Tamil Nadu", "Tamil Nadu"),
        ("Telangana", "Telangana"),
        ("Tripura", "Tripura"),
        ("Uttarakhand","Uttarakhand" ),
        ("Uttar Pradesh", "Uttar Pradesh"),
        ("West Bengal","West Bengal" ),
        ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
        ("Chandigarh", "Chandigarh"),
        ("Dadra and Nagar Haveli", "Dadra and Nagar Haveli"),
        ("Daman and Diu","Daman and Diu" ),
        ("Delhi", "Delhi"),
        ("Lakshadweep", "Lakshadweep"),
        ("Puducherry", "Puducherry"),
    )
    
    DTYPE =(
        ("G", "G"),
        ("P", "P"),
        ("U", "U")
    )
    state = models.CharField(max_length=50, choices=STATES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of = models.CharField(max_length=1, choices=TYPE)
    reference_number = models.CharField(max_length=20)
    d_type = models.CharField(max_length=1, choices=DTYPE)
    code = models.CharField(max_length=255)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.state