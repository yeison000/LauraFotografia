from .views import *
from django.urls import path

urlpatterns = [
    
    path('album/',ListarPorfolio.as_view(), name ='album'),
    
    path('contacto/',Contacto.as_view(), name='contacto'),
    path('pack/',Pack.as_view(), name='pack'),
    path('listaralbume/<int:pk>',ListarAlbume.as_view(), name ='listaralbume'),
    path('collage/<int:pk>',ListarCollage.as_view(), name ='collage'),
    path('listarsoloimg/<int:pk>',ListarSoloImg.as_view(), name ='listarsoloimg'),

]