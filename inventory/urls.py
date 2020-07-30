from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path("", views.item_list, name="item_list"),
    # path("amount/", views.amount_ajax, name="amount_ajax"),
    path("<int:pk>/", views.item_read, name="item_read"),
    path("create/", views.item_create, name="item_create"),
    path("update/<int:pk>/", views.item_update, name="item_update"),
    path("delete/<int:pk>/", views.item_delete, name="item_delete"),

path("account/", views.account_list, name="account_list"),
    path("account/<int:pk>/", views.account_read, name="account_read"),
    path("account/create/", views.account_create, name="account_create"),
    path("account/update/<int:pk>/", views.account_update, name="account_update"),
    path("account/delete/<int:pk>/", views.account_delete, name="account_delete"),
]