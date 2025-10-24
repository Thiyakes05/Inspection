from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
     path('login/',views.login,name="login"),
     path('login/home/',views.home,name="home"),
     path('login/home/terms',views.terms,name="terms"),
      path('login/home/terms/procedure',views.procedure,name="procedure"),
      path('login/home/terms/procedure/inspection',views.inspection,name="inspection"),
       path('login/home/terms/procedure/inspection/washroom_inspection',views.washroom_inspection,name="washroom_inspection"),
        path('login/home/terms/procedure/inspection/infrastructure_inspection',views.infrastructure_inspection,name="infrastructure_inspection"),
         path('login/home/terms/procedure/inspection/faculty_credentials',views.faculty_credentials,name="faculty_credentials"),
         path('login/home/terms/procedure/inspection/classroom_inspection',views.classroom_inspection,name="classroom_inspection"),
         path('login/home/terms/procedure/inspection/certificate_verification',views.certificate_verification,name="certificate_verification"),
         path('login/home/terms/procedure/inspection/safety_measure',views.safety_measure,name="safety_measure"),
          path('login/home/terms/procedure/inspection/inspection_end',views.inspection_end,name="inspection_end"),
]





























































































