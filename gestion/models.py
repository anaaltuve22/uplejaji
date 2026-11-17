from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Productor(models.Model):
  nombre = models.CharField(max_length=100)
  telefono = models.CharField(max_length=20, blank=True, null=True)
  direccion = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.nombre


class SemanaLiquidacion(models.Model):
  """Permite gestionar las semanas flexibles (ej. de miércoles a martes, 6 a 8 días)"""

  numero_semana = models.CharField(
      max_length=50, help_text="Ej. Semana 42 (Mié 15 - Mar 21)"
  )
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField()
  activa = models.BooleanField(default=True)

  def __str__(self):
    return (
        f"{self.numero_semana} ({self.fecha_inicio} al {self.fecha_fin})"
    )


class RecepcionLeche(models.Model):
  """Módulo de Davey: Registro de litros de leche por productor y semana"""

  productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
  semana = models.ForeignKey(SemanaLiquidacion, on_delete=models.CASCADE)
  litros = models.DecimalField(max_digits=10, decimal_places=2)
  calidad_observacion = models.TextField(blank=True, null=True)
  fecha_registro = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"{self.productor.nombre} - {self.litros} L ({self.semana})"


class Insumo(models.Model):
  """Módulo de Carolina: Alimentos e insumos disponibles en inventario"""

  nombre = models.CharField(max_length=100)
  precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
  stock_piso = models.DecimalField(
      max_digits=10, decimal_places=2, help_text="Cantidad actual en piso"
  )

  def __str__(self):
    return f"{self.nombre} (Stock: {self.stock_piso})"


class VentaInsumo(models.Model):
  """Registro de ventas de insumos a los productores por semana"""

  productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
  insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
  cantidad = models.DecimalField(max_digits=10, decimal_places=2)
  precio_total = models.DecimalField(max_digits=10, decimal_places=2)
  semana = models.ForeignKey(SemanaLiquidacion, on_delete=models.CASCADE)
  fecha = models.DateField(auto_now_add=True)

  def __str__(self):
    return f"Venta: {self.insumo.nombre} a {self.productor.nombre}"


class PlanSanitario(models.Model):
  """Gestión independiente para campañas sanitarias (2-3 veces al año)"""

  nombre_campana = models.CharField(
      max_length=150, help_text="Ej. Campaña de Vacunación"
  )
  productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
  costo = models.DecimalField(max_digits=10, decimal_places=2)
  fecha = models.DateField()
  observaciones = models.TextField(blank=True, null=True)

  def __str__(self):
    return f"{self.nombre_campana} - {self.productor.nombre}"
