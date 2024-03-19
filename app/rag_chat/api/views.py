from rest_framework import status, generics
from rest_framework.response import Response
import logging
from utilities.rag_handler import RAGHandler
from utilities.config import MODEL_RAG


class RAGChatView(generics.GenericAPIView):
    """RAG Chat API view."""
    def post(self, request, *args, **kwargs):
        """Function to handle POST requests."""
        try:
            question = 'Dime si tengo alguna cita medica'
            rag_handler = RAGHandler(MODEL_RAG)
            response = rag_handler.get_rag_response(question)
            
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logging.exception("Unexpected error occurred when checking unseen emails.")
            return Response({"detail": " An unexpected error occurred, " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)