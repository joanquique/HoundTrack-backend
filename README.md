# Hound Express Backend

Proyecto base del backend para **Hound Express**, desarrollado con Python y Django.

Este repositorio contiene la estructura inicial del proyecto que servirá como base para la implementación futura de la API encargada de administrar los eventos y estatus de envíos dentro del sistema.

---

## 📌 Descripción

El objetivo de este proyecto es construir un backend que permita:

- Administrar eventos relacionados con envíos
- Crear y actualizar estatus de paquetería
- Integrar una API para comunicación con el frontend desarrollado previamente
- Persistir información en base de datos para futuras referencias

Actualmente el proyecto se encuentra en su fase inicial, únicamente con la configuración base de Django para futuras implementaciones.

---

## 🛠️ Tecnologías utilizadas

- Python
- Django
- Entorno virtual (venv)

---

## ⚙️ Instalación y ejecución

### 1️⃣ Clonar repositorio

```bash
git clone https://github.com/joanquique/HoundTrack-backend

### Crear entorno virutal
python -m venv .venv

### Activar entorno
.\.venv\Scripts\Activate.ps1

### Mac/Linux
source .venv/bin/activate

### instalar dependencias
pip install django

### Ejecutar servidor
python manage.py runserver

### Abrir en navegador
http://localhost:8000

