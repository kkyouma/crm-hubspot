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

def generar_empresa():
    nombre_empresa = fake.company()
    correo_empresa = fake.email()
    telefono_empresa = fake.phone_number()
    ciudad_empresa = fake.city()

    return {"Nombre": nombre_empresa, "Correo": correo_empresa, "Telefono": telefono_empresa, "Ciudad": ciudad_empresa}

num_clientes = 20 #Cantidad de iteraciones (filas) de datos
num_empresas = 20 #Cantidad de iteraciones (filas) de datos

clientes = [generar_cliente() for _ in range (num_clientes)]
empresas = [generar_empresa() for _ in range (num_empresas)]

df = pd.DataFrame(clientes)
df = pd.DataFrame(empresas)

df.to_csv("datos_clientes", index=False) 
df.to_csv("datos_empresas", index=False) 
