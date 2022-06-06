from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect


class AdminAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseNotAllowed('شما اجازه دسترسی به این صفحه را ندارید !')

