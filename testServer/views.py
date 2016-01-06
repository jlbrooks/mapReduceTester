from django.shortcuts import render, redirect
import subprocess
import os

def index(request):
  return render(request, 'index.html')

def submit(request):
  if request.method == 'GET':
    return redirect(index)

  f = request.FILES.get('java_file')

  print(f.temporary_file_path())

  p1 = subprocess.Popen("java -jar %s" % f.temporary_file_path(), shell=True, stdout=subprocess.PIPE)
  message = p1.stdout.read()

  context = {
    'message': message
  }

  return render(request, 'index.html', context)