from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='list/')),
    path('admin/', admin.site.urls),
    path('add/', views.add_student, name='add_student'),  # HOME = LIST PAGE
    path('list/', views.student_list, name= 'student_list'),
    path('edit/<int:student_id>/', views.edit_student,name = 'edit_student'),
    path('delete/<int:student_id>/', views.delete_student,name= 'delete_student'),
    path('view/<int:pk>/', views.item_view, name='item_view'),
]