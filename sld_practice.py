import flet as ft
from base_conocimientos import Hechos

def puede_alta (x):
    if Hechos["Personas"][x]:
        return tiene_vehiculo_alta(x)
    return None

def tiene_vehiculo_alta(x):
    vehiculos = ["Automovil", "Motocicleta", "Camion", "Remolque"]
    if (Hechos["Personas"][x]["Vehiculo"]["Tipo"] in vehiculos 
        and not Hechos["Personas"][x]["Vehiculo"]["Registrado"]):
        m = Hechos["Personas"][x]["Municipio"]
        return vive_Ensenada(x,m)
    return "Vehiculo no valido" 

def vive_Ensenada(x,m):
    if m == "Ensenada":
        t = Hechos["Personas"][x]["TipoPersona"]
        return id_valida(x,t)
    return "Solo residentes de ensenada pueden realizar el tramite en ensenada"

def id_valida(x,t):
    if (t == "Moral" and Hechos["Personas"][x]["IdentificacionRepresentante"] == "Vigente" 
        or t == "Fisica" and Hechos["Personas"][x]["Identificacion"] == "Vigente"):
            return ver_docs(x,t)           
    return "Su identificacion no es valida"

def ver_docs(x,t):
    if t == "Moral":
        docs = ["ComprobanteDomicilio", "EscrituraConstitutiva","CedulaFiscalRFC",
                "PagoDerechos","SeguroResponsabilidadCivil"]
    else:
        docs = ["ComprobanteDomicilio","LicenciaConducirVigente","FacturaOriginal",
                "PagoDerechos", "SeguroResponsabilidadCivil"]
        if Hechos["Personas"][x]["Discapacidad"]:
            docs.append("ComprobanteMedico")
    if Hechos["Personas"][x]["Vehiculo"]["Foraneo"]:
        docs.append("SolicitudForaneo")
    if sorted(docs) == sorted(Hechos["Personas"][x]["Documentos"]["AltaVehicular"]):
        return "Tiene todo lo necesario para realizar el tramite"
    return "Faltan documentos"

def puede_baja(x):
    if Hechos["Personas"][x]:
        return tiene_vehiculo_baja(x)
    return None

def tiene_vehiculo_baja(x):
    if Hechos["Personas"][x]["Vehiculo"]["Registrado"]:
        m = Hechos["Personas"][x]["Municipio"]
        return vive_Ensenada_baja(x,m)
    return "Vehiculo no valido"

def vive_Ensenada_baja(x,m):
    if m == "Ensenada":
        t = Hechos["Personas"][x]["TipoPersona"]
        return id_valida_baja(x,t)
    return "Solo residentes de ensenada pueden realizar el tramite en ensenada"

def id_valida_baja(x,t):
    if (t == "Moral" and Hechos["Personas"][x]["IdentificacionRepresentante"] == "Vigente" 
        or t == "Fisica" and Hechos["Personas"][x]["Identificacion"] == "Vigente"):
            return ver_docs_baja(x)           
    return "Su identificacion no es valida"

def ver_docs_baja(x):
    docs = ["Placas","TarjetaCirculacion", "PagoDerechos"]
    if sorted(docs) == sorted(Hechos["Personas"][x]["Documentos"]["BajaVehicular"]):
        return "Tiene todo lo necesario para realizar el tramite"
    return "Faltan documentos"

def main(page: ft.Page):
    page.title = "Gestión Vehicular - Sistema Experto"
    page.horizontal_alignment = "center"
    page.window_width = 500
    page.window_height = 400

    nombres = list(Hechos["Personas"].keys())

    dropdown = ft.Dropdown(
        label="Selecciona una persona",
        options=[ft.dropdown.Option(nombre) for nombre in nombres],
        width=300
    )

    salida_texto = ft.Text(value="", selectable=True, size=14)

    def ejecutar_alta(e):
        nombre = dropdown.value
        if not nombre:
            salida_texto.value = "Selecciona una persona primero."
        else:
            resultado = puede_alta(nombre)
            salida_texto.value = f"Resultado de alta para {nombre}:\n{resultado}"
        page.update()

    def ejecutar_baja(e):
        nombre = dropdown.value
        if not nombre:
            salida_texto.value = "Selecciona una persona primero."
        else:
            resultado = puede_baja(nombre)
            salida_texto.value = f"Resultado de baja para {nombre}:\n{resultado}"
        page.update()

    btn_alta = ft.ElevatedButton("Alta vehicular", on_click=ejecutar_alta)
    btn_baja = ft.ElevatedButton("Baja vehicular", on_click=ejecutar_baja)

    page.add(
        ft.Column(
            [
                ft.Text("Trámites Vehiculares", size=20, weight="bold"),
                dropdown,
                ft.Row([btn_alta, btn_baja], alignment="center"),
                ft.Divider(),
                salida_texto,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
    )

ft.app(target=main)
