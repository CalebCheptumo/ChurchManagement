from django.views import generic
from .models import Pastor

class PastorListView(generic.ListView):
    model = Pastor
    template_name = 'pastor_list.html'

class PastorDetailView(generic.DetailView):
    model = Pastor
    template_name = 'pastor_detail.html'

class PastorCreateView(generic.CreateView):
    model = Pastor
    fields = ['first_name', 'last_name', 'contact_number', 'pastoral_history']
    template_name = 'pastor_form.html'

class PastorUpdateView(generic.UpdateView):
    model = Pastor
    fields = ['first_name', 'last_name', 'contact_number', 'pastoral_history']
    template_name = 'pastor_form.html'

class PastorDeleteView(generic.DeleteView):
    model = Pastor
    template_name = 'pastor_confirm_delete.html'
    success_url = '/pastors/'