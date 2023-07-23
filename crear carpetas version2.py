from os import mkdir


ruta = input("Ruta de donde se crarán las carpetas: ")


desde = int(input("Desde cuál número de radicado crear carpetas: "))
hasta = int(input("hasta cual número de radicado crear carpetas: "))

for i in  range(desde, hasta + 1):

    mkdir(f"{ruta}\\0{i}")

##    mkdir(f"{ruta}\\01-2023-UT4G-4502015-311-{i}")
