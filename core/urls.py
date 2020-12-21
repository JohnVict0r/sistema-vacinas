from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', views.auth),
    path('me/vaccines', views.user_vaccines),
    path('me/agendamentos', views.user_agendamentos),
    path('patients/vaccines', views.pacient_vaccines),
    path('vaccines/', views.vaccines),
    path('vaccines/<int:pk>', views.vaccines),
    path('agendamentos/', views.agendamentos),
    path('atendimentos/', views.atendimentos),
    path('ufs', views.uf_list),
    path('municipios', views.municipios),
]
