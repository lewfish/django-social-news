from django.contrib import admin
from . import models

@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'post_date'
    fields = ('title','link',)
    exclude = ('post_date',)

@admin.register(models.Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
