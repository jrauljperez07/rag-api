"""URLs for RAG Add API handler"""
from django.urls import path
from rag_add.api.views import RAGAddView

urlpatterns = [
    path('rag-add/', RAGAddView.as_view(), name='rag'),
]