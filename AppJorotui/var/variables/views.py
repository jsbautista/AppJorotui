from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from .forms import VariableForm
from .logic.variable_logic import get_variables, create_variable
from .models import Variable
from django.contrib.auth.decorators import login_required
from monitoring.auth0backend import getRole

def variable_list(request):
    queryset = request.GET.get("buscar")
    variables = get_variables()

    if queryset:
        variables = filter(lambda variable: queryset.lower() in variable.tipo.lower() or queryset.lower() in variable.name.lower(), variables)

    context = {
        'variable_list': variables
    }

    return render(request, 'Variable/variables.html', context)

def VariableList(request):
    queryset = Variable.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)


@login_required
def variable_create(request):
	role = getRole(request)
	if role == "Admin":
		if request.method == 'POST':
			form = VariableForm(request.POST)
			if form.is_valid():
				create_variable(form)
				messages.add_message(request, messages.SUCCESS, 'Se creo de forma exitosa el  producto')
				return HttpResponseRedirect(reverse('variableCreate'))
			else:
				print(form.errors)
		else:
			form = VariableForm()
		context = {
			'form': form,
		}
		return render(request, 'Variable/variableCreate.html', context)
	else:
		return HttpResponse("Usuario no Autorizado")

@login_required
def variable_edit(request,variable_id):
	role = getRole(request)
	if role == "Admin" or role=="Disenador":
		instancia = Variable.objects.get(id=variable_id)
		form = VariableForm(instance=instancia)
		if request.method== 'POST':
			form = VariableForm(request.POST,instance=instancia)

			if form.is_valid():

				instancia=form.save(commit=False)
				instancia.save()
		return render(request,"Variable/variableEdit.html",{'form':form})
	else:
		return HttpResponse("Usuario no Autorizado")
