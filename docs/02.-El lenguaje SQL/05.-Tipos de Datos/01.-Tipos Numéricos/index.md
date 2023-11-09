Los tipos numéricos consisten en números de dos, cuatro y ocho bytes, números de punto flotante de cuatro y ocho bytes, y decimales de  precisión seleccionable. [En](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-NUMERIC-TABLE) la tabla [8.2](https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-NUMERIC-TABLE) se enumeran los tipos disponibles.

**Cuadro 8.2. Tipos numéricos**

| Nombre             | Tamaño de almacenamiento | Descripción                                   | Rango                                                        |
| ------------------ | ------------------------ | --------------------------------------------- | ------------------------------------------------------------ |
| `smallint`         | 2 bytes                  | enseñado de gama pequeña                      | -32768 a 32767                                               |
| `integer`          | 4 bytes                  | elección típica para el entero                | -2147483648 a . . . . . . . . . . .                          |
| `bigint`           | 8 bytes                  | entero de gran alcance                        | -9223373686854775808 a .923372036854775707                   |
| `decimal`          | variable variable        | Precisión especificada por el usuario, exacta | hasta 131072 dígitos antes del punto decimal; hasta 16383 dígitos después del punto decimal |
| `numeric`          | variable variable        | Precisión especificada por el usuario, exacta | hasta 131072 dígitos antes del punto decimal; hasta 16383 dígitos después del punto decimal |
| `real`             | 4 bytes                  | de precisión variable, inexacta               | 6 dígitos decimales precisión                                |
| `double precision` | 8 bytes                  | de precisión variable, inexacta               | 15 dígitos decimales precisión                               |
| `smallserial`      | 2 bytes                  | pequeño autoincrementing entero               | 1 a 32767                                                    |
| `serial`           | 4 bytes                  | ente entero de autoincremento                 | 1 a 2147483647                                               |
| `bigserial`        | 8 bytes                  | gran autoincremento entero                    | 1 a 9223372036854775807                                      |

La sintaxis de constantes para los tipos numéricos se describe en [la Sección 4.1](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-CONSTANTS).2. Los tipos numéricos tienen un conjunto completo de operadores y funciones de aritmética correspondientes. Consulte el [capítulo 9](https://www.postgresql.org/docs/current/functions.html) para más información. En las siguientes secciones se describen los tipos en detalle.

### 