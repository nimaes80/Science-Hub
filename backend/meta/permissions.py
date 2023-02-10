from rest_framework.permissions import SAFE_METHODS, BasePermission




class IsSuperUserOr404Forbidden(BasePermission):

	def has_permission(self, request, view): # GET / POST (LIST / CREATE)
		return bool(request.user and request.user.is_superuser)
	
	def has_object_permission(self, request, view, obj): # GET / PATCH / PUT / DELETE (RETRIEVE / UPDATE / PARTIAL UPDATE / DELETE)
		return bool(request.user and request.user.is_superuser)


class IsSuperUserOrReadOnly(BasePermission):

	def has_permission(self, request, view): # GET / POST (LIST / CREATE)
		return bool(request.user and request.user.is_superuser or request.method in SAFE_METHODS)
	
	def has_object_permission(self, request, view, obj): # GET / PATCH / PUT / DELETE (RETRIEVE / UPDATE / PARTIAL UPDATE / DELETE)
		return bool(request.user and request.user.is_superuser or request.method in SAFE_METHODS)


class IsSafeOr404Forbidden(BasePermission):

	def has_permission(self, request, view): # GET / POST (LIST / CREATE)
		return bool(request.method in SAFE_METHODS)
	
	def has_object_permission(self, request, view, obj): # GET / PATCH / PUT / DELETE (RETRIEVE / UPDATE / PARTIAL UPDATE / DELETE)
		return bool(request.method in SAFE_METHODS)
