from django.urls import path

from .views import CadastroListView, CadastroDetailView

urlpatterns = [
    path('', CadastroListView.as_view()),
    path('<pk>/', CadastroDetailView.as_view()),
]
