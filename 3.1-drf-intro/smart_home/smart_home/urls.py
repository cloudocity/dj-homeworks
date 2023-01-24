"""smart_home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from measurement.views import SensorView, MeasurementView, SensorUpdate, SensorMeasurementView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sensor', SensorView.as_view()), #Get получить список датчиков и POST добавить новый
    path('api/sensor/<pk>', SensorUpdate.as_view()), #Put изменить данные датчика
    path('api/measurement', MeasurementView.as_view()),# Get Получить все  измерения и Post  Добавить измерение. Указываются ID датчика и температура.
    path('api/sensormeas/<pk>', SensorMeasurementView.as_view()),# Get Получить информацию по конкретному датчику

]
