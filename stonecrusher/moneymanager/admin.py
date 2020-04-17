from django.contrib import admin
from django.apps import apps

models = apps.get_models()
models = models[6:]
# print(models)
# Register your models here.
for model in models:
    admin.site.register(model)