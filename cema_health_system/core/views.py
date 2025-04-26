from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Program
from .serializers import ClientSerializer, ClientCreateSerializer, ProgramSerializer
from rest_framework.permissions import IsAuthenticated

# Viewset for managing Program entities
class ProgramViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing the Program model.
    Allows authenticated users to perform CRUD operations on Programs.
    """
    
    queryset = Program.objects.all()  # Queryset to fetch all Program objects
    serializer_class = ProgramSerializer  # Serializer used to convert Program objects to and from JSON
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset


# Viewset for managing Client entities
class ClientViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing the Client model.
    Allows authenticated users to perform CRUD operations on Clients.
    It also includes actions for enrolling a client in programs and searching for clients by name.
    """

    queryset = Client.objects.all()  # Queryset to fetch all Client objects
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this viewset
    
    def get_serializer_class(self):
        """
        Returns the appropriate serializer class based on the action.
        Uses ClientCreateSerializer for create, update, and partial_update actions,
        and ClientSerializer for other actions (like retrieve or list).
        """
        if self.action in ['create', 'update', 'partial_update']:
            return ClientCreateSerializer  # Use the serializer for client creation or update
        return ClientSerializer  # Default to using the serializer for retrieving client data
    
    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None):
        """
        Enroll a client in one or more programs.
        Accepts a list of program IDs and associates them with the client.

        Args:
            request (Request): The HTTP request containing program_ids to enroll the client.
            pk (int): The primary key (ID) of the client.

        Returns:
            Response: A message confirming the enrollment of the client.
        """
        client = self.get_object()  # Fetch the client object based on the provided ID
        program_ids = request.data.get("program_ids", [])  # Retrieve program IDs from the request
        programs = Program.objects.filter(id__in=program_ids)  # Find the programs by their IDs
        client.programs.add(*programs)  # Add the programs to the client's 'programs' relationship
        return Response({"message": "Client enrolled successfully."})  # Return success message

    @action(detail=False, methods=['get'])
    def search(self, request):
        """
        Search for clients by name.
        Filters clients whose name contains the search query.

        Args:
            request (Request): The HTTP request containing the search query as a query parameter.
        
        Returns:
            Response: A list of clients that match the search query.
        """
        name = request.query_params.get('name', '')  # Get the search query from request parameters
        clients = Client.objects.filter(name__icontains=name)  # Find clients whose name contains the query
        serializer = self.get_serializer(clients, many=True)  # Serialize the list of matching clients
        return Response(serializer.data)  # Return the serialized data in the response
