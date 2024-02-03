from django.contrib import admin
from .models import Client
# from django.contrib.auth import get_user_model


# Register your models here.


# User = get_user_model()
# admin.site.unregister(User)

class ClientInline(admin.StackedInline):
    model = Client
    extra = 0

# class UserAdmin(admin.ModelAdmin):
#     # inlines = [ClientInline]
#     list_display = ['id','username', 'email', 'password']
#     # fields = ['username', 'email', 'password', 'is_staff']

# admin.site.register(User, UserAdmin)


# admin.site.register(ClientProfile)

# class ClientProfileInline(admin.StackedInline):
#     model = ClientProfile
#     extra = 0
#     # fields = ['client', 'contactno', 'bank_account', 'weblink']

class ClientAdmin(admin.ModelAdmin):

    list_display = ['id', 'user', 'Full_name', 'email', 'country', 'contactno', 'bank_account',  'img']
    # raw_id_field = ['user']
    search_fields = ['Full_name']
    
admin.site.register(Client, ClientAdmin)


