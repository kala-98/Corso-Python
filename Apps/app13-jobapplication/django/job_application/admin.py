from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    # if django finds this variable it will display all the columns
    list_display = ("first_name", "last_name", "email") 

    search_fields = ("first_name", "last_name", "email")

    list_filter = ("date", "occupation")

    ordering = ("first_name",) # ("-first_name") to do reverse order

    readonly_fields = ("occupation",)

# link our database with an admin interface ("/admin")
admin.site.register(Form, FormAdmin)