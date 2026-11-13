# Configuración de Debian Live-Build

Esta carpeta contiene la configuración del sistema Live de NovaLinux Zenkai OS.

- `package-lists/zenkai.list.chroot`: paquetes instalados dentro de la imagen.
- `hooks/`: scripts ejecutados durante la construcción del sistema (se añadirán cuando haya personalizaciones verificadas).
- `includes.chroot/`: archivos que se copiarán al sistema raíz de la imagen.

La primera iteración prioriza una ISO Live amd64 con XFCE, NetworkManager y firmware distribuido por Debian. La compatibilidad real depende del dispositivo y debe probarse en hardware y máquinas virtuales.
