from .permisson import IsStaffEditorPrmission
from rest_framework.permissions import IsAdminUser
class StaffEditorPermissionMixin():
    permission_classes=[IsAdminUser,IsStaffEditorPrmission]