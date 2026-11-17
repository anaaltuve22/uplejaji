from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Productor,
    SemanaLiquidacion,
    RecepcionLeche,
    Insumo,
    VentaInsumo,
    PlanSanitario,
)

admin.site.register(Productor)
admin.site.register(SemanaLiquidacion)
admin.site.register(RecepcionLeche)
admin.site.register(Insumo)
admin.site.register(VentaInsumo)
admin.site.register(PlanSanitario)
