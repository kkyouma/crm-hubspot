import pandas as pd
import faker import Faker

faker = Faker('es_CL')

def generar_cliente():
  nombre = fake.name()
  correo = fake.email()
  telefono = fake_phone_number()
  direccion = fake.address()

  return {"Nombre": nombre, "Correo": correo, "Telefono": telefono, "Direccion": direccion}

num_clientes = 100 #Cantidad de iteraciones (filas) que se agregaran
clientes = [generar_cliente() for _ in range (num_clientes)]

df = pd.DataFrame(clientes)

df.to_csv("datos_clientes")