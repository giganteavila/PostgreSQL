PostgreSQL soporta el conjunto completo de  SQLlos tipos de fecha y hora, que se muestran en la [Tabla 8.](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-DATETIME-TABLE)9. Las operaciones disponibles en estos tipos de datos se describen en [la sección 9.](https://www.postgresql.org/docs/current/functions-datetime.html)9. Las fechas se cuentan según el calendario gregoriano, incluso en años antes de que se introdujo ese calendario (ver [Sección B.6](https://www.postgresql.org/docs/current/datetime-units-history.html) para más información).

**Cuadro 8.9. Tipos de fecha/tiempo**

| Nombre                                        | Tamaño de almacenamiento | Descripción                                    | Bajo valor      | Alto valor     | Resolución     |
| --------------------------------------------- | ------------------------ | ---------------------------------------------- | --------------- | -------------- | -------------- |
| `timestamp [ (*`p`*) ] [ without time zone ]` | 8 bytes                  | tanto la fecha como la hora (sin zona horaria) | 4713 BC         | 294276 dC      | 1 microsegundo |
| `timestamp [ (*`p`*) ] with time zone`        | 8 bytes                  | tanto la fecha como la hora, con huso horario  | 4713 BC         | 294276 dC      | 1 microsegundo |
| `date`                                        | 4 bytes                  | fecha (sin hora del día)                       | 4713 BC         | 5874897 dC     | 1 día          |
| `time [ (*`p`*) ] [ without time zone ]`      | 8 bytes                  | hora del día (sin fecha)                       | 00:00 horas     | 24:00 horas    | 1 microsegundo |
| `time [ (*`p`*) ] with time zone`             | 12 bytes                 | hora del día (sin fecha), con zona horaria     | 00:00.1559      | 24:00 a 1559   | 1 microsegundo |
| `interval [ *`fields`* ] [ (*`p`*) ]`         | 16 bytes                 | intervalos de tiempo                           | -178000000 años | 178000000 años | 1 microsegundo |

### Nota

El estándar SQL requiere que la escritura sea sólo  `timestamp`ser equivalente a `timestamp without time zone`, y PostgreSQL honra ese comportamiento.  `timestamptz`es aceptado como una abreviatura de `timestamp with time zone`; esta es una extensión de PostgreSQL.

`time`, `timestamp`, y  `interval`aceptar un valor de precisión opcional  *`p`*que especifica el número de dígitos fraccionados retenidos en el campo de  segundos. Por defecto, no hay un límite explícito de precisión. El rango permitido de  *`p`*es de 0 a 6.

El  `interval`tipo tiene una opción adicional, que consiste en restringir el conjunto de campos almacenados escribiendo una de estas frases:

```
YEAR
MONTH
DIA
NUESTRO
MINUTE
SEGUNDO
A los meses
DIA a HOUR
Día para MINUTE
Día para SEGUNDO
HORA A MINUTE
HORA SEGUNDO
MINUTE A SEGUNDO
```

Tenga en cuenta que si ambos  *`fields`*y  *`p`*se especifican, la  *`fields`*debe incluir `SECOND`, ya que la precisión se aplica sólo a los segundos.

El tipo  `time with time zone`se define por la norma SQL, pero la definición muestra propiedades que  conducen a una utilidad cuestionable. En la mayoría de los casos, una  combinación de `date`, `time`, `timestamp without time zone`, y  `timestamp with time zone`debe proporcionar un rango completo de funcionalidad fecha/hora requerido por cualquier aplicación.