# NovaLinux Zenkai OS

Sistema operativo personalizado basado en Debian 13 Trixie.

## Objetivo de la primera imagen

Una ISO Live híbrida amd64 que integre en una sola imagen el sistema base, kernel, firmware disponible en Debian, escritorio XFCE, red, audio, Bluetooth, utilidades y herramientas iniciales para IA.

## Construcción

Requiere Debian 13 o entorno compatible, permisos de root y conexión a Internet:

```bash
sudo apt update
sudo apt install live-build debootstrap squashfs-tools xorriso grub-pc-bin grub-efi-amd64-bin mtools dosfstools
chmod +x auto/config auto/clean auto/build
sudo lb config
sudo lb build
```

La ISO se genera en el directorio raíz. No se considera terminada hasta verificar su arranque e instalación.

## IA local

La ISO debe integrar el acceso al asistente Zenkai y sus herramientas de preparación. Ollama y los modelos grandes se configuran después del primer arranque para no inflar innecesariamente la imagen.

## Limitaciones

- Primera versión amd64.
- El firmware depende del hardware.
- Deben probarse BIOS, UEFI, instalación, red, audio, gráficos y apagado antes de declarar estable la distribución.
