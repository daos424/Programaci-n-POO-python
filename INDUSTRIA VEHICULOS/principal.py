from auto import Auto
from auto_clasico import AutoClasico
from auto_familiar import AutoFamiliar
from auto_hibrido import AutoHibrido

obj_auto_clasico = AutoClasico("Coupe antiguo", "rojo", "2.0", 2, 4)
obj_auto_familiar = AutoFamiliar("Familiar", "gris", "2.0", 5, 7)
obj_auto_hibrido = AutoHibrido("Hibrido urbano", "blanco", "hibrido", 4, 5)

print(obj_auto_clasico.arrancar())
print(obj_auto_clasico.acelerar_y_frenar("acelerar", 80))
print(obj_auto_clasico.acelerar_y_frenar("frenar", 30))
print(obj_auto_clasico.apagar())
print(obj_auto_clasico.sistema_direccion("asistida"))
print(obj_auto_clasico.climatizacion("encendida"))
print(obj_auto_clasico.tipo_seguridad())
print(obj_auto_clasico.luces("encendidas"))
print(obj_auto_clasico.sistema_ventanas("abiertas"))
print(obj_auto_clasico.sistema_espejo("ajustados"))

print(obj_auto_familiar.arrancar())
print(obj_auto_familiar.sistema_ventanas("cerradas"))
print(obj_auto_familiar.tipo_seguridad())

print(obj_auto_hibrido.arrancar())
print(obj_auto_hibrido.sistema_espejo("ajustados"))
print(obj_auto_hibrido.climatizacion("encendida"))
