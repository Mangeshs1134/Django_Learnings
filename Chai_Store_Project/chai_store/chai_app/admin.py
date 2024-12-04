from django.contrib import admin
from .models import Chai_Variety , Chai_Reviews , Certificates, Stores

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = Chai_Reviews
    extra = 3

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display=('name', 'location' ,'get')
    filter_horizontal = ('avail',)

class CertificateAdmin(admin.ModelAdmin):
    list_display= ('chai' , 'certificate_num','issue_date', 'exp_date')




admin.site.register(Chai_Variety , ChaiVarietyAdmin)
admin.site.register(Stores , StoreAdmin)
admin.site.register(Certificates , CertificateAdmin)

# admin.site.register(Chai_Reviews)
