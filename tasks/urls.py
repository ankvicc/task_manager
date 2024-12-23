from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Главная страница
    path('signup/', views.signup, name='signup'), # Регистрация
    path('profile/', views.profile, name='profile'),  # Страница профиля пользователя
    path('tasks/', views.task_list, name='task_list'),  # Список задач
    path('tasks/create/', views.task_create, name='task_create'),  # Создание задачи
    path('tasks/edit/<int:task_id>/', views.task_edit, name='task_edit'),  # Редактирование задачи
    path('tasks/delete/<int:task_id>/', views.task_delete, name='task_delete'),  # Удаление задачи
]
