from django.http import HttpResponse
from django.shortcuts import redirect, render

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		
		if request.user.is_superuser:
			return view_func(request, *args, **kwargs)
		else:
			return render(request, "dashboard/not_admin.html")
	
	return wrapper_function