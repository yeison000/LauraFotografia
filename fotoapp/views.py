from django.shortcuts import render, redirect  
from .models import *
from django.views.generic import  View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from  django.urls import reverse_lazy
from fotoapp.forms import ContactoForm

# Create your views here.

class ListaIndex(ListView):
        model="Albume"
        template_name='index.html'
        context_object_name ='destacado'
        queryset=Albume.objects.filter(albumDestacado=True)
   
class ListarPorfolio(ListView):
        model=Portfolio
        template_name="fotoapp/album.html"
        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                context['portfolio'] = Portfolio.objects.all()
                context['portfolioimg'] = PortfolioSoloImg.objects.all()
                return context
        



class ListarSoloImg(ListView):
        model=SoloImg
        template_name="fotoapp/listarsoloimg.html"
       

        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                port=  PortfolioSoloImg.objects.get(pk = self.kwargs.get('pk',None))
                context['soloimg'] = SoloImg.objects.filter( fkPortfolioSoloImg=port.id)
                return context



class ListarAlbume(ListView):
        model= Albume
        template_name='fotoapp/listaralbume.html'
       
        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                port=  Portfolio.objects.get(pk = self.kwargs.get('pk',None))
                context['listaalbum'] = Albume.objects.filter( fkPortFolio=port.id)
                return context


class ListarCollage(ListView):
        model= ImgAlbume
        template_name='fotoapp/collage.html'
       
        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                album=  Albume.objects.get(pk = self.kwargs.get('pk',None))
                context['albumCollage'] =album
                context['collage'] = ImgAlbume.objects.filter( fkAlbume= album.id)
                return context

class Pack(ListView):
        model = Pack
        template_name='fotoapp/oferta.html'
        context_object_name ='lista'
        queryset = Pack.objects.filter()

class Contacto(CreateView):
        model = Contacto
        template_name='fotoapp/contacto.html'
        form_class = ContactoForm
        success_url = reverse_lazy('fotoapp:contacto')
