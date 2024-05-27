from rest_framework import viewsets
from intergration_app.models import Payment, Plan, UserIntergrationApp
from intergration_app.serializers import GetIntegrationAppSerializer, IntegrationAppSerializer 
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from datetime import timedelta
  

# Create your views here.

class UserIntergrationAppView(viewsets.ModelViewSet):
    queryset = UserIntergrationApp.objects.all()
    serializer_class = IntegrationAppSerializer 

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset().filter(user=request.user))
        serializer = GetIntegrationAppSerializer(queryset, many=True)
        return Response(
            {
                'status': True,
                'message': 'User intergration app list',
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )   
    
    def create(self, request):
        plan = Plan.objects.get(name='FREE' )

        try:
            payment = Payment.objects.get(user=request.user, plan=plan) 
        except Payment.DoesNotExist:
            payment = None  
        
        if payment is None:
            payment = Payment.objects.create(
                user=request.user,
                plan=plan,
                amount=plan.price,
                currency='TZS',
                expire_date=timezone.now() + timedelta(days=30)
            ) 
            data = {
                'name': request.data.get('name'),
                'description': request.data.get('description'),
                "user": request.user.user_uid,
                "payment": payment.id
            }

    
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response(
                {
                    'status': True,
                    'message': 'User intergration app created successfully',
                    'data': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        else:
           return Response(
            {
                'status': False,
                'message': 'Upgrade your plan  for more features',
            },
            status=status.HTTP_400_BAD_REQUEST)
           
           
       