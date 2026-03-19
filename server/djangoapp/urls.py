from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('registration', views.registration, name='registration'),

    # Path for login
    path(route='login', view=views.login_user, name='login'),

    # Path for logout
    path(route='logout', view=views.logout_request, name='logout'),

    # Path for dealer reviews view
    # path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='get_dealer_reviews'),

    # Path for add a review view
    # path(route='add_review', view=views.add_review, name='add_review'),

    path(route='logout', view=views.logout_request, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)