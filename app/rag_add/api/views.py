from rest_framework import status, generics
from rest_framework.response import Response
import logging
from utilities.rag_handler import RAGHandler
from utilities.config import MODEL_RAG

class RAGAddView(generics.GenericAPIView):
    """Handle POST Adds a new source to the Embedchain app."""
    
    def post(self, request,*args, **kwargs):
        try:
            rag_handler = RAGHandler(MODEL_RAG)
            source = rag_handler.add_source()
            return Response(source, status=status.HTTP_200_OK)   
        except Exception as e:            
            logging.exception("Unexpected error occurred when adding RAG resources.")
            return Response({"detail": " An unexpected error occurred, " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 