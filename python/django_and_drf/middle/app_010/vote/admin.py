from django.contrib import admin
from vote.models import Vote, Person, DurrationDate

admin.site.register(Vote)
admin.site.register(Person)
admin.site.register(DurrationDate)