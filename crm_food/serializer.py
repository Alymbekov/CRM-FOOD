from rest_framework import serializers

from crm_food.models import (
                        Table,
                        Department,
                        Status,
                        ServicePercentage,
                    )

class TableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = (
            'id',
            'name_of_tables',
        )


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = (
            'id',
            'name_of_departments',
        )

class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = (
            'id',
            'name_of_statuses',
        )


class ServicePercentageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServicePercentage
        fields = (
            'name',
        )