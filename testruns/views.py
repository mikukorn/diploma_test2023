from django.views.generic import ListView
from testruns.droneci_script import update_runs
from integrations.models import DroneCIListResults


class DroneCIRunListIndex(ListView):
    model = DroneCIListResults
    template_name = 'testruns/index.html'
    context_object_name = 'runs_list'
    paginate_by = 10

    def get_last_runs(self):
        data = update_runs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_data'] = self.get_last_runs
        return context

