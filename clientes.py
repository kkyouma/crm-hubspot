import pandas as pd
from faker import Faker

fake = Faker('es_CL')

def generar_cliente():
  nombre = fake.name()
  correo = fake.email()
  telefono = fake.phone_number()
  direccion = fake.address()
  ciudad = fake.city()

  return {"Nombre": nombre, "Correo": correo, "Telefono": telefono, "Ciudad": ciudad,"Direccion": direccion}

num_clientes = 100 #Cantidad de iteraciones (filas) de datos
clientes = [generar_cliente() for _ in range (num_clientes)]

df = pd.DataFrame(clientes)

df.to_csv("datos_clientes")