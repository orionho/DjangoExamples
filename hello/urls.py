from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<str:name>",views.greet, name="greet"),
    path("orion",views.orion, name="orion"),
    path("david",views.david, name="david"),
]