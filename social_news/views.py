from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse

from . import models

def all(request):
    entries = models.Entry.objects.all()
    scores = map(lambda e: e.compute_score(), entries)
    sorted_entries = [e for s,e in sorted(zip(scores, entries), reverse=True)]
    if request.user.is_authenticated():
        sorted_voted = map(lambda e: voted(e, request.user), sorted_entries)
    else:
        #if anonymous user, count them as having voted
        #so the vote button won't be displayed
        sorted_voted = [True for e in entries]
    return render(request, 'social_news/all.html', 
                  {"entries" : zip(sorted_entries, sorted_voted)})

def voted(entry, user):
    return models.Vote.objects.filter(entry = entry, voter = user).count() > 0

def vote(request):
    num_votes = 0
    if request.method == 'POST':
        pk = request.POST["entry_pk"]
        entry = models.Entry.objects.get(pk = pk)
        if not voted(entry, request.user):
            vote = models.Vote(entry = entry,
                               voter = request.user)
            vote.save()
        num_votes = entry.num_votes
    return HttpResponse(num_votes)

class EntryCreateView(CreateView):
    model = models.Entry
    fields = ['title', 'link']

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.author = self.request.user
        entry.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse("all")

    


