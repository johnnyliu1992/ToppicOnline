import subprocess, os, mimetypes
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from django.utils.encoding import smart_str





from pweb.forms import DocumentForm
from pweb.models import Document

# Create your views here.

def index(request):
	
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			documents = list(Document.objects.all().values_list('document',flat=True))
			if documents!=[]:
				documents=documents[0].split('/')[1]
			return render(request, 'pweb/index.html', {'form': form, 'documents':documents})
	else:
		form = DocumentForm()
		documents = list(Document.objects.all().values_list('document',flat=True))
		if documents!=[]:
			i_clean=Document.objects.all().delete()
			documents=[]
			go_to_data_folder_command='cd '+settings.MEDIA_ROOT+'/'+'toppic_data_to_use'
			clean_previous_data_command=go_to_data_folder_command+' && '+'rm *'# /S /Q'
			clean_previous_data=subprocess.check_output(clean_previous_data_command, shell=True).decode("utf-8").replace('\r\n','')
		return render(request, 'pweb/index.html', {'form': form, 'documents':documents})

	
	
def analyze(request):
	if request.method=='POST':
		data_file_name=list(Document.objects.all().values_list('document',flat=True))[0].split('/')[1]
		request.session['data_file_name']=data_file_name#get data file name into session
		data_path=settings.MEDIA_ROOT+'/'+'toppic_data_to_use'
		request.session['data_path']=data_path#get data path into session
		go_to_data_folder_command='cd'+' '+data_path
		'''toppic command'''
		maxcs=request.POST.get('maxcs')
		maxmm=request.POST.get('maxmm')
		et=request.POST.get('et')
		snr=request.POST.get('snr')
		piws=request.POST.get('piws')
		ms1spec=request.POST.get('ms1spec')
		pre_toppic_command=' ../toppic-linux-1.1.2/topfd '
		if maxcs != '':
			pre_toppic_command=pre_toppic_command+'-c '+maxcs+' '
		if maxmm != '':
			pre_toppic_command=pre_toppic_command+'-m '+maxmm+' '
		if et != '':
			pre_toppic_command=pre_toppic_command+'-e '+et+' '
		if snr != '':
			pre_toppic_command=pre_toppic_command+'-s '+snr+' '
		if piws != '':
			pre_toppic_command=pre_toppic_command+'-w '+piws+' '
		if ms1spec != None:
			pre_toppic_command=pre_toppic_command+'-n '
		run_toppic_command=pre_toppic_command+data_file_name
		'''final command'''
		final_command=go_to_data_folder_command+' &&'+' cd ../toppic-linux-1.1.2/'+' && '+'ls'#run_toppic_command
		result=subprocess.check_output(final_command, shell=True).decode("utf-8")
		'''check output'''
		check_output_command=go_to_data_folder_command+' && ' +'ls'# /b'
		request.session['check_output_command']=check_output_command#store check_output_command to session
		check_output_num=subprocess.check_output(check_output_command, shell=True).decode("utf-8").split('\r\n')
		check_output_num=len(check_output_num)
		if check_output_num>=2:
			note=1
		else:
			note=0
		return render(request, 'pweb/analyze.html', {'note':note, 'final_command':result})
	else:
		return render(request, 'pweb/analyze.html')

		
		
		

		
		
def result(request):
	data_file_name=request.session['data_file_name']
	check_output_command=request.session['check_output_command']
	output_files=subprocess.check_output(check_output_command, shell=True).decode("utf-8").split('\r\n')
	output_files.remove('')
	output_files.remove(data_file_name)
	return render(request, 'pweb/result.html',{'data_file_name':data_file_name,'output_files':output_files})

	
def download(request,file_name):
	data_path = request.session['data_path']
	file_path = data_path+'/'+file_name
	file_wrapper = FileWrapper(open(file_path))
	file_mimetype = mimetypes.guess_type(file_path)
	response = HttpResponse(file_wrapper, content_type=file_mimetype )
	response['X-Sendfile'] = file_path
	response['Content-Length'] = os.stat(file_path).st_size
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
	return response
	
def download_sample(request,file_name):
	data_path = settings.MEDIA_ROOT
	file_path = data_path+'/'+file_name
	file_wrapper = FileWrapper(open(file_path))
	file_mimetype = mimetypes.guess_type(file_path)
	response = HttpResponse(file_wrapper, content_type=file_mimetype )
	response['X-Sendfile'] = file_path
	response['Content-Length'] = os.stat(file_path).st_size
	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name) 
	return response
	
