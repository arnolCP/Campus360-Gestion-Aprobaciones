# Módulo de Gestión de Flujo de Aprobaciones (Campus360)

Motor de decisiones jerárquico diseñado para automatizar trámites universitarios, garantizando el cumplimiento de Acuerdos de Nivel de Servicio (SLA) y la trazabilidad de auditoría. 

## Tecnologías Utilizadas
*   **Backend:** Python, FastAPI, Uvicorn
*   **Frontend:** React
*   **Testing:** Pytest
*   **Arquitectura:** Modelo 4+1 Vistas, Arquitectura Orientada a Servicios (SOA), Clean Architecture

## Documentación y Análisis Funcional
Este repositorio destaca por su exhaustivo nivel de diseño y documentación arquitectónica. Los documentos detallados se encuentran disponibles en el repositorio e incluyen:
*   **Arquitectura de Software:** Diseño estructural bajo el modelo 4+1 vistas de Kruchten.
*   **Contratos API REST:** Manual de integración y especificaciones de endpoints.
*   **Patrones de Diseño Aplicados:** Justificación técnica de las decisiones de diseño.
*   **Plan y Ejecución de Pruebas:** Estrategia de validación y aseguramiento de calidad (QA).

## Instrucciones de Ejecución (Entorno de Desarrollo)

### Backend
1. Acceder al directorio del servidor:
`cd backend`
2. Activar el entorno virtual:
`.\venv\Scripts\activate`
3. Levantar el servidor:
`uvicorn app.main:app --reload`
4. Acceder a la documentación interactiva de la API (Swagger): Abrir el navegador en `http://127.0.0.1:8000/docs`

### Ejecución de Pruebas
Para ejecutar la batería de pruebas unitarias y de integración:
`python -m pytest`
