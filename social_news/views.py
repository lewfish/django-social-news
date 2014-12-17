from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from . import models

def all(request):
    entries = sorted(models.Entry.objects.all(), key = lambda e: e.num_votes, reverse = True)
    return render(request, 'social_news/all.html', {"entries" : entries})

def vote(request):
    if request.method == 'POST':
        pk = request.POST["entry_pk"]
        entry = models.Entry.objects.get(pk=pk)
        #if user hasn't voted on the entry yet
        if models.Vote.objects.filter(entry=entry, voter= request.user).count() == 0:
            vote = models.Vote(entry = entry,
                               voter = request.user)
            vote.save()
    return redirect("all")

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

    


