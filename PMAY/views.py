from django.shortcuts import render
from django.views import generic
from .models import UserRequest
 
class IndexView(generic.TemplateView):
    template_name = 'PMAY/index.html'
    
def saveContactInfo(request):
    pc = UserRequest(
        user_name = request.session.get('member_id'),
        first_name = request.POST['contFirstName'],
        middle_name = request.POST['contMiddleName'],
        last_name = request.POST['contLastName'],
        address = request.POST['contAddress'],
        city = request.POST['contCity'],
        state = request.POST['contState'],
        zipCode = request.POST['contZip'],   
        adhaar_Number = request.POST['contPhoneMain'],
        cellPhone = request.POST['contPhoneCell'],
        email = request.POST['contEmail'])
    pc.save()
    return render(request, 'water_management/index.html')

class ModifyView(generic.TemplateView):
    template_name = 'PMAY/modify.html'
    
def readData(request):
    if request.session.get('member_id'):
        contact = UserRequest.objects \
            .filter(user_name__exact = request.session.get('member_id')).values();
        return render(request, "PMAY/modify.html", {"contact_list": contact,})
    return render(request, "login/index.html")

def updateContactInfo(request):
    if request.session.get('member_id'):
        pc = UserRequest.objects.get(user_name=request.session.get('member_id'))
        pc.user_name = request.session.get('member_id')
        pc.first_name = request.POST['contFirstName']
        pc.middle_name = request.POST['contMiddleName']
        pc.last_name = request.POST['contLastName']
        pc.address = request.POST['contAddress']
        pc.city = request.POST['contCity']
        pc.state = request.POST['contState']
        pc.zipCode = request.POST['contZip']
        pc.adhaar_Number = request.POST['contPhoneMain']
        pc.cellPhone = request.POST['contPhoneCell']
        pc.email = request.POST['contEmail']
        pc.save()
        return render(request, 'dashboard/index.html')
    else:
        return render(request, 'login/index.html')