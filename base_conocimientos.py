HECHOS = {
    "reglas": [
        ('persona', 'Juan'),
        ('persona', 'Felipe'),
        ('persona', 'EmpresaABC'),

        ('municipio', 'Juan', 'Ensenada'),
        ('municipio', 'Felipe', 'Ensenada'),
        ('municipio', 'EmpresaABC', 'Ensenada'),

        ('tipo_persona', 'Juan', 'Fisica'),
        ('tipo_persona', 'Felipe', 'Fisica'),
        ('tipo_persona', 'EmpresaABC', 'Moral'),

        ('identificacion', 'Juan', 'Vigente'),
        ('identificacion', 'Felipe', 'Vigente'),
        ('identificacion_representante', 'EmpresaABC', 'Vigente'),

        ('discapacidad', 'Juan', False),
        ('discapacidad', 'Felipe', False),

        ('vehiculo', 'Juan', 'auto_juan'),
        ('vehiculo', 'Felipe', 'moto_felipe'),
        ('vehiculo', 'EmpresaABC', 'camion_abc'),

        ('tipo_vehiculo', 'auto_juan', 'Automovil'),
        ('tipo_vehiculo', 'moto_felipe', 'Motocicleta'),
        ('tipo_vehiculo', 'camion_abc', 'Camion'),

        ('foraneo', 'auto_juan', False),
        ('foraneo', 'moto_felipe', False),
        ('foraneo', 'camion_abc', True),

        ('registrado', 'auto_juan', True),
        ('registrado', 'moto_felipe', False),
        ('registrado', 'camion_abc', True),

        ('documentos_alta', 'Juan', [
            "ComprobanteDomicilio",
            "LicenciaConducirVigente",
            "FacturaOriginal",
            "PagoDerechos",
            "SeguroResponsabilidadCivil"
        ]),
        ('documentos_alta', 'Felipe', [
            "ComprobanteDomicilio",
            "LicenciaConducirVigente",
            "FacturaOriginal",
            "PagoDerechos",
            "SeguroResponsabilidadCivil"
        ]),
        ('documentos_alta', 'EmpresaABC', [
            "ComprobanteDomicilio",
            "EscrituraConstitutiva",
            "CedulaFiscalRFC",
            "PagoDerechos",
            "SeguroResponsabilidadCivil",
            "SolicitudForaneo"
        ]),

        ('documentos_baja', 'Juan', [
            "TarjetaCirculacion",
            "Placas",
            "PagoDerechos"
        ]),
        ('documentos_baja', 'Felipe', [
            "TarjetaCirculacion",
            "Placas",
            "PagoDerechos"
        ]),
        ('documentos_baja', 'EmpresaABC', [
            "Placas",
            "TarjetaCirculacion",
            "PagoDerechos"
        ]),
    ]
}
