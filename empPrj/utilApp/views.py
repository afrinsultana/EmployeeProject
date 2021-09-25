from django.contrib.messages.api import error
from utilApp.forms import EmailForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.
def SendEmailwithAttachment(request):
    if request.method=='POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            email=form.cleaned_data['email']

            try:
                mail=EmailMessage(subject,message,settings.EMAIL_HOST_USER,[email])
                if request.FILES:
                    files=request.FILES.getlist('attach')
                    for f in files:
                        mail.attach(f.name,f.read(),f.content_type)

                mail.send()
                messages.success(request,'Email Send Successfully')
                return redirect('/')
            except Exception as ex1:

                print(ex1)
                messages.error(request,'email send hoi nai')

    else:
        form=EmailForm()

    context={'form':form}
    return render(request,'mail/mailform.html',context)

