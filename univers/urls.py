from django.urls import path, include
from . import views

urlpatterns = [
    path('home/<int:user_id>', views.home, name = 'univers_home'),
    path('home/form/<int:user_id>/<verbe>', views.homeForm, name = 'univers_home_form'),
    path('artistic-tastes/<int:user_id>', views.artistic_tastes, name = 'univers_artistic_tastes'),
    path('appearance/<int:user_id>', views.appearance, name = 'univers_appearance'),
    path('reaction/<int:user_id>', views.reaction, name = 'univers_reaction'),
    path('book/<int:user_id>', views.book, name = 'univers_book')
]
