from django.shortcuts import render
from .models import project
from django.views.generic import CreateView
from .forms import myform
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    mydata=project.objects.all()
    return render(request,'myapp/index.html',{"manoj":mydata})

class forms(CreateView):
    model = project
    form_class = myform
    template_name ='myapp/myform.html'
    success_url =reverse_lazy('home')


# def edit_data(request,id):
#     post_data=get_object_or_404(MYBLOGAPP,id=id)
#     if request.method=='POST':
#         form_data=mydata(request.POST,instance=post_data)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect('home')
#     else:
#         form_data=mydata(instance=post_data)
#         myinfo={"form_data":form_data}
#     return render(request,'myapp/edit.html',myinfo)

