from django.shortcuts import render
from main.forms import StackForm, PortfolioForm, ArchiveForm, ContactForm
from main.models import Stack, Portfolio, Archive, Contact
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

StackFormSet = formset_factory(StackForm,   extra=1)
PortfolioFormSet = formset_factory(PortfolioForm, extra=1)
ArchiveFormSet = formset_factory(ArchiveForm, extra=1)
template = "backend/backend.html"
info = ""
error = ""
target = ""

def landing(request):
  template = "index.html"
  title = "Pius Lucky"
  stack = Stack.objects.all()
  portfolio = Portfolio.objects.all()
  archive = Archive.objects.all()
  context = {
    "title":title,
    "stack":stack,
    "portfolio":portfolio,
    "archive":archive
  }
  return render(request, template, context)
  


def post_contact(request):
  if request.method == 'POST' and request.is_ajax():
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
      instance = contact_form.save(commit=False)
      name = contact_form.cleaned_data['name']
      email = contact_form.cleaned_data['email']
      subject = contact_form.cleaned_data['subject']
      message = contact_form.cleaned_data['message']
      emailFrom = email
      # Save first to retrieve timestamp
      instance.save()
      emailTo = settings.EMAIL_HOST_USER 
      with open(settings.BASE_DIR + "/templates/attachments/__contact-mail.txt") as txt_file:
        contact_message = txt_file.read()
      message1 = EmailMultiAlternatives(subject=subject, body=message, from_email= emailFrom, to=[emailTo,] )
      html_template1 = get_template("attachments/__contact-mail.html").render({"to_email":[emailTo,],
      "subject":subject,"name":name,"email":email,"message":message, "emailFrom":emailFrom, "timestamp":instance.timestamp })
      message1.attach_alternative(html_template1, "text/html")
      try:
        info = "Successfully sent!"
        message1.send()
        return JsonResponse({"success":True, "info":info}, status=200)
        
      except:
        info = "Failed, try again!"
        return JsonResponse({"success":False, "info":info}, status=400)
    else:
      info = "Invalid form, try again!"
      return JsonResponse({"success":False, "info":info}, status=400)
  return JsonResponse({"success":False}, status=400)

def backend(request):
    if request.user.is_authenticated:
      title = "Backend"
      t_formset = StackFormSet(request.GET or None, prefix='t_formset')    
      portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')     
      arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')     
      return render(request, template, {
        "title":title,
        "formset":t_formset, 
        "portf_formset":portf_formset,
        "arch_formset":arch_formset
      })
    else:
      return HttpResponse ("Not allowed!")
    

def postStack(request):
  title = "Technologies"
  if request.POST.get('get_stack_name') == 'get_stack_value':
    t_formset = StackFormSet(request.POST, request.FILES, prefix="t_formset")
    if t_formset.is_valid():
        for form in t_formset:
            instance = form.save(commit=False)
            instance.icon = form.cleaned_data.get('icon')
            instance.tech = form.cleaned_data.get('tech')
            instance.about_tech = form.cleaned_data.get('about_tech')
            if instance.icon != None and instance.tech != None and instance.about_tech != None:
              form.save()
            else:        
              portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')  
              arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')  
              error = "Invalid stack form, Try again!"
              return render(request, template, {
                "title":title, 
                "error":error, 
                "resume_form":resume_form,
                "formset":t_formset,                            
                "portf_formset":portf_formset,
                "arch_formset":arch_formset
              })
        info = "successfully created"   
        target = "Stack"     
        portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')  
        arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')  
        return render(request, template, {
          "title":title,
          "info":info, 
          "target":target, 
          "formset":t_formset,          
          "portf_formset":portf_formset,
          "arch_formset":arch_formset
        })
    else: 
        portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')  
        arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')  
        error = "Invalid Stack form, Try again!"
    return render(request, template, {
      "title":title,
      "error":error,
      "formset":t_formset,                                
      "portf_formset":portf_formset,
      "arch_formset":arch_formset
    })



def postPortf(request):
  title = "Portfolio"
  info = ""
  error = ""
  target = ""
  if request.POST.get('get_portf_name') == 'get_portf_value':
    portf_formset = PortfolioFormSet(request.POST, request.FILES, prefix="portf_formset")
    if portf_formset.is_valid():
        for form in portf_formset:
            instance = form.save(commit=False)
            instance.position = form.cleaned_data.get('position')
            instance.description_header = form.cleaned_data.get('description_header')
            instance.description_body = form.cleaned_data.get('description_body')
            instance.image = form.cleaned_data.get('image')
            instance.github = form.cleaned_data.get('github')
            instance.link = form.cleaned_data.get('link')
            if (instance.position != None and 
            instance.description_header != None and  
            instance.description_body != None and  
            instance.image != None and   
            instance.github != None and  
            instance.link != None):form.save()
            else:
                t_formset = StackFormSet(request.GET or None, prefix='t_formset')   
                arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset') 
                error = "Invalid Portfolio form, Try again!"
                return render(request, template, {
                  "title":title,
                  "info":info, 
                  "error":error,
                  "target":target, 
                  "formset":t_formset, 
                  "portf_formset":portf_formset,
                  "arch_formset":arch_formset
                })
        info = "successfully created"   
        target = "Portfolio Item" 
        t_formset = StackFormSet(request.GET or None, prefix='t_formset')        
        arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')                          
        return render(request, template, {
          "title":title,
          "info":info, 
          "error":error,
          "target":target, 
          "formset":t_formset,                                
          "portf_formset":portf_formset,
          "arch_formset":arch_formset
        })
    else:
        t_formset = StackFormSet(request.GET or None, prefix='t_formset')      
        arch_formset = ArchiveFormSet(request.GET or None, prefix='arch_formset')                           
        error = "Invalid Portfolio form, Try again!"
    return render(request, template, {
      "title":title,
      "info":info, 
      "error":error,
      "target":target, 
      "formset":t_formset,                             
      "portf_formset":portf_formset,
      "arch_formset":arch_formset
    })


def postArch(request):
  title = "Archive"
  info = ""
  error = ""
  target = ""
  if request.POST.get('get_archive_name') == 'get_archive_value':
    arch_formset = ArchiveFormSet(request.POST, request.FILES, prefix="arch_formset")
    if arch_formset.is_valid():
        for form in arch_formset:
            instance = form.save(commit=False)
            instance.position = form.cleaned_data.get('position')
            instance.github = form.cleaned_data.get('github')
            instance.external_link = form.cleaned_data.get('external_link')
            instance.title = form.cleaned_data.get('title')
            instance.description = form.cleaned_data.get('description')
            instance.backend_tech = form.cleaned_data.get('backend_tech')
            instance.timestamp = form.cleaned_data.get('timestamp')
            if (instance.position != None and 
            instance.position != None and  
            instance.github != None and  
            instance.external_link != None and  
            instance.title != None and  
            instance.description != None and  
            instance.backend_tech != None):form.save()
            else:
                t_formset = StackFormSet(request.GET or None, prefix='t_formset')      
                portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')  
                error = "Invalid Archive form, Try again!"
                return render(request, template, {
                  "title":title,
                  "info":info, 
                  "error":error,
                  "target":target, 
                  "formset":t_formset, 
                  "portf_formset":portf_formset,
                  "arch_formset":arch_formset
                })
        info = "successfully created"   
        target = "Archive Item" 
        t_formset = StackFormSet(request.GET or None, prefix='t_formset')          
        portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')                       
        return render(request, template, {
          "title":title,
          "info":info, 
          "error":error,
          "target":target, 
          "formset":t_formset,                                
          "portf_formset":portf_formset,
          "arch_formset":arch_formset
        })
    else:
        t_formset = StackFormSet(request.GET or None, prefix='t_formset')       
        portf_formset = PortfolioFormSet(request.GET or None, prefix='portf_formset')                          
        error = "Invalid Archive form, Try again!"
    return render(request, template, {
      "title":title,
      "info":info, 
      "error":error,
      "target":target, 
      "formset":t_formset, 
      "portf_formset":portf_formset,
      "arch_formset":arch_formset
    })
    
