from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from .models import Etablissement
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
import re
from .models import Etablissement
from .serializers import EtablissementSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.decorators import api_view

# Create your views here.

# Serialization
class EtablissementList(mixins.CreateModelMixin, generics.ListAPIView):

	lookup_field = 'pk'
	#queryset = Etablissement.objects.all()
	serializer_class = EtablissementSerializer

	def get_queryset(self):
		qs = Etablissement.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			qs = qs.filter(Q(nom__contains=query)|Q(ville__contains=query)).distinct()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)



class EtablissementDetailList(generics.RetrieveUpdateDestroyAPIView):

	lookup_field = 'pk'
	#queryset = Etablissement.objects.all()
	serializer_class = EtablissementSerializer

	def get_queryset(self):
		return Etablissement.objects.all() 


# Etablissement CRUD
class EtablissementListView(ListView):
	model = Etablissement


class EtablissementDetailView(DetailView):
	model = Etablissement

	def get_context_data(self, **kwargs):
		context = super(EtablissementDetailView, self).get_context_data(**kwargs)
		return context
