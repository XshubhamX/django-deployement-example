from django.conf.urls import url,include
from t_a import views
app_name="t_a"
urlpatterns=[
url(r'^main/',views.main,name="main"),
url(r'^other/',views.other,name="other")
]
