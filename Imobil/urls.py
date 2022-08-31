from django.urls import path
from . import views
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='imobil-home'),
    path('imobil/<int:pk>/', PostDetailView.as_view(), name='imobil-detail'),
    path('about', views.about, name='imobil-about'),
    path('imobil/new/', PostCreateView.as_view(), name='imobil-create'),
    path('imobil/<int:pk>/update/', PostUpdateView.as_view(), name='imobil-update'),
    path('imobil/<int:pk>/delete/', PostDeleteView.as_view(), name='imobil-delete'),
]
