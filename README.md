# AZ-Watch

AZ-Watch es una aplicación web para monitorear los tickets de ServiceNow en tiempo real. La aplicación recibe información constantemente del fake-generator y utiliza Redis para almacenar los datos en memoria, lo que permite un rápido acceso a los tickets activos de ServiceNow.

## Características

- Monitoreo en tiempo real de tickets gracias al webhook implementado en el fake-generator.
- Almacenamiento de tickets activos en Redis para un acceso rápido.
- Personalización de dashboards para adaptarse a las necesidades de cada usuario.
- Notificaciones personalizables enviadas a través de Outlook y Microsoft Teams.
- Visualización de servicios impactados basándose en los tickets abiertos, servicios y prioridad.
- Histórico de tickets para cada servicio.

## Configuración e instalación

Sigue estos pasos para configurar la aplicación:

1. Crea un entorno virtual:

```
python3 -m venv env
```

2. Activa el entorno virtual:

- En Linux o macOS:
```
source env/bin/activate
```

- En Windows:
```
.\env\Scripts\activate
```

3. Instala las dependencias del archivo `requirements.txt`:
```
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```


Ahora, la aplicación debería estar ejecutándose en `http://127.0.0.1:8000/`.

## Integración con fake-generator

Para recibir datos constantemente del fake-generator, primero se debe de correr este proyecto y despues el faker.
Asegurate de tener instalado redis en tu equipo.
Asegúrate de configurar correctamente la URL del webhook en la función `post_updated_tickets` en el archivo `main.py` del fake-generator.

La aplicación az-watch procesará la información recibida a través del webhook y actualizará la base de datos en memoria (Redis) con los nuevos tickets y cambios en Business Services y Business Groups.

