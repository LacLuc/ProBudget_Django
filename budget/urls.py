from django.urls import path

from budget.views import categories, fontpayers, home, monthYears, sobre

urlpatterns = [
    path('', home),  # Home
    path('categories/', categories),  # /category/
    path('sobre/', sobre),  # /sobre/
    path('monthYears/', monthYears),  # /monthYears
    path('fontpayers/', fontpayers),  # /fontpayers
]
