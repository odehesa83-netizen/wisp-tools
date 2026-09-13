# WISP Tools

Herramientas open source para diagnóstico y monitoreo básico de redes WISP/ISP.

## Network Check

El script `network_check.py` permite realizar pruebas rápidas sobre una IP o dominio.

### Funciones

- Resolución DNS
- Ping
- Prueba de puerto DNS 53
- HTTP 80
- HTTPS 443
- MikroTik API 8728
- MikroTik Winbox 8291

## Requisitos

- Python 3
- Windows o Linux
- Conectividad de red hacia el destino a revisar

## Uso

Ejecuta:

```bash
python network_check.py
```

Después escribe la IP o dominio que quieres revisar.

Ejemplo:

```text
IP o dominio a revisar: 192.168.0.12
```

El script mostrará:

- Resolución DNS
- Resultado del ping
- Estado de los puertos configurados

## Objetivo

Este proyecto busca facilitar tareas básicas de diagnóstico para pequeños proveedores ISP/WISP, técnicos de campo y administradores de red.

La idea es reunir herramientas simples que ayuden a comprobar conectividad, servicios de red y equipos MikroTik sin depender de aplicaciones complejas.

## Próximas funciones

- Revisión de varias IP simultáneamente
- Monitoreo básico de equipos MikroTik
- Generación de reportes
- Pruebas de conectividad automatizadas
- Validación de servicios de red

## Licencia

Este proyecto se distribuye bajo licencia MIT.
