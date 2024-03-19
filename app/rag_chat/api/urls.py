"""URLs for RAG Add API handler"""
from django.urls import path
from rag_chat.api.views import RAGChatView

urlpatterns = [
    path('rag-chat/', RAGChatView.as_view(), name='rag'),
]