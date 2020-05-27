from django.contrib import admin
from .models import Portfolio,PortfolioSoloImg,SoloImg,Albume,ImgAlbume, Pack,Contacto

# Register your models here.


admin.site.register(Portfolio)
admin.site.register(PortfolioSoloImg)
admin.site.register(SoloImg)
admin.site.register(Albume)
admin.site.register(ImgAlbume)
admin.site.register(Contacto)
admin.site.register(Pack)


admin.site.site_header = 'Laura fotografa'