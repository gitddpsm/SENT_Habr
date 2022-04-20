from django.urls import path, include

from .views import IndexListView, SectionListView, SectionHelpView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('<slug:section_slug>/', SectionListView.as_view(), name='section'),
    path('<slug:section_slug>/', SectionHelpView.as_view(), name='help'),


    path('auth/', include('authapp.urls', namespace='auth'), name='auth'),
    path('article/', include('articleapp.urls', namespace='article'), name='article'),
    path('account/', include('persaccapp.urls', namespace='account'), name='account'),
]
