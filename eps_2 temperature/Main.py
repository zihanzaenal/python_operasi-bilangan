# latihan konversi satuan temperature

print("\n_____PROGRAM KONEVERSI TEMPERATURE CELCIUS TO____\n")

# Celcius
celcius = float(input('Masukan suhu dalam celcius : '))

# Reamur 
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur,"Reamur")

# Farenheit
fahreinheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahreinheit,"fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin,"Kelvin")


print("\n_____PROGRAM KONEVERSI TEMPERATURE REAMUR TO____\n")

reamur = float(input('Masukan suhu dalam raemur : '))

# Celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah",celcius,"Celcius" )

# fahreinheit
fahreinheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah",fahreinheit,"fahrenheit")

# Kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah", kelvin,"Kelvin")

print("\n_____PROGRAM KONEVERSI TEMPERATURE FAHREINHEIT TO____\n")

fahreinheit = float(input('Masukan suhu dalam fahreinheit : '))

# Celcius
celcius = (5/9 * (fahreinheit-32))
print("suhu dalam celcius adalah",celcius,"Celcius" )

# Reamur 
reamur = (4/9 * (fahreinheit -32))
print("suhu dalam reamur adalah", reamur,"Reamur")

# Kelvin
kelvin = 5/9 * (fahreinheit - 32) + 273
print("suhu dalam kelvin adalah", kelvin,"Kelvin")

print("\n_____PROGRAM KONEVERSI TEMPERATURE KELVIN TO____\n")

kelvin = float(input('Masukan suhu dalam kelvin : '))

# Celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius,"Celcius" )

# Reamur 
reamur = (4/5 * (kelvin -273))
print("suhu dalam reamur adalah", reamur,"Reamur")

# fahreinheit
fahreinheit = 9/5 * (kelvin -273) + 32
print("suhu dalam fahrenheit adalah",fahreinheit,"fahrenheit")
