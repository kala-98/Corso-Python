from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = ( # 1st part is for the code, 2nd one to be displayed
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Item(models.Model):
    meal = models.CharField(max_length = 1000, unique = True)
    description = models.CharField(max_length = 2000)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    meal_type = models.CharField(max_length = 200, choices = MEAL_TYPE)
    author = models.ForeignKey(User, on_delete = models.PROTECT) # with CASCADE it is possible to delete the user/cooker and its inherited meals. SET_NULL will keep the dishes but not the author
    status = models.IntegerField(choices = STATUS, default = 0)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True) # verify when the item is modified

    def __str__(self):
        return self.meal