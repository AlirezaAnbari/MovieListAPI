from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (WatchList,
                     StreamPlatform,
                     Review,
                    )

# Register your models here.
class CustomReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ["id", "review_user", "rating","watchlist",]
    list_filter = ["rating","watchlist",]
    
    
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review, CustomReviewAdmin)