from django.urls import path

from .views import home, add_student, delete_student, update_student,do_update_student

urlpatterns = [
     path('home/', home),
     path('add_student/', add_student),
     path('delete_student/<int:id>', delete_student),
     path('update_student/<int:id>',update_student),
     path('do_update_student/<int:id>',do_update_student)

    ]