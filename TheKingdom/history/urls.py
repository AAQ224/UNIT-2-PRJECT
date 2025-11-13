from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("era/first/",  views.first_state_view,  name="era_first"),
    path("era/second/", views.second_state_view, name="era_second"),
    path("era/third/",  views.third_state_view,  name="era_third"),

   path("ruler/king-abdulaziz/", views.ruler_abdulaziz, name="ruler_abdulaziz"),
    path("ruler/king-saud/", views.ruler_saud, name="ruler_saud"),
    path("ruler/king-faisal/", views.ruler_faisal, name="ruler_faisal"),
    path("ruler/king-khalid/", views.ruler_khalid, name="ruler_khalid"),
    path("ruler/king-fahd/", views.ruler_fahd, name="ruler_fahd"),
    path("ruler/king-abdullah/", views.ruler_abdullah, name="ruler_abdullah"),
    path("ruler/king-salman/", views.ruler_salman, name="ruler_salman"),
    path("ruler/muhammad-bin-saud/", views.ruler_muhammad_bin_saud, name="ruler_muhammad_bin_saud"),
    path("ruler/abdulaziz-bin-muhammad/", views.ruler_abdulaziz_bin_muhammad, name="ruler_abdulaziz_bin_muhammad"),
    path("ruler/saud-bin-abdulaziz/", views.ruler_saud_bin_abdulaziz, name="ruler_saud_bin_abdulaziz"),
    path("ruler/abdullah-bin-saud/", views.ruler_abdullah_bin_saud, name="ruler_abdullah_bin_saud"),
    path("ruler/turki-bin-abdullah/", views.ruler_turki_bin_abdullah, name="ruler_turki_bin_abdullah"),
    path("ruler/faisal-bin-turki/", views.ruler_faisal_bin_turki, name="ruler_faisal_bin_turki"),
    path("ruler/abdullah-bin-faisal/", views.ruler_abdullah_bin_faisal, name="ruler_abdullah_bin_faisal"),
    path("ruler/saud-bin-faisal/", views.ruler_saud_bin_faisal, name="ruler_saud_bin_faisal"),
    path("ruler/abdulrahman-bin-faisal/", views.ruler_abdulrahman_bin_faisal, name="ruler_abdulrahman_bin_faisal"),
]
