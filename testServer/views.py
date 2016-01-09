from django.shortcuts import render, redirect
from django.conf import settings
import subprocess
import os
import uuid

def setup_javadir(f):
  # Create the folder if it doesn't exist.
  try:
    os.mkdir(settings.JAVA_DIR)
  except:
    pass

  # Create a unique folder name for this java run
  folder = os.path.join(settings.JAVA_DIR, str(uuid.uuid1()))
  filename = os.path.join(folder, f.name)
  print(filename)


def index(request):
  return render(request, 'index.html')

def submit(request):
  if request.method == 'GET':
    return redirect(index)

  f = request.FILES.get('java_file')

  setup_javadir(f)

  p1 = subprocess.Popen("java -jar %s" % f.temporary_file_path(), shell=True, stdout=subprocess.PIPE)
  message = p1.stdout.read()

  context = {
    'message': message
  }

  return render(request, 'index.html', context)