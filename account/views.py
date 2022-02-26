from django.shortcuts import render, redirect, get_object_or_404
import config
from django.contrib import messages
from account.models import Code
from datetime import datetime
from django.http import HttpResponse
from .forms import CodeForm
from django.views.generic import ListView, DetailView

# Create your views here.
def view(request):
    config.code = config.code + 1
    code = Code.objects.filter(user_id = request.user.id)
    return render(request, 'code.html', {'code_list':code, 'code':config.code})

#Function to save code form.
def add(request):
    if request.method == 'POST':
        state = request.POST['state']
        type_of = request.POST['atype']
        reference_number = request.POST['rnumber']
        d_type = request.POST['dtype']
        created_date = datetime.now()
        user_id = request.user.id
        generated_code = state[:2]+type_of+d_type+ str(config.code)
        code = Code(state= state, type_of= type_of, reference_number = reference_number, d_type = d_type,
                    created_date = created_date,code= generated_code, user_id=user_id)
        
        if len(reference_number) > 20:
            messages.info(request, 'Reference number can not be greater than 20 digit.Please try again.')
            return redirect('../')

        code.save()
        messages.info(request, 'Code has been created: '+generated_code)
        return redirect('../')

    else:
        messages.info(request, 'Something went wrong. Please try again.')
        return redirect('../')


#Function to edit code form.
def edit(request, code_id):
    code = get_object_or_404(Code, pk=code_id, user_id= request.user.id)
    form = CodeForm(request.POST or None, instance=code)
    if form.is_valid():
        form.save()
        messages.info(request, 'Successfully updated data.')
        return redirect('../')
    return render(request, 'edit.html', {'form':form})


#Function to delete code form.
def delete(request, code_id):
    code = get_object_or_404(Code, pk=code_id, user_id= request.user.id)
    if request.method=='POST':
        code.delete()
        messages.info(request, 'Successfully deleted data.')
        return redirect('../')
    return render(request, 'delete.html', {'object':code})

