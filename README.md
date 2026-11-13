# NovaLinux Zenkai OS
Distribución Live personalizada basada en Debian 13 (Trixie), arquitectura amd64.

## Primera imagen de desarrollo
- Kernel Debian amd64, live-boot y live-config.
- XFCE, LightDM y NetworkManager.
- Firmware Debian desde main, contrib, non-free y non-free-firmware.
- Herramientas de diagnóstico y particionado.
- Arranque ISO híbrido BIOS/UEFI.

## Compilar
En GitHub: Actions → Construir NovaLinux Zenkai OS ISO → Run workflow.
El resultado se publica como artefacto descargable.

## Estado
Primera configuración de desarrollo. No se considera estable hasta compilar y probar inicio Live, sesión gráfica, red, almacenamiento e instalador en máquina virtual y hardware real.

La sesión Live solicita el usuario admin; verificar el comportamiento de autenticación durante la prueba. No se promete compatibilidad universal con todo el hardware.
