import pandas as pd
from faker import Faker

fake = Faker('es_CL')

def generar_cliente():
  nombre = fake.name()
  correo = fake.email()
  telefono = fake.phone_number()
  company = fake.company()
  ciudad = fake.city()

  return {"Nombre": nombre, "Correo": correo, "Telefono": telefono,"Nombre de la empresa": company}

num_clientes = 20 #Cantidad de iteraciones (filas) de datos
clientes = [generar_cliente() for _ in range (num_clientes)]

df = pd.DataFrame(clientes)

df.to_csv("datos_clientes") 