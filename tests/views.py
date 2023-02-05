from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.core import serializers
import json
import datetime
from datetime import datetime
from integrations.models import TestRunResults
from tests.forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ListIndex(ListView):
    template_name = 'tests/index.html'
    model = TestCase

    def get_context_data(self, **kwargs):
        context = super(ListIndex, self).get_context_data(**kwargs)
        context.update({
            'history_list_case': History.objects.all().order_by('create_date')[:5]
        })
        return context



# done
class ListAllScenario(ListView):
    template_name = 'tests/all_scenario.html'
    model = TestCase
    context_object_name = 'tests_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ListAllScenario, self).get_context_data(**kwargs)
        context.update({
            'feat_list': FeatureTest.objects.all()  # filter(id=self.kwargs.get('pk')),
        })
        return context

    def get_features(self, **kwargs):
        pass


class TestsFeature(ListView):
    model = TestCase
    template_name = 'tests/feature_scenario.html'
    context_object_name = 'tests'
    paginate_by = 10

    def get_queryset(self):
        return TestCase.objects.filter(feature__slug=self.kwargs['feature_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'feat': FeatureTest.objects.filter(slug=self.kwargs['feature_slug']),
        })
        return context


# done
class DetailScenario(DetailView):
    template_name = 'tests/scenario.html'
    model = TestCase

    def last_results(self, **kwargs):
        context = TestCase.objects.filter(id=self.kwargs['pk'])[0]
        scenario = context.name

        data_model = TestRunResults.objects.all().order_by('-created')[:5]
        serialized_data = serializers.serialize('json', data_model, fields='body_test')
        data = json.loads(serialized_data)

        for d in data:
            last_result = []
            list_result = d["fields"]["body_test"]
            for i in list_result:
                name = json.loads(i)['name']
                if scenario == name:
                    status_date = []
                    status = json.loads(i)['status']
                    date = datetime.utcfromtimestamp(json.loads(i)['stop'] / 1000).strftime('%Y-%m-%d %H:%M')
                    status_date.append(status)
                    status_date.append(date)
                    last_result.append(status_date)
                    print(last_result)
                    return last_result
        return last_result


    def get_context_data(self, **kwargs):
        context = super(DetailScenario, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(scenario_public=self.object)
        context.update({
            'last_results_obj': self.last_results
        })
        return context

    def add_comment_scenario(self, request, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST or None)
        scenario = TestCase.objects.filter(id=self.kwargs['pk'])[0]

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.scenario_public = scenario
            comment.save()
            return redirect('tests:get_scenario', scenario.id)
        return render(request, 'scenario.html', context={'form': form, 'is_edit': True})


class CreateScenario(CreateView):
    model = TestCase
    form_class = AddScenarioForm
    template_name = 'tests/add_form_forscreeen.html'
    success_url = 'tests/index.html'


class CreateFeature(CreateView):
    model = FeatureTest
    form_class = AddFeatureForm
    template_name = 'tests/add_feature.html'
    success_url = 'tests/index.html'


class UpdateScenario(UpdateView):
    model = TestCase
    form_class = AddScenarioForm
    template_name = 'tests/update_scenario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update
        return context

    def get_success_url(self):
        messages.success(self.request, 'Your post has been updated successfully.')
        return reverse_lazy('tests:get_scenario', kwargs={'pk': self.kwargs.get('pk')})

    def update_event(self):
        text = f'Пользователь {self.last_update_user} внес изменения в сценарий: {self.name}.'
        poll = History.objects.create(text=text, create_date=datetime.now())
        return poll



class DeleteScenario(DeleteView):
    model = TestCase
    success_url = reverse_lazy('tests:index')
