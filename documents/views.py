from django.shortcuts import render, redirect, get_object_or_404
from .models import Document, Download
from django.contrib.auth.decorators import login_required
from django.db.models import Count # pour compter les doc par rubrique
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import FileResponse


@login_required
def cours(request):
    cours = Document.objects.filter(
        doc_type='course',
).distinct()

    return render(request, 'documents/cours.html', {'documents': cours})

@login_required
def devoir(request):
    devoirs = Document.objects.filter(
        doc_type='assignment',
    ).distinct()
    return render(request, 'documents/devoir.html', {'documents': devoirs})

@login_required
def examen(request):
    examen = Document.objects.filter(
        doc_type='exam',
    ).distinct()
    return render(request, 'documents/examen.html', {'documents': examen})


 
# vue pour les cours , devoir, examen lies au dashboard de l'etudiant 
@login_required
def student_cours(request):
    downloads = Download.objects.filter(user=request.user,document__doc_type="course").select_related('document')

    documents = []
    for d in downloads:
        doc = d.document
        doc.download_count = Download.objects.filter(document=doc).count()
        documents.append(doc)

    return render(request, "dashboard/student_cours.html", {"documents": documents})


@login_required
def student_devoirs(request):

    downloads = Download.objects.filter(user=request.user,document__doc_type="assignment").select_related('document')

    documents = []
    for d in downloads:
        doc = d.document
        doc.download_count = Download.objects.filter(document=doc).count()
        documents.append(doc)

    return render(request, "dashboard/student_devoirs.html", {"documents": documents})
 

@login_required
def student_examens(request):
    downloads = Download.objects.filter(user=request.user,document__doc_type="exam").select_related('document')

    documents = []
    for d in downloads:
        doc = d.document
        doc.download_count = Download.objects.filter(document=doc).count()
        documents.append(doc)

    return render(request, "dashboard/student_examens.html", {"documents": documents})
 

@login_required
def delete_document(request, pk):
    doc = get_object_or_404(Document, pk=pk, uploaded_by=request.user)
    doc.delete()
    return redirect(request.META.get('HTTP_REFERER', 'student_cours'))




# fonction pour afficher le nombre de doc en fonction de rubrique cours , devoirs, examen 
# remplace 'login' par le nom exact de ta route de connexion si différent

@login_required(login_url='login')  
def download_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)

    # Enregistrer le téléchargement si l'utlisateur est connecté dans le cas contraire il est renvoyé a la page de connexion avec @login_required
    if request.user.is_authenticated:
        Download.objects.get_or_create(user=request.user, document=document)
    
    return FileResponse(document.file.open(), as_attachment=True, filename=document.file.name)
"""
    cette fonction permet de gerer la pagination au cas ou la liste est trop longue on pourra avoir une autre
"""
@login_required
def document_etudiant(request):
    docs_list = Document.objects.filter(uploaded_by = request.user)
    paginator = Paginator(docs_list, 8) # 8 doc par page


    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'documents/dashboard_etudiant.html', {'documents': page_obj})


