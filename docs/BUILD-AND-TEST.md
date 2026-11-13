# NovaLinux Zenkai OS — compilación y pruebas

## Base
Debian 13 (Trixie), arquitectura amd64, XFCE y live-build. La ISO se construye desde los repositorios oficiales de Debian; no se redistribuye ni se modifica una ISO propietaria/precompilada.

## Funciones incluidas en esta etapa
- XFCE y Calamares.
- Firmware Debian no libre habilitado en live-build.
- Herramientas gaming: GameMode y MangoHud.
- Monitor lateral Conky: CPU, RAM, temperaturas disponibles, disco y red.
- Herramientas Vulkan/Mesa para diagnóstico y aceleración gráfica.

## Limitaciones conocidas
- No existe un controlador universal: Intel, AMD y NVIDIA requieren paquetes y pruebas específicos.
- La temperatura de GPU y ventiladores solo aparece si el kernel/controlador expone sensores compatibles.
- FPS de MangoHud se muestra dentro de juegos compatibles, no como contador global.
- GameMode no garantiza más FPS; aplica optimizaciones compatibles cuando el juego lo solicita.
- Steam/Proton y controladores NVIDIA propietarios se mantienen como instalación opcional para no inflar la ISO ni forzar hardware específico.
- La ISO amd64 no arranca en equipos ARM ni en sistemas exclusivamente UEFI de 32 bits.

## Validación
GitHub Actions ejecuta preflight, construye la ISO, comprueba que exista el sistema squashfs y que Calamares, Conky, GameMode y MangoHud estén dentro de la imagen. Después publica la ISO y registros como artefactos. La compilación exitosa no sustituye pruebas de arranque e instalación en equipos físicos/VM.
