PostgreSQL tiene un rico conjunto de tipos de datos nativos disponibles para los usuarios. Los usuarios pueden añadir nuevos tipos a PostgreSQL usando el comando [CREATE TYPE](https://www.postgresql.org/docs/current/sql-createtype.html).

[En](https://www.postgresql.org/docs/current/datatype.html#DATATYPE-TABLE) el [cuadro 8.1](https://www.postgresql.org/docs/current/datatype.html#DATATYPE-TABLE) se indican todos los tipos de datos incorporados. La mayoría de los nombres alternativos que aparecen en la Aliasescolumna de  son los nombres utilizados internamente por  por razones históricas. Además, algunos tipos de uso interno o deprecación están disponibles, pero no se enumeran aquí.

**Cuadro 8.1. Tipos de datos**

| Nombre                                        | Alisas                       | Descripción                                                  |
| --------------------------------------------- | ---------------------------- | ------------------------------------------------------------ |
| `bigint`                                      | `int8`                       | Firieron ocho bytes enteros                                  |
| `bigserial`                                   | `serial8`                    | autoincrementado ocho bytes enteros                          |
| `bit [ (*`n`*) ]`                             |                              | cuerda de bit de longitud fija                               |
| `bit varying [ (*`n`*) ]`                     | `varbit [ (*`n`*) ]`         | cadena de bits de longitud variable                          |
| `boolean`                                     | `bool`                       | Booleano lógico (verdad/falso)                               |
| `box`                                         |                              | caja rectangular en un plano                                 |
| `bytea`                                       |                              | datos binarios (byte array-arregón de byte)                  |
| `character [ (*`n`*) ]`                       | `char [ (*`n`*) ]`           | cadena de caracteres de longitud fija                        |
| `character varying [ (*`n`*) ]`               | `varchar [ (*`n`*) ]`        | cadena de caracteres de longitud variable                    |
| `cidr`                                        |                              | Dirección de red IPv4 o IPv6                                 |
| `circle`                                      |                              | círculo en un avión                                          |
| `date`                                        |                              | fecha natural (año, mes, día)                                |
| `double precision`                            | `float8`                     | Número de punto flotante de doble precisión (8 bytes)        |
| `inet`                                        |                              | IPv4 o IPv6 dirección de host                                |
| `integer`                                     | `int`, `int4`                | Firieron a cuatro bytes enteros                              |
| `interval [ *`fields`* ] [ (*`p`*) ]`         |                              | lapso de tiempo                                              |
| `json`                                        |                              | datos JSON textual                                           |
| `jsonb`                                       |                              | Datos binarios de JSON, descompuestos                        |
| `line`                                        |                              | Línea infinita en un avión                                   |
| `lseg`                                        |                              | segmento de línea en un avión                                |
| `macaddr`                                     |                              | Dirección MAC (Media Access Control)                         |
| `macaddr8`                                    |                              | Dirección MAC (Media Access Control) (formato EUI-64)        |
| `money`                                       |                              | monto de la moneda                                           |
| `numeric [ (*`p`*, *`s`*) ]`                  | `decimal [ (*`p`*, *`s`*) ]` | números exacto de precisión seleccionable                    |
| `path`                                        |                              | ruta geométrica en un plano                                  |
| `pg_lsn`                                      |                              | Número de secuenciación de registro                          |
| `pg_snapshot`                                 |                              | instantánea de identificación de transacción a nivel de usuario |
| `point`                                       |                              | punto geométrico en un avión                                 |
| `polygon`                                     |                              | Vía geométrica cerrada en un avión                           |
| `real`                                        | `float4`                     | Número de punto flotante de precisión de una sola precisión (4 bytes) |
| `smallint`                                    | `int2`                       | Firman dos bytes enteros                                     |
| `smallserial`                                 | `serial2`                    | autoincrementando el número entero de dos bytes              |
| `serial`                                      | `serial4`                    | autoincrementa cuatro bytes en el integer                    |
| `text`                                        |                              | cadena de caracteres de longitud variable                    |
| `time [ (*`p`*) ] [ without time zone ]`      |                              | hora del día (sin zona horaria)                              |
| `time [ (*`p`*) ] with time zone`             | `timetz`                     | hora del día, incluida la zona horaria                       |
| `timestamp [ (*`p`*) ] [ without time zone ]` |                              | fecha y hora (sin zona horaria)                              |
| `timestamp [ (*`p`*) ] with time zone`        | `timestamptz`                | fecha y hora, incluida la zona horaria                       |
| `tsquery`                                     |                              | consulta de búsqueda de texto                                |
| `tsvector`                                    |                              | documento de búsqueda de texto                               |
| `txid_snapshot`                               |                              | instantánea de identificación de identificación de transacción a nivel de usuario (depretada; ver `pg_snapshot`) |
| `uuid`                                        |                              | identificador único universal                                |
| `xml`                                         |                              | Datos XML                                                    |

### Compatibilidad

Los siguientes tipos (o ortletes de ellos) se especifican por SQL: `bigint`, `bit`, `bit varying`, `boolean`, `char`, `character varying`, `character`, `varchar`, `date`, `double precision`, `integer`, `interval`, `numeric`, `decimal`, `real`, `smallint`,  `time`(con o sin hunidad temporal),  `timestamp`(con o sin hunidad temporal), `xml`.

Cada tipo de datos tiene una representación externa determinada por sus funciones de entrada y salida. Muchos de los tipos incorporados  tienen formatos externos obvios. Sin embargo, varios tipos son  exclusivos de PostgreSQL, como rutas geométricas, o tienen varios formatos posibles, como los  tipos de fecha y hora. Algunas de las funciones de entrada y salida no  son invertibles, es decir, el resultado de una función de salida podría  perder precisión en comparación con la entrada original.