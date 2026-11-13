# tavo — Portafolio de diseño

**Autor: Octavio Rojas Sevilla**  
Diseño Gráfico Digital · Universidad La Salle, campus Condesa.

Portafolio personal con once proyectos en cinco categorías: marca y packaging, campañas, animación, modelado 3D y visualización de datos. El recorrido reúne presentación, formación, herramientas, experiencia, proyectos y contacto. Construido con HTML, CSS y JavaScript sin framework.

## Páginas publicadas

- [Portafolio](https://tavo1320.github.io/Itei-grupo-4/)
- [Muestra del sistema de diseño](https://tavo1320.github.io/Itei-grupo-4/design.html)

## Documentación de la entrega

- [DESIGN.md — tokens y reglas del sistema](DESIGN.md)
- [CV.md — arquitectura, navegación y contenido](CV.md)
- [Sistema de diseño en PDF](docs/Sistema-de-diseno-tavo.pdf)
- [Arquitectura de información en PDF](docs/Arquitectura-de-informacion-tavo.pdf)
- [Sistema de diseño editable en Word](docs/Sistema-de-diseno-tavo.docx)
- [Arquitectura de información editable en Word](docs/Arquitectura-de-informacion-tavo.docx)

## Relación entre las decisiones y el sitio

DESIGN.md contiene el front matter YAML y las ocho secciones de la especificación de Google. El front matter se escribe con sintaxis JSON, válida dentro de YAML. `scripts/build-tokens.py` deriva `tokens.css` de esos valores. Las dos páginas comparten colores, fuentes, espaciado, formas y estilos de componentes. `CV.md` describe el contenido implementado; `content.js` organiza las fichas de los once proyectos.

El rojo #D30B2D identifica las acciones y la selección. Big Shoulders Display se usa para títulos, Avenir Next para lectura cuando está instalada y JetBrains Mono para datos breves. El cuervo es la firma visual. Los proyectos conservan sus colores originales.

## Validación y consulta local

La herramienta oficial **@google/design.md 0.4.0** verificó estructura, referencias, contraste de componentes y colores usados: **0 errores y 0 advertencias**. El diagnóstico completo está en [VALIDACION.md](VALIDACION.md).

Con Node.js instalado: `npm install` y `npm run validate:design`. Para regenerar las variables: `npm run tokens`. Para consultar las páginas sin construir nada: `npm start` y abrir la dirección local que se muestra. También puede utilizarse cualquier servidor de archivos estáticos.

El sitio incluye navegación por teclado, foco visible, diálogo nativo, selección de categorías con estado accesible, pausa de animaciones y respeto por movimiento reducido. Los videos se reproducen por decisión de la persona y se pausan al cerrar el proyecto.

## Fuentes y materiales

Big Shoulders Display y JetBrains Mono se alojan en `assets/fonts` junto a sus licencias SIL Open Font License. Avenir Next no se redistribuye; se usa la instalación local y, en su ausencia, Avenir, Segoe UI o Arial. Las imágenes, videos y textos de los proyectos fueron proporcionados por el autor. Las marcas que aparecen pertenecen a sus titulares y se muestran dentro de trabajos académicos.

Entrega elaborada a partir de las decisiones del autor con asistencia de Codex. [Instrucciones del proyecto académico](https://gist.github.com/jonmircha/5840bd99dc3306654734ee0fc24a7125).
