# NovaLinux Zenkai OS — compilación de una sola ISO

## Integración real
La ISO final se construye con Debian 13 (Trixie), amd64 y live-build.
Todos los paquetes del sistema, XFCE, firmware/controladores disponibles,
Calamares, GameMode, MangoHud, Conky y sensores están declarados juntos en
`config/package-lists/novalinux-completo.list.chroot`.

El workflow exige que exista exactamente una lista de paquetes `.list.chroot`.
Live-build instala esa lista dentro del filesystem raíz del sistema Live y
genera una sola imagen `.iso` con el sistema integrado en
`/live/filesystem.squashfs`. No se generan ISOs separadas por componente.

Los archivos de `config/includes.chroot/` son personalizaciones de la raíz
del sistema (monitor, configuración y autoinicio). No son instaladores
independientes ni imágenes separadas: live-build los copia dentro del mismo
filesystem que termina empaquetado en la ISO.

## Componentes
- Debian 13 Trixie, kernel amd64, arranque Live híbrido.
- XFCE, LightDM, NetworkManager y Calamares.
- Firmware Debian no libre y firmware gráfico Intel/AMD disponible en Debian.
- GameMode, MangoHud, Mesa/Vulkan y utilidades de diagnóstico.
- Monitor Conky con CPU, RAM, sensores de temperatura disponibles, disco y red.

## Límites técnicos
- No existe un controlador universal. Los controladores se limitan al kernel,
  firmware y paquetes disponibles para el hardware soportado por Debian.
- La temperatura de GPU/ventiladores solo aparece cuando el controlador y el
  firmware exponen sensores al kernel.
- NVIDIA propietario y Steam/Proton quedan como instalación opcional para no
  imponer controladores específicos ni aumentar el tamaño base.
- La ISO amd64 no es compatible con equipos ARM ni con UEFI de 32 bits.

## Validación automática
GitHub Actions verifica que haya una única lista consolidada, comprueba los
scripts y construye una única ISO. Luego inspecciona el SquashFS extraído para
confirmar que contiene Calamares, Conky, GameMode, MangoHud y el lector de
sensores. La compilación debe finalizar en verde y la ISO todavía debe probarse
arrancando e instalando en una máquina virtual y en hardware real.
