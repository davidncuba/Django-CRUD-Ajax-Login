from apps.transactions.models import Transactions
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from apps.accounts.decorators import admin_only

@login_required
def index(request):
  if request.user.is_superuser:
    return render(request, 'dashboard/index.html')
  else:
     return render(request, 'dashboard/not_admin.html')

@login_required
@admin_only
def dateFilter(request):
  start = request.GET.get('start', '')
  end = request.GET.get('end', '')
  transactions = Transactions.objects.all().filter(Q(date_depature__gte= start) | Q(date_delivered__lte=end))
  count = Transactions.objects.all().filter(Q(date_depature__gte= start) | Q(date_delivered__lte=end)).count()
  return render(request, 'dashboard/date_filter.html', {'transactions': transactions, 'count': count})
