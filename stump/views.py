from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import json
from .forms import ImgForm

# Create your views here.

def index(request):

	if request.method == 'POST':
		imgForm = ImgForm(request.POST)
		if imgForm.is_valid():
				outpic_url = imgForm.cleaned_data['picImg'] + '-/overlay/3904bdef-47b2-4672-a04b-e7bdefd958eb/20px20p/80p/'
		return HttpResponse(json.dumps(outpic_url), content_type="application/json")
	else:
		imgForm = ImgForm()
	return render(request,'stump/index.html',{'form':imgForm})
