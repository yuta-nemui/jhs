from django.urls import path
from jhs import views
from . import views

app_name = 'jhs'
urlpatterns = [
    # 会社
    path('company/', views.company_list, name='company_list'),   # 一覧
    path('company/add/', views.company_edit, name='company_add'),  # 登録
    path('company/mod/<int:company_id>/',
         views.company_edit, name='company_mod'),  # 修正
    path('company/del/<int:company_id>/',
         views.company_del, name='company_del'),   # 削除
]
