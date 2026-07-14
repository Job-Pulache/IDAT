# Atlantic City CRM

Proyecto MVP desarrollado con Django, MySQL y Bootstrap para la gestión centralizada de clientes de Atlantic City.

## Descripción general

Atlantic City CRM es un sistema web desarrollado como parte de un trabajo académico. Su objetivo principal es centralizar la información del cliente en una sola plataforma, permitiendo registrar clientes, visitas, incidencias, promociones y visualizar indicadores desde un dashboard.

El sistema busca responder a una problemática relacionada con la información dispersa, la falta de trazabilidad del cliente y la dificultad para tomar decisiones basadas en datos.

## Módulos principales

* Login y cierre de sesión.
* Dashboard con indicadores generales.
* Gestión de clientes.
* Ficha única del cliente.
* Registro de visitas.
* Registro de incidencias.
* Gestión y asignación de promociones.
* Roles y permisos.
* Página de acceso no permitido 403.
* Interfaz responsive con Bootstrap y CSS personalizado.

## Tecnologías utilizadas

* Python
* Django
* MySQL
* HTML
* CSS
* Bootstrap
* JavaScript básico
* Git y GitHub

## Requisitos para ejecutar el proyecto

Cada integrante debe tener instalado:

* Python
* MySQL Community Server
* Visual Studio Code
* Git
* Navegador web actualizado

## Instalación en Windows 11

Clonar el repositorio:

```bash
git clone https://github.com/anthony-devtecno/atlantic_city_crm.git
```

Ingresar a la carpeta:

```bash
cd atlantic_city_crm
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear la base de datos en MySQL:

```sql
CREATE DATABASE atlantic_city_crm
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Configurar la contraseña local de MySQL en:

```text
config/settings.py
```

Ejecutar verificación:

```bash
python manage.py check
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear superusuario:

```bash
python manage.py createsuperuser
```

Levantar servidor:

```bash
python manage.py runserver
```

Ingresar al sistema:

```text
http://127.0.0.1:8000/login/
```

Ingresar al administrador de Django:

```text
http://127.0.0.1:8000/admin/
```

## Grupos sugeridos en Django Admin

Desde el administrador de Django se deben crear los siguientes grupos:

* Administrador
* Operaciones
* Marketing
* AtencionCliente

Cada grupo debe tener permisos según su función dentro del sistema.

## Nota para el equipo

No se debe subir la carpeta `venv`, archivos temporales ni bases de datos locales. Cada integrante debe crear su propio entorno virtual y su propia base de datos local en MySQL.
