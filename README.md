# Landing CV · tavo

**Autor:** Octavio Rojas Sevilla (tavo)

Este repositorio reúne el CV y portafolio de Octavio Rojas Sevilla y la referencia visual de su sistema de diseño. La página se adapta a móvil, tableta y escritorio y está construida con HTML, CSS y JavaScript sin frameworks. El contenido y la arquitectura se describen en [CV.md](CV.md), y la identidad visual —colores, tipografía, espaciado, formas y componentes— se define en [DESIGN.md](DESIGN.md). Incluye once proyectos organizados en cinco categorías, navegación móvil, filtros de proyectos, galerías y animaciones.

## Páginas publicadas

- [Landing del CV y portafolio](https://tavo1320.github.io/Itei-grupo-4/)
- [Sistema de diseño](https://tavo1320.github.io/Itei-grupo-4/design.html)

## Documentos

- [CV.md](CV.md)
- [DESIGN.md](DESIGN.md)
- [Arquitectura del CV y portafolio (PDF)](docs/Arquitectura-de-informacion-tavo.pdf)
- [Sistema de diseño (PDF)](docs/Sistema-de-diseno-tavo.pdf)

## Contenido del repositorio

- [`index.html`](index.html) — landing del CV y portafolio.
- [`design.html`](design.html) — referencia visual del sistema de diseño.
- [`styles.css`](styles.css) y [`personal.css`](personal.css) — estilos y adaptación a distintos tamaños de pantalla.
- [`tokens.css`](tokens.css) — variables de diseño derivadas de DESIGN.md.
- [`app.js`](app.js) y [`content.js`](content.js) — navegación, filtros, galerías y contenido de los proyectos.
- [`design.css`](design.css) y [`design.js`](design.js) — presentación e interacciones de la muestra del sistema.
- [`assets/`](assets/) — imágenes, videos, iconos y fuentes.
- [`docs/`](docs/) — documentos Word y PDF del proyecto.

## Cómo verlo localmente

Desde la carpeta del proyecto, inicia un servidor local:

```bash
python3 -m http.server 8765
```

Después visita [http://localhost:8765/](http://localhost:8765/) para ver el portafolio y [http://localhost:8765/design.html](http://localhost:8765/design.html) para consultar el sistema de diseño.

## Accesibilidad

La página incluye navegación por teclado, enlace para saltar al contenido, foco visible, textos alternativos y controles con nombres accesibles. Los filtros indican su selección mediante color y una marca de verificación. Las animaciones pueden pausarse y respetan la preferencia de movimiento reducido. Los videos tienen controles y se pausan al cerrar el proyecto. La validación oficial de DESIGN.md terminó con 0 errores y 0 advertencias; los pares de texto y fondo declarados cumplen el contraste mínimo AA de 4.5:1.
