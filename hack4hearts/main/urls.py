from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('', views.doctor, name='doctor'),
    path('patient/<int:transcript_id>/', views.patient, name='patient'),
    path('patient_cards/<int:transcript_id>/', views.patient_card, name='patient_cards'),
    path('get_query_answer/', views.get_query_answer, name='get_query_answer'),
]
