from django.db import models
from register.models import User
import uuid

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=150)

    def __str__(self):
        return self.department
    
    
class Complaint_Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category
    

class Complaint(models.Model):
    status_choices = (
        ('open', 'Open'),
        ('in progress','In Progress'),
        ('resolved','Resolved'),
        ('closed','Closed')
    )
    complaint_id = models.CharField(max_length=20, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    category = models.ForeignKey(Complaint_Category, on_delete=models.PROTECT)
    description = models.TextField()
    attachment = models.FileField(upload_to='complaint_attachments/')
    status = models.CharField(choices=status_choices, default='open', max_length=20)

    # overwriting the django save() function
    def save(self, *args, **kwargs):
        if not self.complaint_id:
            self.complaint_id = f"CMP-{uuid.uuid4().hex[:10].upper()}"
            # uuid.uuid() is the python built-in unique ID generator
            # .hex() is used to remove the hyphens or also called dash from the generated unique ID
            # [:10] limits the length of the UUID to 10 characters
            # .upper() to convert the obtained ID into uppercase
        super().save(*args, **kwargs)# calling django's original save() function to actually save the data in the database, without this data won't get saved
    
    def __str__(self):
        return f"{self.complaint_id} | {self.full_name} | {self.status}"