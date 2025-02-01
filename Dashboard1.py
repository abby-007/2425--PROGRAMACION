# -*- coding: utf-8 -*-
# DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS
# Autora: ESTHER SELLAN BARAHONA
# Repositorio: https://github.com/abby-007/2425--PROGRAMACION.git

import os
from typing import Union


def mostrar_codigo(ruta_relativa: Union[str, os.PathLike]) -> None:
    """
    Muestro el contenido de un archivo desde la raíz del proyecto.

    Parámetros:
    ruta_relativa (Union[str, os.PathLike]): Ruta relativa desde la carpeta raíz
    """
    try:
        ruta_base = os.path.dirname(__file__)
        ruta_completa = os.path.abspath(os.path.join(ruta_base, str(ruta_relativa)))

        if not os.path.exists(ruta_completa):
            raise FileNotFoundError(f"❌ Archivo no encontrado: {os.path.basename(ruta_relativa)}")

        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            print(f"\n{'═' * 50} INICIO DEL CÓDIGO {'═' * 50}")
            print(f"📄 ARCHIVO: {os.path.basename(ruta_completa)}")
            print(f"📂 UBICACIÓN: {ruta_completa}\n")
            print(archivo.read())
            print(f"{'═' * 50} FIN DEL CÓDIGO {'═' * 50}\n")

    except Exception as error:
        print(f"\n⚠️ ERROR: {str(error)}")


def generar_menu() -> None:
    """
    Genero el menú interactivo con estructura de proyecto exacta
    """
    opciones = {
        '1': {
            'ruta': 'Unidad 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py',
            'desc': 'Técnicas básicas de programación - Mis prácticas'
        },
        '2': {
            'ruta': 'Unidad 1/2.1. Programacion tradicional frente a POO/2.1-1. Ejemplo Programacion tradicional frente a POO.py',
            'desc': 'Comparativa programación tradicional vs POO - Mi análisis'
        },
        '3': {
            'ruta': 'Unidad 1/2.2. Caracteristicas de la POO/2.2.1. Ejemplo Caracteristicas POO.py',
            'desc': 'Características POO - Mis implementaciones'
        }
    }

    while True:
        print("\n" + "★" * 60)
        print("🌟 DASHBOARD PERSONAL DE ESTHER SELLAN - POO")
        print("★" * 60 + "\n")

        for clave, valor in opciones.items():
            print(f"[{clave}] {valor['desc']}")

        print("\n[0] Salir y actualizar repositorio\n")

        eleccion = input("▶ Tu selección: ")

        if eleccion == '0':
            print("\n✅ ¡Recuerda ejecutar estos comandos para actualizar GitHub:")
            print("git add .")
            print('git commit -m "Dashboard actualizado con mis scripts"')
            print("git push origin main\n")
            break

        if eleccion in opciones:
            mostrar_codigo(opciones[eleccion]['ruta'])
        else:
            print("\n⚠️ ¡Opción no válida! Intenta con 1, 2, 3 o 0")


if __name__ == "__main__":
    print("\n" + "═" * 70)
    print(f"🔧 Dashboard ejecutado desde: {os.path.abspath(os.path.dirname(__file__))}")
    print("═" * 70)

    generar_menu()

# NOTA PARA EL INGENIERO:
# He oraganizado mi repoitorio con la estructura que tengo ya que los otros proyectos personales
# y ejercicios adicionales los desarrollo en repositorios independientes.