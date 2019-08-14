from dataclasses import dataclass


@dataclass
class AdminInfo:
    app_label: str
    model_name: str
    obj_id: str

    def admin_change_url(self) -> str:
        return f"/admin/{ self.app_label.lower() }/{ self.model_name.lower() }/{self.obj_id}/change/"

    def admin_history_url(self):
        return f"/admin/{ self.app_label.lower() }/{ self.model_name.lower() }/{self.obj_id}/history/"


class AdminableObject:
    def get_admin_info(self) -> AdminInfo:
        return AdminInfo(self._meta.app_label, self._meta.object_name, self.id)

    def is_adminable(self) -> bool:
        return True

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse(self.url_base, args=[str(self.id)])
