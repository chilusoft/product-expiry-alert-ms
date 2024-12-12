from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import ProductForm

from .models import Product, ProductBatch



def create_product(request):
    form = ProductForm()
    print(request.method)
    if request.method == 'POST':
        print('starting post request')
        form = ProductForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Process the form data
            # You can access form data like form.cleaned_data['name']
            p=Product.objects.create(
                name=form.cleaned_data['name'],
                image=form.cleaned_data['image'],
                batch=ProductBatch(id=int(form.cleaned_data['batch_number'])),
            )
            p.product_category.set([form.cleaned_data['category']].pop())
            print(p)

            # Save to database or perform other actions
            # form.save()
            print('redirecting...')
            return redirect(reverse('index:index'))  # Redirect after successful form submission
        else:
            print('form not valid')
            form = ProductForm()
        return redirect(reverse('index:index'))
    else:

        print('post request failed.')
        return redirect(reverse('index:index'))

def view_dashboard(self,request,**kwargs):

    # product_form=ProductForm.initial(
    # )

    ctx={
        'edit_product_form':ProductForm
    }
    return render(request,'products/partials/create.html',ctx)