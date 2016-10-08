from django.conf.urls import url, include
from rest_framework import routers
from eatapp import views



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'menu', views.MenusViewSet)
router.register(r'restaurant', views.ResViewSet)
router.register(r'categories', views.CatViewSet)
router.register(r'menupage', views.MenusViewSetRes)
router.register(r'restpos', views.restpos)
router.register(r'customer', views.Customerviewset)


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^restpost/', views.restpost),
    url(r'^index/', views.detail),

]	