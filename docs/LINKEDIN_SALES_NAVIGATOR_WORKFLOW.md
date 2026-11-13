# Captación comercial con LinkedIn Sales Navigator — procedimiento seguro

**Fecha:** 2026-11-12
**Estado:** diseñado, no activado. No se ha leído ninguna lista de Sales Navigator del usuario ni publicaciones privadas.

## Conexiones confirmadas

- En ChatGPT hay herramienta LinkedIn para búsqueda de perfiles de terceros por nombre/apellido, empresa y cargo. **No da acceso al Sales Navigator de la cuenta**, listas guardadas, publicaciones de la red ni exportación de contactos.
- Hay conector HubSpot disponible para guardar cuentas, contactos y oportunidades, sujeto a verificar la conexión/destino antes de escribir.
- n8n y Zapier declarados por el usuario, pero sus instancias y credenciales no verificadas.

## Restricción del proveedor

LinkedIn indica que **Sales Navigator no exporta listas de leads/cuentas a CSV o XLS**. Solo **Advanced Plus** dispone de CRM Sync y creación de leads en CRM con socios como HubSpot. Advanced/planes inferiores tienen listas guardadas y alertas, no esa sincronización.

Referencias:
https://www.linkedin.com/help/sales-navigator/answer/a110717
https://www.linkedin.com/help/sales-navigator/answer/a106005
https://www.linkedin.com/help/sales-navigator/answer/a105133
https://business.linkedin.com/sell/sales-navigator/how-to-use

## Flujo escogido

1. Definir cuentas objetivo por segmento: proveedores tecnológicos salmoneros, productores, consultores y alianzas.
2. Guardar leads y cuentas dentro de Sales Navigator. Activar alertas de cambios de cargo y publicaciones. Guardar búsquedas por cargo y región.
3. Si la licencia real es **Advanced Plus**, conectar CRM Sync oficial con HubSpot (ver permisos, destino y no duplicados). Si no lo es, alimentar HubSpot solo con campos públicos necesarios y enlaces verificados, mediante búsqueda autorizada, sin scraping ni exportación masiva.
4. En HubSpot almacenar empresa, rol, nombre profesional público, URL del perfil, sitio oficial, razón de acercamiento, fuente, fecha de verificación y última acción. No copiar mensajes privados, InMail ni datos sensibles.
5. n8n, cuando esté integrado, vigila solamente cambios autorizados que ingresen por HubSpot, correo de alertas o APIs oficiales. Evitar automatizar extracción desde LinkedIn no autorizada por sus términos.
6. Los agentes redactan mensajes; ninguna invitación o contacto sale sin revisión comercial humana.

## Prioridad por vencimiento de cortesía

- Identificar fin del período de Sales Navigator.
- Crear listas guardadas para las empresas prioritarias.
- Activar alertas y búsquedas guardadas.
- Si no hay Advanced Plus, no prometer exportación de datos ni continuidad de funciones Premium al terminar la cortesía.
- Revisar cada cargo antes de usarlo en un mensaje.

## Primeras metas

15 cuentas objetivo y 30 roles, cinco mensajes preparados, y 3 reuniones solicitadas después de aprobación. Estas son metas, **no resultados**.

## Criterios de aceptación para automatización futura

- No contraseñas ni cookies de LinkedIn en GitHub.
- Ningún scraping masivo de Sales Navigator.
- Dedupe por URL de LinkedIn + empresa.
- Alertas de publicaciones solo por mecanismos oficiales o datos públicos permitidos.
- Separación entre contacto investigado, validado, contactado y convertido.
