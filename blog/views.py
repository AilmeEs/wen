from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index(request):
    postes = Post.objects.all()
    return render(request, '../../../../../xue/binbin-1-master/Training/templates/index.html', {'postes': postes})
def edit(request,id):
    po=get_object_or_404(Post,id=id)
    if request.method=="POST":
        po_forms=PostForm(data=request.POST,instance=po)
        if po_forms.is_valid():
            po_forms.save()
        return redirect("index")
    else:
        po_forms=PostForm(instance=po)
    return render(request,'edit.html',{'po':po,'po_forms':po_forms})