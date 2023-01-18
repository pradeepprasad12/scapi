
from django.urls import path,include
from student.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('sdata',views.Studentviewset,basename='student')
router.register('cdata',views.Classviewset,basename='class')


urlpatterns = [
     path('',include(router.urls)),
]