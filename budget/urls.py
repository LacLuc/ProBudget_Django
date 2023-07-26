from django.urls import path

from budget.views import contato, home, sobre

urlpatterns = [
    path('', home),  # Home
    path('contato/', contato),  # /contato/
    path('sobre/', sobre),  # /sobre/
]
