from django.db import models

# defining the database's model
class Form(models.Model): 
    first_name = models.CharField(max_length = 80)
    last_name = models.CharField(max_length = 80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length = 80)

    # obtain a string representation of the instance
    # (what should be printed when the print is used)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

