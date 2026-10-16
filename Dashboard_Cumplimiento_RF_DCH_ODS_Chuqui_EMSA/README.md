# Dashboard Cumplimiento RF DCH ODS Chuqui EMSA

Dashboard web para visualizar el cumplimiento general de los riesgos RF04, RF06, RF10, RF18, RF20 y RF27, con seguimiento de evidencias, observaciones, planes mitigadores y fechas de implementación.

## Archivos

- `app.py`: aplicación Streamlit que presenta el dashboard HTML.
- `dashboard.html`: interfaz interactiva con panel general, filtros y semáforo de antigüedad.
- `requirements.txt`: dependencias para Streamlit Community Cloud.

## Ejecutar localmente

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Publicar en Streamlit Community Cloud

1. Sube estos tres archivos a un repositorio de GitHub.
2. Entra a https://share.streamlit.io/ e inicia sesión con GitHub.
3. Selecciona **Create app**.
4. Elige el repositorio, la rama `main` y el archivo principal `app.py`.
5. Pulsa **Deploy** y espera a que termine la instalación.

## Actualizar la planilla

Abre la aplicación publicada y utiliza el botón **Actualizar información** del propio dashboard para seleccionar el Excel actualizado. El archivo debe conservar los nombres de hojas y la estructura esperada: `RF04`, `RF06`, `RF10`, `RF18`, `RF20` y `RF27`.

La planilla se procesa en el navegador y no se incorpora al repositorio de GitHub ni se guarda automáticamente en el servidor. La carga de Excel requiere acceso a Internet para obtener la biblioteca XLSX desde CDN.
