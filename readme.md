<p style="text-align: right;">Juan Antonio Román Castro</p> 

# Práctica: Resolución SLD
Esta práctica maneja leyes de Horn y resolución SLD para realizar consultas con el fin de determinar si una persona puede dar de baja o dar de alta el vehículo que tiene registrado.
### Leyes de Horn
- alta_vehiculo(x) ← tiene_vehiculo_alta(x), vive_Ensenada(x,m), id_valida(x,t), ver_docs(x,t)
- baja_vehiculo(x) ← tiene_vehiculo_baja(x), vive_Ensenada_baja(x,m), id_valida_baja(x,t), ver_docs_baja(x,t)
#### Donde
- x ← Persona
- t ← Tipo de persona (física o moral)
- m ← Municipio de residencia
### Leyes usadas
#### Alta de vehículo
1. Si adquieres un vehículo, debes darlo de alta dentro de los siguientes 5 días hábiles.
2. Si deseas dar de alta un vehículo siendo persona física, debes presentar en original y copia la licencia de conducir vigente del Estado de Baja California.
3. Si deseas obtener placas para vehículo de persona con discapacidad, debes ser considerado persona física y presentar un certificado médico o constancia de discapacidad emitida por una institución pública.
4. Si tienes una discapacidad que te impide conducir el vehículo a dar de alta, debes presentar la licencia de conducir vigente del autorizado para conducir.
5. Si deseas dar de alta un vehículo siendo persona moral, debes presentar en original y copia comprobante de domicilio no mayor a tres meses de antigüedad, escritura constitutiva, cédula de identificación fiscal del Registro Federal de Contribuyentes, identificación oficial con fotografía vigente del representante legal y documentación que acredite la personalidad de quien comparece.
6. Si deseas dar de alta un vehículo foráneo, debes presentar registro y comprobantes de pago de la entidad federativa de origen.
7. Si deseas dar de alta un vehículo, debes presentar en original y copia el seguro de responsabilidad civil vigente que ampare los conceptos y el monto señalados en el artículo 18 bis de este ordenamiento.
8. Si deseas dar de alta un vehículo, debes presentarte en la oficina de Recaudación de Rentas de Ensenada junto con el vehículo.
9. Si deseas dar de alta un vehículo foráneo, debes presentar una solicitud para su trámite, la cual se validará en un plazo de 10 días.
10. Si se valida la solicitud para dar de alta un vehículo foráneo, debes regresar a la oficina de Recaudación de Rentas de Ensenada para continuar el trámite.
11. Si el trámite para dar de alta un vehículo se realiza con éxito, debes pagar las tarifas correspondientes en efectivo, cheque certificado o tarjeta de débito/crédito.
#### Baja de vehículo
1. Si deseas dar de baja tu vehículo, el vehículo debe estar dado de alta.
2. Si deseas dar de baja tu vehículo siendo persona física, debes presentarte con tu identificación oficial vigente (original y copia).
3. Si deseas dar de baja un vehículo siendo persona moral, debes presentarte con original y copia de la identificación oficial vigente y la documentación que acredite la personalidad de quien comparece.
4. Si realizas el trámite de dar de baja un vehículo, se te solicitará que entregues las placas y la tarjeta de circulación.
5. Si el trámite de dar de baja un vehículo se realiza con éxito, debes pagar $384.62 MXN en efectivo, cheque certificado o tarjeta de débito/crédito.
### Hechos usados
1. Un vehículo puede ser dado de alta por su representante legal o por una persona interesada.
2. Se debe llevar el vehículo para una verificación.
3. Un vehículo foráneo también puede ser dado de alta.
4. El precio varía según el tipo de vehículo que se dé de alta. Tarifas (en M.N.):

Para la expedición de tarjeta de circulación:
- Automóviles y camiones particulares: $1,779.85
- Motocicletas: $1,779.85
- Para demostración: $4,253.14
- Remolques: $1,636.86

Para la expedición de placas de circulación:
- Automóviles y camiones particulares: $1,874.63
- Motocicletas: $376.19
- Para demostración: $4,228.96
- Remolques: $1,359.19
- Para vehículo de persona con discapacidad: $1,874.63
5. No es necesario llevar el vehículo cuando se desea dar de baja.
6. El dueño del vehículo es quien debe darlo de baja.
7. El vehículo de una empresa se da de baja por un representante de la empresa.
8. Se entregan las placas y la tarjeta de circulación al dar de baja el vehículo.
9. El costo del trámite de dar de baja un vehículo es de $384.62 MXN.