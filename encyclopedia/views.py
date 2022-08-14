from django.shortcuts import render, redirect
from markdown2 import Markdown
from random import choice

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def show(request, title):
    entry = util.get_entry(title)
    if entry is None:
        return render(request, "encyclopedia/error.html", {
            "error": "Not Found",
            "message": f"There are no wiki entries with this title: {title}"
        })

    md = Markdown()
    entry = md.convert(entry)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": entry
    })


def search(request):
    q = request.GET['q']
    entries = util.list_entries()
    search_result = []

    for entry in entries:
        if q.lower() == entry.lower():
            return redirect('show', title=entry)

        if q.lower() in entry.lower():
            search_result.append(entry)

    return render(request, "encyclopedia/search_results.html", {
        "entries": search_result
    })


def new(request):
    return render(request, "encyclopedia/entry_form.html", {
        "create": True,
    })


def store(request):
    title = request.POST['title']
    content = request.POST['content']

    entry = util.get_entry(title)
    if entry is not None:
        return render(request, "encyclopedia/error.html", {
            "error": f"Entry Title Collision",
            "message": f"There is already an entry titled: {title}"
        })

    util.save_entry(title, content)

    return redirect("show", title=title)


def edit(request, title):
    content = util.get_entry(title)


    return render(request, "encyclopedia/entry_form.html", {
        "title": title,
        "content": content,
        "create": False
    })


def save_edit(request):
    title = request.POST['title']
    content = request.POST['content']

    util.save_entry(title, content)
    return redirect('show', title=title)


def random_entry(request):
    entries = util.list_entries()
    entry = choice(entries)
    return redirect('show', title=entry)
