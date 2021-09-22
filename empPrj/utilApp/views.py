from django.shortcuts import render

# Create your views here.
def SendEmailwithAttachment(request):
    if request.method=='POST':
        pass
    else:
        pass

    context={}
    return render(request,'mail/mailform.html',context)

