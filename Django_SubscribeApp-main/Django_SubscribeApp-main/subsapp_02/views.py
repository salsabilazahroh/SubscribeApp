from django.shortcuts import render
from subsapp_02.models import Customer
from subsapp_02.forms import NewSubscriber

# Create your views here.
def index(request):
    return render(request, 'subscribe_app/index.html')

def customers(request):
    customers_list = Customer.objects.order_by('first_name')
    if customers_list is not None:
        Customer_dict = {'customers': customers_list}
        return render(request, 'subscribe_app/customers.html', context=Customer_dict)
    else:
        return render(request, 'subscribe_app/customers.html', {'error_message': 'No customers found'})


def subscribe(request):
    form = NewSubscriber()

    if request.method == 'POST':
        form = NewSubscriber(request.POST)
        if form.is_valid():
            form.save(commit=True)
            # return render(request, 'subscribe_app/customers.html')
            return customers(request)
    else:    
        # form = NewSubscriber()
        print("form is not valid")

    return render(request, 'subscribe_app/subscribe.html', {'form': form})
