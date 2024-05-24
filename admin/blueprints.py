from .views import view as admin_view
from .apis.member import api as member_api
from .apis.trip import api as trip_api

blueprints = [
  member_api,
  trip_api,
  admin_view,
]