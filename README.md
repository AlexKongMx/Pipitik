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

- Lalo Moreno ya está incluido en el equipo con una ficha de escultura y modelado. Pendiente retrato confirmado; se muestra un monograma temporal, sin atribuirle una fotografía de otra persona.
- Propuestas de imágenes héroe AI en revisión: https://drive.google.com/drive/folders/1ZuxIALBi3Ut62YWTz_XCtNjIElAQuoue. Mantener las fotografías actuales hasta que Alex elija las variantes.
- El pasillo de Alien ya tiene una fotografía; faltan las imágenes adicionales de proceso y la otra pieza que Alex mencionó.
- Joel: confirmar apellido, cargo y biografía. El CV cronológico sin firma de la carpeta no se ha atribuido a una persona.
- Validar las biografías resumidas y los textos de proyectos con el taller; no se han añadido créditos ni especificaciones no confirmados.
- Logo adaptado de la referencia existente, con acento rojo. Sustituir por el archivo original vectorial cuando esté disponible.
- Retratos en blanco y negro preparados a partir de fotografías del equipo mediante edición de imagen; conservar y revisar la identidad con el taller.
- Datos de contacto usados: correo y teléfono de dirección presentes en el CV de Ernesto.

## Validación

Revisar `npm run build`, rutas directas, seis tarjetas de portada, trece tarjetas del catálogo, imágenes, navegación móvil, lightbox y ausencia de desbordamiento horizontal.
