#from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import gas_supply_demand
from .models import complain_manage

class IndexView(generic.TemplateView):
    template_name = 'gas_supply/index.html'

def saveMedHistory(request):
    if request.session.get('member_id'):
        user = request.session.get('member_id')
        pat_medHis = gas_supply_demand.objects \
            .filter(user_name__exact = user);
        fields = request.POST 
        if pat_medHis.count() == 0:
            for field in fields:
                field_val = request.POST[field]
                if 'Info' not in field and field_val == '1': 
                    if (field + 'Info') in fields:
                        field_text = fields[field + 'Info']
                    else:
                        field_text = field_val

                    pm = gas_supply_demand(
                        user_name = user,
                        info_type = field,
                        med_history = field_text)
                    pm.save()
            return render(request, 'electricity_management/index.html')
        else:
            for field in fields:
                field_val = request.POST[field]
                if 'Info' not in field and field_val == '1' or field_val == '0':
                    if (field + 'Info') in fields:
                        field_text = fields[field + 'Info']
                    else:
                        field_text = field_val
                    pm = pat_medHis.filter(info_type__exact = field)
                    if pm.count() > 0:
                        pm = pat_medHis.get(info_type = field)
                        if pm.info_type in fields and \
                            request.POST[pm.info_type] == '0':
                            pm.delete()
                        else:
                           if pm.info_type in fields and \
                                fields[pm.info_type] == '1' and \
                                len(field_text) > 1 and \
                                pm.med_history != field_text:
                            pm.med_history = field_text
                            pm.save()
                    else:
                        if pm.count() == 0 and field_val == '1':
                            pm = gas_supply_demand(
                                user_name = user,
                                info_type = field,
                                med_history = field_text)
                            pm.save()

            for pm in pat_medHis:
                if pm.info_type not in fields:
                    pm.delete()

            return render(request, "dashboard/index.html")
    return render(request, "login/index.html")

def readData(request):
    if request.session.get('member_id'):
        user = request.session.get('member_id')
        pat_medHis = gas_supply_demand.objects \
            .filter(user_name__exact = user);
        medHis = complain_manage.objects \
            .order_by('med_history_id');

        if pat_medHis.count() == 0:
            return render(request, "gas_supply/index.html", {"medHis_info":{"medhis_list": medHis,},})
        else:
            objs = dict()
            for pm in pat_medHis:
                objs.update({pm.info_type : pm.med_history})
        return render(request, "gas_supply/modify.html", {"medHis_info":{"pat_medhis_list": objs,"medhis_list": medHis,},})
    return render(request, "login/index.html")