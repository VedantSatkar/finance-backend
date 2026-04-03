from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta

from .models import FinancialRecord
from .serializers import RecordSerializer
from .permissions import IsAdmin


class RecordViewSet(viewsets.ModelViewSet):
    queryset = FinancialRecord.objects.all()
    serializer_class = RecordSerializer

    # ✅ FIXED PERMISSIONS
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            return [IsAdmin()]  # only admin can modify
        return [IsAuthenticated()]  # others must be logged in

    # ✅ FILTERING
    def get_queryset(self):
        queryset = FinancialRecord.objects.all()

        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')
        start_date = self.request.query_params.get('start')
        end_date = self.request.query_params.get('end')

        if type:
            queryset = queryset.filter(type=type)
        if category:
            queryset = queryset.filter(category=category)
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        return queryset


# ✅ DASHBOARD API
@api_view(['GET'])
def dashboard_summary(request):
    records = FinancialRecord.objects.all()

    total_income = records.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
    total_expense = records.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

    # category-wise totals
    category_data = records.values('category').annotate(total=Sum('amount'))

    # recent transactions
    recent = records.order_by('-date')[:5]

    # monthly trends (last 30 days)
    last_30_days = now().date() - timedelta(days=30)
    monthly = records.filter(date__gte=last_30_days).values('date').annotate(total=Sum('amount'))

    return Response({
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense,
        "category_breakdown": category_data,
        "recent_transactions": RecordSerializer(recent, many=True).data,
        "monthly_trends": monthly
    })