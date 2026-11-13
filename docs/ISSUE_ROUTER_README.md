# Issue Router — integración inicial segura

**Estado:** código propuesto para revisión en PR; sin integración n8n habilitada.

El workflow es **manual**, exige Issue abierto del propietario/colaborador, etiqueta `agent-approved` y exactamente una etiqueta `agent:<nombre>`. Genera un JSON de metadatos y un artefacto descargable, **sin copiar el cuerpo del Issue** a logs ni archivos públicos. No ejecuta ninguna IA, no envía mensajes, no crea PR automáticamente, no despliega y no consume API comercial.

## Uso futuro

1. En un repositorio **privado** de dirección, abrir Issue con tarea e información necesaria.
2. Aplicar `agent-approved` y `agent:gemini` (o el proveedor seleccionado).
3. Ejecutar el workflow manualmente en un entorno autorizado.
4. Revisar el resultado `work-order.json`, sin información sensible.
5. Solo tras pruebas y aprobación, conectar salida a n8n con identidad y secret seguro, presupuesto y control de permisos.

**Nota:** este repositorio es público. No usarlo para Issues comerciales reales ni pasarle secretos. El workflow aquí es demostrativo: GitHub no se enlaza automáticamente con otros repositorios por alojar documentación.

### Pruebas

```bash
python -m unittest discover -s tests -p 'test_issue_router.py' -v
```

Los tests verifican autorización, etiquetas, rutas, protección de datos de cuerpo y rechazo de tareas ambiguas. No demuestran conexión con n8n ni agentes externos.
