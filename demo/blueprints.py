from .views.demo import view as demo_view
from .apis.demo import api as demo_api

blueprints = [
  demo_view,
  demo_api,
]