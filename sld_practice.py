import flet as ft
from base_conocimientos import HECHOS

def obtener(predicado, sujeto):
    return [
        t[2]
        for t in HECHOS["reglas"]
        if len(t) >= 3 and t[0] == predicado and t[1] == sujeto
    ]

def obtener_unico(predicado, sujeto):
    valores = obtener(predicado, sujeto)
    return valores[0] if valores else None

# Alta
def puede_alta(nombre):
    tipo_vehiculo = obtener_unico('tipo_vehiculo', obtener_unico('vehiculo', nombre))
    registrado = obtener_unico('registrado', obtener_unico('vehiculo', nombre))
    if tipo_vehiculo in ["Automovil", "Motocicleta", "Camion", "Remolque"] and not registrado:
        municipio = obtener_unico('municipio', nombre)
        return vive_Ensenada(nombre, municipio)
    return "Vehículo no válido o ya registrado."

def vive_Ensenada(nombre, municipio):
    if municipio == "Ensenada":
        tipo = obtener_unico('tipo_persona', nombre)
        return id_valida(nombre, tipo)
    return "Solo residentes de Ensenada pueden realizar el trámite."

def id_valida(nombre, tipo):
    if (tipo == "Moral" and obtener_unico('identificacion_representante', nombre) == "Vigente") or \
       (tipo == "Fisica" and obtener_unico('identificacion', nombre) == "Vigente"):
        return ver_docs(nombre, tipo)
    return "Su identificación no es válida."

def ver_docs(nombre, tipo):
    docs_requeridos = []
    if tipo == "Moral":
        docs_requeridos = [
            "ComprobanteDomicilio", "EscrituraConstitutiva", "CedulaFiscalRFC",
            "PagoDerechos", "SeguroResponsabilidadCivil"
        ]
    else:
        docs_requeridos = [
            "ComprobanteDomicilio", "LicenciaConducirVigente", "FacturaOriginal",
            "PagoDerechos", "SeguroResponsabilidadCivil"
        ]
        if obtener_unico('discapacidad', nombre):
            docs_requeridos.append("ComprobanteMedico")

    vehiculo_id = obtener_unico('vehiculo', nombre)
    if obtener_unico('foraneo', vehiculo_id):
        docs_requeridos.append("SolicitudForaneo")

    documentos = obtener_unico('documentos_alta', nombre)
    if sorted(docs_requeridos) == sorted(documentos):
        return "Tiene todo lo necesario para realizar el trámite."
    return "Faltan documentos."

# Baja
def puede_baja(nombre):
    vehiculo_id = obtener_unico('vehiculo', nombre)
    registrado = obtener_unico('registrado', vehiculo_id)
    if registrado:
        municipio = obtener_unico('municipio', nombre)
        return vive_Ensenada_baja(nombre, municipio)
    return "Vehículo no válido o no registrado."

def vive_Ensenada_baja(nombre, municipio):
    if municipio == "Ensenada":
        tipo = obtener_unico('tipo_persona', nombre)
        return id_valida_baja(nombre, tipo)
    return "Solo residentes de Ensenada pueden realizar el trámite."

def id_valida_baja(nombre, tipo):
    if (tipo == "Moral" and obtener_unico('identificacion_representante', nombre) == "Vigente") or \
       (tipo == "Fisica" and obtener_unico('identificacion', nombre) == "Vigente"):
        return ver_docs_baja(nombre)
    return "Su identificación no es válida."

def ver_docs_baja(nombre):
    docs_requeridos = ["Placas", "TarjetaCirculacion", "PagoDerechos"]
    documentos = obtener_unico('documentos_baja', nombre)
    if sorted(docs_requeridos) == sorted(documentos):
        return "Tiene todo lo necesario para realizar el trámite."
    return "Faltan documentos."

# Interfaz
def main(page: ft.Page):
    page.title = "Gestión Vehicular - Sistema Experto (Tuplas)"
    page.horizontal_alignment = "center"
    page.window.width = 500
    page.window.height = 400

    nombres = [t[1] for t in HECHOS["reglas"] if t[0] == 'persona']

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
            salida_texto.value = f"Resultado de alta para {nombre}:\n{puede_alta(nombre)}"
        page.update()

    def ejecutar_baja(e):
        nombre = dropdown.value
        if not nombre:
            salida_texto.value = "Selecciona una persona primero."
        else:
            salida_texto.value = f"Resultado de baja para {nombre}:\n{puede_baja(nombre)}"
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
