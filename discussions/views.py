from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required

# Afficher la liste des discussions
@login_required
def discussion_list(request):
    discussions = Comment.objects.all()
    return render(request, 'discussions/discussion_list.html', {'discussions': discussions})

# Créer une nouvelle discussion
@login_required
def create_discussion(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        new_discussion = Comment(title=title, content=content, user=request.user)
        new_discussion.save()
        return redirect('discussion_list')
    
    return render(request, 'discussions/create_discussion.html')

# Afficher une discussion spécifique
@login_required
def view_discussion(request, id):
    discussion = Comment.objects.get(id=id)
    return render(request, 'discussions/view_discussion.html', {'discussion': discussion})
