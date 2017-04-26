from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Max,Count
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from claroapp.models import *
from claro import settings
from django.db import transaction
from django.contrib.auth.hashers import *
from django.core.mail import send_mail

from django.utils.six.moves import range
from django.http import StreamingHttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt
import time
import collections
import xlrd
import json 
import csv
import simplejson
import xlwt
import requests
import os
from PIL import Image
from resizeimage import resizeimage
from claro.settings import *
from datetime import datetime,timedelta
from django.contrib.auth import authenticate

from django.contrib.sites.shortcuts import get_current_site


def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def home(request):



	return render(request, 'home.html',{})


def cliente(request):



	return render(request, 'cliente.html',{})



def subir(request):



	return render(request, 'subir.html',{})


def uploadfile(request):

	if request.method == 'POST':

		process_file = request.FILES['file']

		cliente = request.POST['anio']
		
		mes = request.POST['mes']

		proveedor = request.POST['proveedor']

		cartera = request.POST['cartera']

		Lote(file=process_file).save()

		id_lote = Lote.objects.all().values('id').order_by('-id')[0]['id']

		process_file = Lote.objects.get(id=id_lote).file

		xls_name = '/var/www/html/'+str(process_file)

		print xls_name

		book = xlrd.open_workbook(xls_name)

		sh = book.sheet_by_index(0)
		
		date =datetime.now()
	
		for rx in range(sh.nrows):

			for col in range(sh.ncols):

					nombre = None

					if col == 0:

						dni= str(sh.row(rx)[col]).split("u")[1].replace("'","")

					if col == 1:

						nombre= str(sh.row(rx)[col]).split("u")[1].replace("'","")

					Base(dni=dni,nombre=nombre).save()

					#number:45514207.0
					# text:u'JONN MICHAEL MARTELL CERPA'
					# xldate:42822.0
					# xldate:42843.0
					# text:u'MC'
					# text:u'5123128196781165'
					# xldate:44531.0
					# text:u'APROBADA'
					# number:959720.0
					# empty:u''
					# number:8089104.0
					# text:u'PV0418362119'
					# number:1.0
					# number:25.0


			print '________________________________________'

		return render(request, 'subir.html',{})






