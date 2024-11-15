from django.db import models

# Create User Data Model
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.username
    
# Create Traffic Law Model
class TrafficLaw(models.Model):
    state = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    law_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return
    
# Create Traffic Violation Model
class Violation(models.Model):
    violation_code = models.CharField(max_length=10, unique=True)
    violation_law = models.ForeignKey(TrafficLaw, on_delete=models.CASCADE, related_name='violations')
    penalty = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.violation
    
# Create bookmark model
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE, related_name='bookmarks')

    def __str__(self):
        return self.violation