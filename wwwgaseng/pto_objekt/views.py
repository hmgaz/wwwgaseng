# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views import generic
from django.core.urlresolvers import reverse
from pto_objekt.models import osnovanie , objekt


class IndexView(generic.ListView):
    template_name = 'pto/index.html'
    #context_object_name = 'latest_question_list'
    model = objekt
    #def get_context_data(self, **kwargs):
        #return generic.ListView.get_context_data(self, **kwargs)
 #   def get_queryset(self):
 #       return objekt.objects.ge_naimenovaniekr
