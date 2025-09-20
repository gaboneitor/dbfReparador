# dbfReparador
# 🗃️ DBF Data Copier

Este script en Python está diseñado para **copiar los datos de un archivo `.DBF` a otro archivo `.DBF` con la misma estructura**. Es especialmente útil cuando deseas recuperar datos desde un archivo `.DBF` corrupto **siempre y cuando tengas otro archivo `.DBF` sano con la misma estructura**.

---

## ⚠️ Advertencia importante

> Este script **no repara archivos `.DBF` corruptos por sí solo**. Para recuperar la información:
>
> - Necesitas tener un archivo `.DBF` que tenga **la misma estructura** (mismos campos, orden y tipos de datos).
> - El script simplemente **borra todos los registros del archivo destino** y luego **copia los registros del archivo fuente**.

---

## 🧾 ¿Qué hace este script?

1. Abre el archivo `.DBF` destino.
2. Elimina todos los registros existentes.
3. Abre el archivo `.DBF` origen.
4. Copia los registros del archivo origen al archivo destino.
5. Muestra el progreso en consola.

---

## 🛠️ Requisitos

- Python 3.6+
- Librería [`dbf`](https://pypi.org/project/dbf/)

Instalación del módulo:

```bash
pip install dbf
📦 Estructura del código
python
Copiar código
generador = generadorDBF('origen.dbf', 'destino.dbf')
generador.generar()
▶️ Cómo usarlo
Asegúrate de tener dos archivos .DBF:

Uno dañado o que contiene los datos que deseas rescatar (origen.dbf)

Otro válido y vacío (o con datos prescindibles) pero con la misma estructura (destino.dbf)

Guarda el script en un archivo, por ejemplo copiar_datos_dbf.py.

Ejecuta el script con Python:

bash
Copiar código
python copiar_datos_dbf.py
El script mostrará en consola el progreso del borrado y la copia.

🧯 Ejemplo de uso
python
Copiar código
from copiar_datos_dbf import generadorDBF

# Archivos DBF con misma estructura
generador = generadorDBF("datos_corruptos.dbf", "estructura_valida.dbf")
generador.generar()
❗ Notas adicionales
Se recomienda hacer una copia de seguridad de ambos archivos antes de ejecutar el script.

En caso de errores durante la copia, los registros problemáticos se saltarán y se imprimirá el error en consola.

El script utiliza dbf.delete() y pack() para eliminar los registros actuales antes de copiar.
