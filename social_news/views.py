from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from . import models

def all(request):
    entries = models.Entry.objects.order_by('-post_date')
    return render(request, 'social_news/all.html', {"entries" : entries})

def vote(request):
    if request.method == 'POST':
        pk = request.POST["entry_pk"]
        entry = models.Entry.objects.get(pk=pk)
        entry.vote_count += 1
        entry.save()
    return redirect("all")

class EntryCreateView(CreateView):
    model = models.Entry
    def get_success_url(self):
        return reverse("all")
    fields = ['title', 'link']
