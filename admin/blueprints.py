from .views import view as admin_view
from .apis.member import api as member_api

blueprints = [
  member_api,
  admin_view,
]