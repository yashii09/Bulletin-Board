from django.shortcuts import render, HttpResponse, redirect
from dashboard.models import FilesAdmin
# Create your views here.
def student(request):
	return render(request, 'branchboard/board.html', {'student':True, 'teacher':False})
def teacher(request):
	return render(request, 'branchboard/board.html', {'student':False, 'teacher':True})
def upload(request):
	if request.method == "POST":
		file2 = request.FILES["file"]
		filename = request.POST["name"]
		branch = request.POST["branch"]
		if len(filename) != 0:
			document = FilesAdmin.objects.create(adminupload = file2, title = filename, branch = branch)
			document.save()
			return render(request, 'branchboard/board.html', {'student':False, 'teacher':True, 'success':True})
		else:
			return render(request, 'branchboard/board.html', {'student':False, 'teacher':True, 'name':True})
	return render(request, 'branchboard/fileupload.html')