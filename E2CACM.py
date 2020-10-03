try:
    from bs4 import BeautifulSoup as bs
except ImportError: 
    os.system('pip install bs4')
    print('Installing bs4...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import sys
except ImportError:
    os.system('pip install sys')
    print('Installing sys...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import os
except ImportError:
    os.system('pip install os')
    print('Installing os...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import requests
except ImportError:
    os.system('pip install requests')
    print('Installing requests...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    exit()


# Carlos Augusto Covarrubias Miranda
"""Este script utiliza la librería bs4 para extraer información de sitios web,
la librería webbrowser es usada para abrir documentos o sitios web en el
navegador por defecto y los modulos os y sys nos permiten acceder a funciones
del sistema operativo"""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango, finRango = finRango, inicioRango
for i in range(inicioRango, finRango, 1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get(url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content, "html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content, "html.parser")
                parrafos = soup2.select("p")
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print("Abriendo", url2)
                        webbrowser.open(url2)
                        break
