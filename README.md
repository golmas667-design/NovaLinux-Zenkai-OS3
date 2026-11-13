# NovaLinux Zenkai OS

Distribución personalizada basada en **Debian 13 (Trixie)**.

## Estado del proyecto

**Fase inicial de documentación.** Todavía no hay una ISO compilada ni validada. El objetivo es preparar una imagen Live reproducible con Debian Live-Build.

## Objetivos de la primera versión

- Arquitectura amd64.
- Escritorio XFCE y LightDM.
- Sesión Live con live-boot y live-config.
- NetworkManager.
- Firmware de Debian desde main, contrib, non-free y non-free-firmware.
- Herramientas de hardware, audio, Bluetooth y almacenamiento.
- Arranque BIOS y UEFI.
- Automatización de compilación mediante GitHub Actions.
- Pruebas de arranque en QEMU o VirtualBox antes de declarar estable la ISO.

## Criterios técnicos

- Mantener live-boot, live-config y live-config-systemd.
- No desactivar APT recommends sin medir y probar el impacto.
- No incluir contraseñas personales, tokens ni secretos en el repositorio.
- No prometer compatibilidad universal: algunos dispositivos requieren firmware específico.
- Una compilación correcta no sustituye las pruebas de arranque e instalación.

## Próximas etapas

1. Añadir configuración de Debian Live-Build.
2. Añadir listas de paquetes y scripts de personalización.
3. Añadir workflow de GitHub Actions.
4. Compilar y corregir errores.
5. Probar la ISO en máquina virtual y documentar resultados.
