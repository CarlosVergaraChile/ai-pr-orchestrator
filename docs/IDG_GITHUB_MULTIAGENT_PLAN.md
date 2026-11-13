# IDG | Orquestación de IA desde GitHub — diseño de implantación

**Estado:** arquitectura propuesta, no ejecutada. **Fecha:** 2026-11-12. Responsable de integración: dirección de producto.

## Decisión

Usar **GitHub Issues** para encargos, **Pull Requests** para propuestas y código, **GitHub Actions** para verificaciones, y un repositorio **privado** de dirección como centro de operaciones. Mantener este repositorio `ai-pr-orchestrator` público para documentación y componentes reutilizables que sean revisados para publicación.

No usar el repositorio público `coipo-orchestrator` como archivo de contactos, datos privados, contraseñas ni investigaciones sensibles: ese repositorio documenta un MVP distinto, de análisis de Gmail con OAuth y n8n.

## Estado real observado

- La raíz de `ai-pr-orchestrator` contiene README, configuración, guías y un workflow, pero no aparece la carpeta `scripts/` que el README indica como componente del sistema.
- Las versiones de modelos documentadas en el archivo YAML son históricas. No se infiere que endpoints, modelos ni API keys estén habilitados.
- No hay evidencia aquí de una ejecución end-to-end multiagente, facturación habilitada, webhooks ni permisos de proveedores.
- Por tanto, **orquestador documentado, implementación operativa no verificada**.

## Experiencia deseada

1. La dirección crea un Issue con objetivo, producto, criterios de aceptación, fuentes permitidas y visibilidad.
2. El Issue incluye agente objetivo o tipo de trabajo: `agent:claude`, `agent:gemini`, `agent:deepseek`, `agent:perplexity`, `agent:manus`, `agent:grok`, `agent:chatgpt`.
3. Un dispatcher **solo cuando esté configurado y probado**, identifica la tarea y consulta la API del proveedor con credenciales en GitHub Secrets o identidad federada.
4. El agente entrega un informe como comentario y/o archivo propuesto en una rama `agent/<provider>/<issue-number>`.
5. Un PR referencia `Closes #N` y adjunta metodología, fuentes, evidencia de pruebas y limitaciones.
6. CI valida formato, referencias, secretos y tests. La dirección revisa y acepta o rechaza.
7. Las publicaciones a Hostinger se gestionan por separado y necesitan autorización explícita; jamás se desencadenan por un simple Issue.

## Integraciones por prioridad

| Agente | Vía recomendada | Estado |
|---|---|---|
| Claude Code | App oficial/Claude Code GitHub Action; credenciales y permisos limitados | Disponible como mecanismo, conexión a este repo no verificada |
| Gemini CLI | Acción oficial GitHub `google-github-actions/run-gemini-cli` | Disponible como mecanismo, conexión no verificada |
| ChatGPT/Codex | Conector GitHub en ChatGPT para PR y gestión manual; GitHub Agentic Workflows o API para automatización real | Conector para operaciones GitHub disponible; servicio autónomo permanente no configurado |
| DeepSeek | API mediante un dispatcher con limitación de presupuesto; no equivale a su chat web | Pendiente de credenciales, adaptador, tests |
| Perplexity | API para investigación; no equivale a su sesión web Pro | Pendiente de credenciales y validación de citaciones |
| Manus | Manus API v2 Tasks, con resultados de regreso a Issues/PR | Pendiente de credenciales, adaptador |
| Grok | xAI API; revisión de compatibilidad y costos | Pendiente de credenciales, adaptador |
| Kodee | Integración específica Hostinger por confirmar; **no asumir** que GitHub Issue ejecuta acciones en Hostinger Agent | Manual hasta disponibilidad confirmada |
| Google AI Studio | API Gemini; modelos y permisos por proyecto | No requiere un segundo orquestador |
| Google Cloud | Solo backend si GitHub Actions resulta insuficiente | No contratar inicialmente |

## Seguridad y costos

- El trabajo **privado** (prospectos, evaluación comercial, datos sintéticos internos, auditorías y código propietario) se ejecuta solo en un repositorio privado.
- Nunca pegar API keys o credenciales en Issues, PR, commits, README, logs ni prompts.
- Usar GitHub Secrets, permisos mínimos por workflow, `GITHUB_TOKEN` de solo lectura por defecto y escritura delimitada por job.
- Deshabilitar ejecución sobre Issues creados por usuarios no autorizados; tratar prompts, adjuntos y comentarios como entrada no confiable.
- No enviar secretos ni datos privados del repositorio a proveedores IA sin revisión de permisos y acuerdos aplicables.
- Ejecutar por evento o despacho manual, no por sondeo continuo. Límite de presupuesto y concurrencia por proveedor.
- Guardar hashes/ID de solicitud, gasto aproximado, versión de modelo, entrada, salida, evidencias y errores.
- Cambios de visibilidad, merges a `main`, publicación web, envíos de correos y gastos nuevos requieren revisión humana.

## Fase 1: operacional sin APIs

- Repo privado de coordinación; Issue template, etiquetas y tablero.
- Entregables estandarizados en `deliverables/<issue>/<agent>/` y `research/`.
- Todo agente que ya tenga GitHub autorizado podrá leer Issues y proponer PR. Los demás pueden requerir exportación manual temporal.
- Evaluar uno o dos agentes nativos (Claude/Gemini) en un repositorio de prueba sin datos comerciales.

## Fase 2: automatizar

- Dispatcher `workflow_dispatch` o evento Issue autorizado.
- Primero integración real de **un** proveedor, pruebas en sandbox, salida en PR.
- Después DeepSeek, Perplexity y Manus por API con auditoría independiente.
- No afirmar funcionamiento multiagente hasta demostrar una ejecución completa con log y PR final.

## Fuentes oficiales

- https://docs.github.com/en/actions/tutorials/develop-agentic-workflows-in-github-actions
- https://github.com/anthropics/claude-code-action
- https://github.com/google-github-actions/run-gemini-cli
- https://open.manus.ai/docs/v2/introduction

## Decisión de dirección: n8n primero, Zapier como complemento

El titular informa que ya dispone de cuentas n8n y Zapier asociadas al correo de referencia de sus herramientas, y otras cuentas adicionales. **No se han verificado instancias, URLs, planes, credenciales, permisos, webhooks ni flujos activos**. Compartir dirección de correo no otorga autorización ni conexión automática entre plataformas.

**Motor preferido: n8n existente**, si es accesible y permite webhooks seguros, autenticación y gestión de credenciales. GitHub sigue siendo registro central de Issue/PR/archivos y no se crea otro centro de mando. 

Flujo objetivo: Issue autorizado GitHub → evento n8n → comprobación allowlist de repositorio, autor y etiqueta → seleccionar proveedor IA configurado → ejecutar con contexto mínimo → guardar resultado en rama/PR o Issue → revisión humana. Para investigación sensible, operar solamente en repositorios privados.

Zapier queda para automatizaciones sencillas (avisos, calendarios, correo autorizado) si aportan valor, evitando duplicación de flujos con n8n. No programar envíos comerciales autónomos ni despliegues productivos.

**Verificación necesaria antes de activar:** encontrar la instancia n8n y su propietario, confirmar modo cloud/self-hosted, URL, versionado, límites de costos, GitHub App/token de alcance mínimo, gestor de secretos y workflow existente. Revisar cuentas secundarias **una por una** con autorización explícita. No copiar credenciales a Drive o a GitHub.

**Primera prueba sugerida:** crear un Issue sintético en repositorio privado, n8n recibe evento y deja un comentario/PR de demostración, con logs sin secretos. Después incorporar un único proveedor IA real y medir ejecución, costo y seguridad.
