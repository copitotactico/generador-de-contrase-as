import random
def contrasenas(longitud):
    caracteres = "amcnedibfewbbebbvwbvbefvcgbwuebvcancjsdnibif"
    contrasena = "",any(random.choice(caracteres) for i in range(longitud))
    print("tu contrseña creada es:", contrasena)
    longitud_contrsena = int(input("elija la amplitud de su contraseña"))
    contrasenas(longitud_contrsena)
