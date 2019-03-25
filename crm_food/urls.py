from django.urls import path
from .views import (
            index,
            TablesListView,
            DepartmentsListView,
            StatusesListView,
            ServicePercentageListView,
        )


urlpatterns = [
    path('',index,name="index"),
    path('tables/',TablesListView.as_view(),name="tables"),
    path('tables/<int:id>/',TablesListView.as_view(),name="tables_id"),
    path('departments/',DepartmentsListView.as_view(),name="departments"),
    path('statuses/',StatusesListView.as_view(),name="statuses"),
    path('servicePercentage/',ServicePercentageListView.as_view(),name="servicepercentages"),
]
