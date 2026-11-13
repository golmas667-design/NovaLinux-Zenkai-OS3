# NovaLinux Zenkai OS — Arquitectura técnica

**Estado:** especificación inicial para revisión; no es una ISO ni certifica una compilación.  
**Base:** Debian 13 Trixie.  
**Arquitectura inicial:** amd64.  
**Kernel:** kernel oficial de Debian (`linux-image-amd64`).  
**Instalador:** Calamares.  
**Inteligencia artificial:** NO INCLUIDA. No instalar Ollama, modelos, agentes, asistentes ni servicios de IA.

## 1. Objetivo y alcance

Construir una distribución Linux completa, arrancable en modo Live e instalable en disco, distribuida como una única ISO híbrida amd64. El repositorio contiene los archivos fuente y configuración organizados; el proceso de construcción integra los componentes en la ISO final.

La primera versión se limita a amd64. No se declara compatible con todo el hardware: los controladores y firmware disponibles se seleccionan desde Debian y la compatibilidad se valida en equipos concretos.

## 2. Capas del sistema

1. **Firmware y arranque:** BIOS heredado y UEFI; cargador GRUB; kernel Debian; initramfs.
2. **Kernel:** kernel Debian amd64, módulos, gestión de memoria, procesos, dispositivos y energía.
3. **Sistema base:** Debian 13, systemd, libc y bibliotecas, usuarios, grupos, permisos, sudo, servicios y registro de eventos.
4. **Almacenamiento:** particiones, UUID, montaje, herramientas de sistemas de archivos y utilidades de disco.
5. **Hardware:** firmware no libre cuando corresponda, módulos y herramientas para PCI, USB, gráficos, red, Wi-Fi, Bluetooth, audio e impresoras. La selección exacta de paquetes debe validarse contra los repositorios Trixie antes de compilar.
6. **Red:** NetworkManager, Ethernet, Wi-Fi, DNS y herramientas de diagnóstico.
7. **Audio y multimedia:** ALSA, PipeWire/WirePlumber y controles de volumen.
8. **Entorno gráfico:** servidor gráfico compatible, XFCE, LightDM, gestor de archivos, terminal, panel, configuración regional y temas.
9. **Aplicaciones esenciales:** navegador, editor de texto, archivador, visor PDF, utilidades del sistema y herramientas de actualización.
10. **Instalador:** Calamares con configuración y branding propios, módulos habilitados explícitamente, particionado revisado, selección de usuario/contraseña, zona horaria, teclado, instalación del cargador de arranque y finalización.
11. **Recuperación y diagnóstico:** herramientas para revisar discos, memoria, dispositivos, red, registros y reparar el arranque desde un entorno Live.
12. **Empaquetado:** SquashFS, estructura ISO híbrida, arranque BIOS/UEFI, manifiesto de paquetes y checksum SHA256.

## 3. Identidad y sesión Live

Se debe conservar la intención de la guía original del proyecto: sesión Live con usuario `admin`, inicio automático de escritorio y contraseña temporal Live `live`, si se confirma que esa es la política deseada. La contraseña Live no debe convertirse en la contraseña del usuario instalado. Calamares debe permitir crear credenciales nuevas para la instalación.

Idioma y distribución de teclado deben configurarse de forma explícita y permitir cambios durante la sesión y la instalación.

## 4. Arquitectura de construcción

- Utilizar Debian Live-Build de Debian 13 para construir el sistema de archivos Live.
- Mantener la configuración en `auto/config`, listas de paquetes en `config/package-lists/`, archivos del sistema en `config/includes.chroot/` y hooks pequeños, idempotentes y verificables en `config/hooks/`.
- No ejecutar servicios de sistema durante la construcción; solo habilitarlos/configurarlos para el primer arranque cuando sea necesario.
- No descargar binarios opacos sin versión ni instalar software desde scripts remotos sin verificación.
- Fijar versiones o fuentes reproducibles cuando corresponda y guardar logs de construcción.
- Calamares debe instalar el sistema Live al destino. La configuración de Calamares y la configuración de Live-Build deben probarse juntas; instalar el paquete Calamares por sí solo no basta.

## 5. Estructura de repositorio objetivo

```text
.
├── .github/workflows/build-iso.yml
├── auto/
│   ├── config
│   ├── build
│   └── clean
├── config/
│   ├── package-lists/
│   │   ├── sistema-base.list.chroot
│   │   ├── escritorio.list.chroot
│   │   ├── hardware-firmware.list.chroot
│   │   ├── aplicaciones.list.chroot
│   │   └── instalador-calamares.list.chroot
│   ├── hooks/normal/
│   └── includes.chroot/
│       ├── etc/calamares/
│       ├── etc/skel/
│       └── usr/share/
├── docs/
│   ├── ARQUITECTURA-TECNICA.md
│   └── PLAN-DE-PRUEBAS.md
└── README.md
```

Esta es una estructura objetivo, no una afirmación de que todos esos archivos ya existan.

## 6. Reglas de seguridad y calidad

- No incluir IA ni servicios relacionados.
- No usar contraseñas personales ni claves privadas en el repositorio.
- No habilitar inicio de sesión remoto por defecto.
- Mantener privilegios mínimos y pedir contraseña para operaciones administrativas.
- Validar firmas y repositorios APT oficiales.
- Mantener firmware y controladores bajo las condiciones de sus licencias.
- No afirmar compatibilidad universal de hardware.
- No publicar como estable una ISO que no haya superado las pruebas.

## 7. Puertas de validación obligatorias

**Puerta A — configuración:** sintaxis shell, opciones reales de Live-Build, rutas, permisos y nombres de paquetes existentes en Debian 13.

**Puerta B — resolución de paquetes:** ejecutar la resolución APT en el entorno Trixie objetivo; ningún paquete ausente o conflicto sin resolver.

**Puerta C — construcción:** Live-Build termina con código cero; artefacto ISO existe y el manifiesto registra la versión del sistema y paquetes.

**Puerta D — integridad:** verificar tipo de archivo, estructura ISO, checksum y presencia de kernel, initramfs, SquashFS, GRUB BIOS/UEFI y archivos de Calamares.

**Puerta E — arranque:** probar BIOS y UEFI en máquinas virtuales; comprobar sesión Live, XFCE, red, audio virtual y apagado/reinicio.

**Puerta F — instalación:** ejecutar Calamares de principio a fin sobre disco virtual vacío; comprobar particionado, instalación del cargador, primer arranque desde disco, usuario, red y actualización.

**Puerta G — hardware:** probar en equipos reales representativos. Registrar modelo de dispositivo, controlador, firmware y resultado.

## 8. Criterio de entrega

La entrega solo puede llamarse **ISO candidata** si A–F pasan y los logs y SHA256 están disponibles. Solo puede llamarse **estable** después de pruebas reales de hardware y resolución de defectos críticos.

La ISO final debe ser un único archivo descargable, acompañado por su SHA256, manifiesto de paquetes, versión y notas de publicación. Los archivos fuente permanecerán organizados en GitHub; no se entregarán como sustituto de la ISO.

## 9. Pendientes antes de implementación

- Auditar cada archivo existente y evitar duplicados.
- Confirmar la configuración de usuario Live de la guía original.
- Verificar disponibilidad exacta de paquetes de firmware y Calamares en Debian 13 amd64.
- Diseñar y probar los módulos Calamares necesarios para la instalación del sistema Live.
- Revisar la estrategia BIOS/UEFI de Live-Build con la versión instalada en el runner.
- Definir matriz de pruebas de VM y hardware.
