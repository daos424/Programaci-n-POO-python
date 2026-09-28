from animal import Animal
from gato import Gato
from delfin import Delfin
from mariposa import Mariposa

from loro import Loro
from oso import Oso
obj_gato = Gato("Gato", 3, "pequeno", "gris")
obj_delfin = Delfin("Delfin", 7, "grande", "gris claro")
obj_mariposa = Mariposa("Mariposa", 1, "pequena", "amarillo")
obj_loro = Loro("Loro", 4, "mediano", "verde")
obj_oso = Oso("Oso", 8, "grande", "cafe")

print(obj_gato.moverse())
print(obj_gato.comunicacion())
print(obj_gato.reproduccion())
print(obj_gato.alimentarse())
print(obj_gato.adaptacion())
print(obj_gato.instintos())
print(obj_gato.descanso())
print(obj_gato.sueno())
print(obj_gato.interaccion_social())

print(obj_delfin.moverse())
print(obj_delfin.adaptacion())

print(obj_mariposa.moverse())
print(obj_mariposa.instintos())

print(obj_loro.moverse())
print(obj_loro.comunicacion())

print(obj_oso.moverse())
print(obj_oso.instintos())
