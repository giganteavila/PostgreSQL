Los tipos de datos geométricos representan objetos espaciales bidimensionales. [El cuadro 8.20](https://www.postgresql.org/docs/current/datatype-geometric.html#DATATYPE-GEO-TABLE) muestra los tipos geométricos disponibles en PostgreSQL.

**Cuadro 8.20. Tipos geométricos**

| Nombre    | Tamaño de almacenamiento | Descripción                         | Representación                      |
| --------- | ------------------------ | ----------------------------------- | ----------------------------------- |
| `point`   | 16 bytes                 | Punto en un avión                   | (x,y)                               |
| `line`    | 32 bytes                 | Línea infinita                      | A, B, C.                            |
| `lseg`    | 32 bytes                 | Segmento de línea de finito         | ((x1,y1),(x2,y2))                   |
| `box`     | 32 bytes                 | Caja rectangular                    | ((x1,y1),(x2,y2))                   |
| `path`    | 1617 de bytes            | Ruta cerrada (similar al polígono)  | ((x1,y1),...)                       |
| `path`    | 1617 de bytes            | Vía abierta                         | [(x1,y1),...]                       |
| `polygon` | 40-16n bytes             | Polígono (similar a la vía cerrada) | ((x1,y1),...)                       |
| `circle`  | 24 bytes                 | Círculo                             | "(x,y), r (punto de centro y radio) |

Un rico conjunto de funciones y operadores está disponible para  realizar diversas operaciones geométricas, como escalada, traducción,  rotación e determinaciones. Se explican en [la sección 9](https://www.postgresql.org/docs/current/functions-geometry.html).11.