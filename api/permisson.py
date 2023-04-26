from rest_framework import permissions


class IsStaffEditorPermisson(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff:
            user=request.user
            print('--------',user.has_perm('api.view_product'))
            if user.has_perm('api.view_product'):
                return True          
            return False
        return False