# Pipitik

Sitio del taller de escultura. Portada roja, portafolio de 13 proyectos, páginas de detalle y equipo. HTML estático con CSS y JavaScript; sin dependencias de producción.

## Desarrollo

- `npm run build` genera las 16 páginas en `dist`.
- `npm run dev` sirve el sitio en `http://localhost:4173`.
- `data.mjs` contiene los proyectos, el orden de portada, las galerías, servicios y biografías.
- `public/assets` contiene las fotografías optimizadas, el logo y los retratos.
- `build.mjs` genera rutas independientes, metadatos, sitemap y página 404.

## Netlify

Repositorio `AlexKongMx/Pipitik`, rama `main`. Comando `npm run build`. Directorio de publicación `dist`. Configuración en `netlify.toml`. La carpeta `.netlify` queda excluida de git para mantener fuera la configuración local de vinculación.

## Criterios editoriales

- Seis proyectos en “Piezas que hablan” en portada. El catálogo incluye trece.
- Red Hulk, Hulk verde y el escudo del Capitán América comparten `/proyectos/hulk/`.
- Alien: Romulus, huevo y pasillo comparten `/proyectos/alien/`.
- Tron sustituye la repetición de Hulk en “Oficio en cada detalle”.
- Sin Star Wars, Predator ni Slimer.
- Equipo sin Instagram, LinkedIn ni enlaces sociales personales.
- Foto héroe seguida de una selección corta de fotografías por proyecto. Galerías ampliables con teclado.

## Recursos y contenidos por completar

- Lalo Moreno está incluido con biografía y retrato en blanco y negro basado en las fotografías identificadas por Alex.
- Archivo de propuestas AI: https://drive.google.com/drive/folders/1ZuxIALBi3Ut62YWTz_XCtNjIElAQuoue. Las imágenes autorizadas en la actualización visual están integradas; las demás permanecen disponibles para revisión.
- El pasillo de Alien ya tiene una fotografía; faltan las imágenes adicionales de proceso y la otra pieza que Alex mencionó.
- Joel: confirmar apellido, cargo y biografía. El CV cronológico sin firma de la carpeta no se ha atribuido a una persona.
- Validar las biografías resumidas y los textos de proyectos con el taller; no se han añadido créditos ni especificaciones no confirmados.
- Logo adaptado de la referencia existente, con acento rojo. Sustituir por el archivo original vectorial cuando esté disponible.
- Retratos en blanco y negro preparados a partir de fotografías del equipo mediante edición de imagen; conservar y revisar la identidad con el taller.
- Datos de contacto usados: correo y teléfono de dirección presentes en el CV de Ernesto.

## Validación

En Deploy Preview se generan rutas sin enlace `_preview-checks/360/`, `_preview-checks/390/`, `_preview-checks/700/` y `_preview-checks/1440/` para revisar la página dentro de un viewport real de ese ancho. No se generan en producción.

Revisar `npm run build`, rutas directas, seis tarjetas de portada, trece tarjetas del catálogo, imágenes, navegación móvil, lightbox y ausencia de desbordamiento horizontal.


## Actualización visual — 2026-10-08

Héroes autorizados por Alex: Hulk con foto real in situ; The Last of Us, Demogorgon, ballena, Blue Demon y Trono de Hierro con las propuestas AI seleccionadas. Mufasa recreado sobre el carro alegórico original, en Reforma frente al Ángel, usando referencias de instalación y construcción. Lalo tiene retrato AI basado en las fotos identificadas por Alex, con la misma dirección de fotografía del equipo.

Robin conserva su foto real en Bellas Artes: la nueva generación en esa ubicación fue rechazada por el generador. Tarjetas y héroes muestran la pieza completa; la portada ahora lleva texto sobre la imagen, alineado a la derecha en escritorio y móvil.


## Política de trabajo — 8 octubre 2026

Todos los cambios se revisan en Netlify Deploy Preview. **DO NOT PUSH TO MAIN** hasta que Alex lo indique explícitamente; los pedidos de edición no autorizan publicar a producción. Ver `AGENTS.md`.

Tablero: https://trello.com/b/m2b9JcBy. Consultas y modificaciones exclusivamente mediante n8n, sin conector nativo de Trello. El flujo de creación quedó en el espacio personal de n8n y fue deshabilitado después de crear el tablero.

Esta revisión usa el Hulk con el equipo en portada y conserva el Hulk en plaza dentro del proyecto. Tron muestra primero el stand promocional abierto; su tarjeta mantiene la toma cercana. Last of Us se recrea en una convención y Pinocho en un lobby de cine. Mufasa incorpora un letrero y entra a los seis destacados. Alien y los retratos se conservan.

Imágenes generadas con la herramienta integrada a partir de referencias del proyecto. Assets: `public/assets/the-last-of-us-hero-convention-ai.webp`, `public/assets/pinocho-hero-cinema-ai.webp`, `public/assets/mufasa-hero-reforma-title-ai.webp`. Direcciones de prompt: preservar la escultura de Last of Us y trasladar su stand a Comic-Con; preservar el busto, nariz y gráfica de Pinocho en un cine; preservar el carro de Mufasa en Reforma y agregar únicamente un letrero físico MUFASA. Estas propuestas no confirman ubicaciones históricas.

## Portada — imagen proporcionada por Alex

La portada usa `public/assets/studio-cover-alex-wide.jpg`, panorámica enviada por Alex el 9 de octubre (2048×877). Se conserva el archivo exacto. La foto llena todo el ancho sin franjas negras; `object-fit: cover` evita barras en pantallas anchas y bajas. El bloque de texto grande se coloca sobre la pared libre a la derecha, debajo del puño, con sombreado CSS suave. La portada cabe debajo del encabezado en el primer viewport de escritorio; móvil conserva foto panorámica, título y botón sobre ella.

El montaje Fal/manual anterior fue rechazado por Alex y ya no se muestra. `ops/cover-assets.json` y `ops/prepare-cover.py` conservan el historial de aquella prueba, no la portada actual. No generar ni retocar esta nueva fotografía. **DO NOT PUSH TO MAIN**.


### Galerías de proyectos

`galleries.mjs` contiene la selección revisada de vistas terminadas y fotos de proceso. `ops/gallery-selection.json` conserva las referencias del material original. Se usan miniaturas de 480 px para la cuadrícula y archivos de hasta 1920 px para el visor. Las galerías se recorren con los botones anterior/siguiente o las teclas de flecha; Escape cierra el visor y devuelve el foco a la miniatura. Cada proyecto termina con enlaces al proyecto anterior y siguiente, con su imagen. Cuando el material disponible no aporta más ángulos o etapas de calidad, la selección queda más corta.
