from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse

from django.core.urlresolvers import reverse
from django.views import generic
from .models import Choice, Question, Register
from quiz.forms import SignUpForm



class IndexView(generic.ListView):
    template_name = 'quiz/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-test_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'quiz/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'quiz/results.html'


def answer(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'quiz/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice.choice_text  == selected_choice.answer:
           selected_choice.result = True
        else:
            selected_choice.result = False
        selected_choice.save()
        return HttpResponseRedirect(reverse('quiz:results', args=(p.id,)))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('task:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/singup.html', {'form': form})