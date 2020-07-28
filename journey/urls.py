from django.urls import path
from .views import index_view,home_view,add_view,desc_view
from django.conf import settings
from django.conf.urls.static import static
app_name="memory"
urlpatterns=[
    path('index/',index_view,name='index'),
    path('home/',home_view,name='home'),
    path('add/',add_view,name='add'),
    path('work/<int:id>',desc_view,name='desc'),
    ]+ static(settings.STATIC_URL, 
                              document_root=settings.STATIC_ROOT)