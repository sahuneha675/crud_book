from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name="index"),
    path('student_registration/',views.student_registration, name="student_registration"),
    path('register_data/',views.register_data, name="register"),
    path('student_login/',views.student_login, name="login"),
    path('login_data/', views.login_form, name="login"),
    path('profile/',views.profile, name="profile"),

    path('issue_book/', views.view_issued_book, name="issue_book"),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
