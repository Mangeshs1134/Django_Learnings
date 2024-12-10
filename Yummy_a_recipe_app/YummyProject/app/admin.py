from django.contrib import admin
from .models import Yummy, RecipeLikes
# Register your models here.

class LikeInline(admin.TabularInline):
    model = Yummy.likes.through
    extra = 1

class YummyAdmin(admin.ModelAdmin):
    list_display = ('user', 'text'[:10],'view_count', 'like_or_unlike', 'recipe_name', 'created_at', 'updated_at', )

    def get_likes(self, obj):
        list = []
        for likes in obj.likes.all():
            list.append(likes)
        return len(list)
    get_likes.short_description = 'Likes'

    inlines = [LikeInline]

class RecipesLikesAdmin(admin.ModelAdmin):
    list_display= ('user', 'recipe', 'created', 'isLikedPost')


admin.site.register(Yummy, YummyAdmin)
admin.site.register(RecipeLikes, RecipesLikesAdmin)


# admin.site.register(Yummy , YummyAdmin )

