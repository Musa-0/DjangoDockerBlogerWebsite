from django.contrib import admin

# Register your models here.
from Blog import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "author", "create_at", "id"]
    prepopulated_fields = {'slug': ('name',)}
    save_as = True
    save_on_top = True

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','avatar']
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','author','create_at','post','message']

class CatregoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(models.Category, CatregoryAdmin)

admin.site.register(models.Social)
