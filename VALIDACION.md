# Validación del sistema y del portafolio

Revisión del 13 de noviembre de 2026.

## DESIGN.md

Se ejecutó el linter oficial **@google/design.md 0.4.0** sobre DESIGN.md. Resultado: **0 errores, 0 advertencias**. El resumen registra 9 colores, 9 escalas tipográficas, 3 niveles de redondeo, 16 valores de espaciado y 19 componentes.

La estructura y las referencias entre tokens son válidas. No se detectaron colores definidos sin uso. Los pares de texto y fondo declarados en componentes pasan el contraste AA de 4.5:1. Blanco sobre #D30B2D alcanza aproximadamente **5.45:1**; #595959 sobre blanco, **7.00:1**. #D9D9D9 sirve como división decorativa, no como color de lectura.

## Páginas web

Las dos páginas comparten fonts.css, tokens.css, styles.css y personal.css. Las variables de tokens.css se generan desde DESIGN.md mediante scripts/build-tokens.py. Se revisaron la presentación en escritorio y celular, la selección de categorías y la apertura y cierre del diálogo con teclado. La muestra tiene acciones demostrativas, selección accesible y pausa de animación.

El portafolio contiene once proyectos y cinco categorías. Los proyectos de campañas usan los carteles como portada. Marca y packaging y Campañas no muestran enlaces a Behance. Los cuatro proyectos indicados por el autor sí enlazan a sus entradas específicas. Las dos visualizaciones enlazan a sus experiencias publicadas.

Los videos tienen controles y carga inicial diferida; no se reproducen automáticamente. Los efectos decorativos respetan movimiento reducido y pueden pausarse desde el pie. La comprobación del linter describe los tokens y no equivale a una certificación integral WCAG del sitio.

## Documentos

Los dos Word se exportaron a PDF y se revisaron página por página. El sistema conserva las ocho secciones y una lista multinivel de valores; la arquitectura describe las secciones, contenidos, enlaces y comportamientos implementados. Los archivos originales de Downloads se conservan.

## Reproducir la revisión

Después de instalar las dependencias de package.json, ejecutar `npm run validate:design`. Para reconstruir las variables a partir del front matter: `npm run tokens`.
