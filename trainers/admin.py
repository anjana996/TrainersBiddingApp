from django.contrib import admin

# Register your models here.
from trainers.models import PersonalProfile,TrainerBidding
admin.site.register(PersonalProfile)
admin.site.register(TrainerBidding)

