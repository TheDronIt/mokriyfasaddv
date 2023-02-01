from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from image_uploader_widget.widgets import ImageUploaderWidget

admin.site.register(Category)
admin.site.register(Service)
admin.site.register(ServiceImage)
admin.site.register(Portfolio)
admin.site.register(PortfolioImage)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Product, ProductAdmin)
admin.site.register(Certificate)
admin.site.register(Jobs)