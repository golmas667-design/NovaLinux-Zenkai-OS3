# NovaLinux Zenkai OS

Distribución personalizada basada en **Debian 13 (Trixie)**.

## Estado del proyecto

**Primera infraestructura de compilación añadida.** El repositorio contiene la configuración inicial de Debian Live-Build y un workflow de GitHub Actions para construir una ISO Live amd64 con XFCE.

La ISO todavía debe compilarse y superar las pruebas de arranque antes de considerarse funcional o estable.

## Objetivos de la primera versión

- Debian 13 Trixie, arquitectura amd64.
- Escritorio XFCE y LightDM.
- Sesión Live con live-boot y live-config.
- NetworkManager.
- Firmware y controladores disponibles en los repositorios Debian habilitados.
- Herramientas de hardware, audio, Bluetooth y almacenamiento.
- Imagen ISO híbrida para medios USB y arranque de PC.
- Compilación automatizada mediante GitHub Actions.
- Verificación de existencia, tamaño, tipo y SHA-256 de la ISO.
- Pruebas posteriores de arranque en QEMU o VirtualBox y, cuando sea posible, hardware real.

## Compilar en GitHub

1. Abrir la pestaña **Actions** del repositorio.
2. Seleccionar **Build NovaLinux Zenkai OS ISO**.
3. Pulsar **Run workflow** en la rama `main`.
4. Esperar a que finalice el trabajo `Debian 13 Live ISO (amd64)`.
5. Si termina correctamente, descargar el artefacto `NovaLinux-Zenkai-OS-Debian13-amd64`.

Los commits que modifican `auto/`, `config/` o el workflow también disparan la compilación automáticamente.

## Estructura inicial

- `.github/workflows/build-iso.yml`: compilación y validación en GitHub Actions.
- `auto/config`: parámetros de Debian Live-Build.
- `config/package-lists/zenkai.list.chroot`: paquetes del sistema Live.
- `config/README.md`: notas de configuración.

## Criterios técnicos y de seguridad

- Mantener live-boot, live-config y live-config-systemd.
- No desactivar APT recommends sin medir y probar el impacto.
- No incluir contraseñas personales, tokens ni secretos en el repositorio.
- No prometer compatibilidad universal: algunos dispositivos requieren firmware específico.
- Una compilación correcta no sustituye las pruebas de arranque, instalación, red, audio, gráficos y suspensión.
- No declarar una versión estable hasta documentar las pruebas y sus resultados.

## Próximas etapas

1. Ejecutar y revisar la primera compilación de GitHub Actions.
2. Corregir errores reales del proceso de construcción.
3. Probar el arranque Live en una máquina virtual.
4. Validar instalación, hardware, red, audio y apagado/reinicio.
5. Añadir personalización visual y herramientas propias de Zenkai OS.
