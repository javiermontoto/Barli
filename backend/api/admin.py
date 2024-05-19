from django.contrib import admin
from api.models import UserProfile, Bar, Advertisement, Table, Booking, AdminProfile


admin.site.register(UserProfile)
admin.site.register(AdminProfile)
admin.site.register(Bar)
admin.site.register(Advertisement)
admin.site.register(Table)
admin.site.register(Booking)
