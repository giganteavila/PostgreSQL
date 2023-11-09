[En](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TABLE) el [cuadro 9.33](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TABLE) se indican las funciones disponibles para el procesamiento de la  fecha/precio, con detalles que aparecen en las subsecciones siguientes. [La Tabla 9.32](https://www.postgresql.org/docs/current/functions-datetime.html#OPERATORS-DATETIME-TABLE) ilustra los comportamientos de los operadores de aritmética básica (`+`, `*`, etc.). Para las funciones de formatización, véase [la sección 9.](https://www.postgresql.org/docs/current/functions-formatting.html)8. Usted debe estar familiarizado con la información de antecedentes sobre los tipos de datos fecha/hora de la [Sección 8](https://www.postgresql.org/docs/current/datatype-datetime.html).5.

Además, los operadores de comparación habituales que se muestran en el  están disponibles para los tipos de fecha/hora. Las fechas y marcas  (con o sin huso horario) son comparables, mientras que los tiempos (con o sin zona horaria) y los intervalos sólo pueden compararse con otros  valores del mismo tipo de datos. Al comparar una marca de tiempo sin  zona horaria con una marca de tiempo con huso horario, se supone que el  valor anterior se da en el huso horario especificado por el parámetro de configuración [de TimeZone](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TIMEZONE), y se gira a UTC para compararlo con el segundo valor (que ya está en  UTC internamente). Del mismo modo, se supone que un valor de fecha  representa la medianoche en el  `TimeZone`zona al compararlo con una marca de tiempo.

Todas las funciones y operadores descritos a continuación que se llevan  `time`o o  `timestamp`entradas en realidad vienen en dos variantes: una que toma  `time with time zone`o o `timestamp with time zone`, y uno que toma  `time without time zone`o o `timestamp without time zone`. Para la brevedad, estas variantes no se muestran por separado. También, el  `+`y  `*`los operadores vienen en parejas conmutadoras (por ejemplo, ambos    `date``+``integer`y   `integer``+``date`); sólo mostramos uno de cada uno de esos pares.

**Cuadro 9.32. Operadores de fechas/ohora**

| Operadora              Descripción              Ejemplos (s) |
| ------------------------------------------------------------ |
| `date``+``integer`- `date`              Añadir varios días a una fecha               `date '2001-09-28' + 7`- |
| `date``+``interval`- `timestamp`              Añadir un intervalo a una fecha               `date '2001-09-28' + interval '1 hour'`- |
| `date``+``time`- `timestamp`              Añadir un tiempo de día a una fecha               `date '2001-09-28' + time '03:00'`- |
| `interval``+``interval`- `interval`              Añadir intervalos               `interval '1 day' + interval '1 hour'`- |
| `timestamp``+``interval`- `timestamp`              Añadir un intervalo a una marca de tiempo               `timestamp '2001-09-28 01:00' + interval '23 hours'`- |
| `time``+``interval`- `time`              Añadir un intervalo a una hora               `time '01:00' + interval '3 hours'`- |
| `-``interval`- `interval`              Negate un intervalo               `- interval '23 hours'`- |
| `date``-``date`- `integer`              Resta las fechas, produciendo el número de días transcurridos               `date '2001-10-01' - date '2001-09-28'`- |
| `date``-``integer`- `date`              Resta varios días a partir de una fecha               `date '2001-10-01' - 7`- |
| `date``-``interval`- `timestamp`              Resta un intervalo de una fecha               `date '2001-09-28' - interval '1 hour'`- |
| `time``-``time`- `interval`              Tiempos de sutracción               `time '05:00' - time '03:00'`- |
| `time``-``interval`- `time`              Resta un intervalo de un tiempo               `time '05:00' - interval '2 hours'`- |
| `timestamp``-``interval`- `timestamp`              Resta un intervalo de una marca de tiempo               `timestamp '2001-09-28 23:00' - interval '23 hours'`- |
| `interval``-``interval`- `interval`              Inter intervalos de sutracción               `interval '1 day' - interval '1 hour'`- |
| `timestamp``-``timestamp`- `interval`              Sutembres de tiempo (convertir intervalos de 24 horas en días, de manera similar a `justify_hours()`)               `timestamp '2001-09-29 03:00' - timestamp '2001-07-27 12:00'`- |
| `interval``*``double precision`- `interval`              Multiply un intervalo por un escalar               `interval '1 second' * 900`-                `interval '1 day' * 21`-                `interval '1 hour' * 3.5`- |
| `interval``/``double precision`- `interval`              Divide un intervalo por un escalar               `interval '1 hour' / 1.5`- |

**Cuadro 9.33. Fecha/Funciona las funciones del tiempo**

| Función              Descripción              Ejemplos (s)   |
| ------------------------------------------------------------ |
| `age`( `timestamp`,  `timestamp`) . `interval`              Resta los argumentos, produciendo un symbolicresultado simbólico que utiliza años y meses, en lugar de sólo días               `age(timestamp '2001-04-10', timestamp '1957-06-13')`- |
| `age`(  `timestamp`) .               Sustracto desactivar de  `current_date`(a medianoche)               `age(timestamp '1957-06-13')`- |
| `clock_timestamp`() `timestamp with time zone`              Fecha y hora actuales (cambios durante la ejecución de la declaración); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `clock_timestamp()`- |
| `current_date`- `date`              Fecha actual; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `current_date`- |
| `current_time`- `time with time zone`              Hora actual del día; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `current_time`- |
| `current_time`(  `integer`) .               Hora actual del día, con precisión limitada; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `current_time(2)`- |
| `current_timestamp`- `timestamp with time zone`              Fecha y hora actuales (inicio de la transacción actual); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `current_timestamp`- |
| `current_timestamp`(  `integer`) .               Fecha y hora actuales (inicio de la transacción actual), con precisión limitada; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `current_timestamp(0)`- |
| `date_add`( `timestamp with time zone`,  `interval`[,  `text`] . `timestamp with time zone`              Añadir un  `interval`a a `timestamp with time zone`, horas de comcomputación de ajustes de ahorro de luz diurna de acuerdo  con el huso horario nombrado por el tercer argumento, o la configuración actual [de TimeZone](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TIMEZONE) si se omite. La forma con dos argumentos es equivalente a la    `timestamp with time zone``+``interval`operador.               `date_add('2021-10-31 00:00:00+02'::timestamptz, '1 day'::interval, 'Europe/Warsaw')`- |
| `date_bin`( `interval`, `timestamp`,  `timestamp`) .               Entrada de la papel en el intervalo especificado alineado con el origen especificado; véase [la sección 9.9.3](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-BIN)               `date_bin('15 minutes', timestamp '2001-02-16 20:38:40', timestamp '2001-02-16 20:05:00')`- |
| `date_part`( `text`,  `timestamp`) . `double precision`              Obsúre el subcampo de marca de tiempo (equivalente a `extract`); véase [la sección 9.9.1](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)               `date_part('hour', timestamp '2001-02-16 20:38:40')`- |
| `date_part`( `text`,  `interval`) .               Obste subcampo de intervalo (equivalente a `extract`); véase [la sección 9.9.1](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)               `date_part('month', interval '2 years 3 months')`- |
| `date_subtract`( `timestamp with time zone`,  `interval`[,  `text`] . `timestamp with time zone`              Sustrador  `interval`de a `timestamp with time zone`, horas de comcomputación de ajustes de ahorro de luz diurna de acuerdo  con el huso horario nombrado por el tercer argumento, o la configuración actual [de TimeZone](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-TIMEZONE) si se omite. La forma con dos argumentos es equivalente a la    `timestamp with time zone``-``interval`operador.               `date_subtract('2021-11-01 00:00:00+01'::timestamptz, '1 day'::interval, 'Europe/Warsaw')`- |
| `date_trunc`( `text`,  `timestamp`) . `timestamp`              Truncate a precisión especificada; véase [la Sección 9.9.2](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC)               `date_trunc('hour', timestamp '2001-02-16 20:38:40')`- |
| `date_trunc`( `text`, `timestamp with time zone`,  `text`) .               Truncate a precisión especificada en el huso horario especificado; véase [la sección 9.9.2](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC)               `date_trunc('day', timestamptz '2001-02-16 20:38:40+00', 'Australia/Sydney')`- |
| `date_trunc`( `text`,  `interval`) .               Truncate a precisión especificada; véase [la Sección 9.9.2](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-TRUNC)               `date_trunc('hour', interval '2 days 3 hours 40 minutes')`- |
| `extract`(    *`field`*`from``timestamp`) . `numeric`              Obsúbese de tiempoampeado de subcampo; vea [Sección 9.9.1](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)               `extract(hour from timestamp '2001-02-16 20:38:40')`- |
| `extract`(    *`field`*`from``interval`) . `numeric`              Obste subcampo del intervalo; vea [Sección 9.9.1](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-EXTRACT)               `extract(month from interval '2 years 3 months')`- |
| `isfinite`(  `date`) . `boolean`              Prueba de fecha finita (no/infinito)               `isfinite(date '2001-02-16')`- |
| `isfinite`(  `timestamp`) .               Prueba de la marca de tiempo finito (no/infinito)               `isfinite(timestamp 'infinity')`- |
| `isfinite`(  `interval`) .               Prueba para el intervalo finito (actualmente siempre true)               `isfinite(interval '4 hours')`- |
| `justify_days`(  `interval`) . `interval`              Ajuste de intervalo para que los períodos de tiempo de 30 días se representen como meses               `justify_days(interval '35 days')`- |
| `justify_hours`(  `interval`) . `interval`              Ajuste de los intervalos para que los períodos de tiempo de 24 horas se representen como días               `justify_hours(interval '27 hours')`- |
| `justify_interval`(  `interval`) . `interval`              Ajuste el intervalo de uso  `justify_days`y `justify_hours`, con ajustes adicionales de señal               `justify_interval(interval '1 mon -1 hour')`- |
| `localtime`- `time`              Hora actual del día; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `localtime`- |
| `localtime`(  `integer`) .               Hora actual del día, con precisión limitada; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `localtime(0)`- |
| `localtimestamp`- `timestamp`              Fecha y hora actuales (inicio de la transacción actual); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `localtimestamp`- |
| `localtimestamp`(  `integer`) .               Fecha y hora actuales (inicio de la transacción actual), con precisión limitada; véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `localtimestamp(2)`- |
| `make_date`(  *`year`*`int`,  *`month`*`int`,   *`day`*`int`) . `date`              Crear una fecha de los campos de año, mes y día (años negativos significan BC)               `make_date(2013, 7, 15)`- |
| `make_interval`( [   *`years`*`int`[,   *`months`*`int`[,   *`weeks`*`int`[,   *`days`*`int`[,   *`hours`*`int`[,   *`mins`*`int`[,   *`secs`*`double precision`]]]]]]]]]] ) `interval`              Crear intervalo de años, meses, semanas, días, horas,  minutos y segundos campos, cada uno de los cuales puede predeterminar a  cero               `make_interval(days => 10)`- |
| `make_time`(  *`hour`*`int`,  *`min`*`int`,   *`sec`*`double precision`) . `time`              Crear tiempo a partir de campos de hora, minuto y segundos               `make_time(8, 15, 23.5)`- |
| `make_timestamp`(  *`year`*`int`,  *`month`*`int`,  *`day`*`int`,  *`hour`*`int`,  *`min`*`int`,   *`sec`*`double precision`) . `timestamp`              Crear estampado de tiempo a partir de los campos año, mes, día, hora, minuto y segundos (los años negativos significan BC)               `make_timestamp(2013, 7, 15, 8, 15, 23.5)`- |
| `make_timestamptz`(  *`year`*`int`,  *`month`*`int`,  *`day`*`int`,  *`hour`*`int`,  *`min`*`int`,   *`sec`*`double precision`[,   *`timezone`*`text`] . `timestamp with time zone`              Cree estampado de tiempo con hundi/húngido a partir del año, mes, día, hora, minuto y segundo campos (los años negativos  significan BC). Si  *`timezone`*no se especifica, se utiliza el huso horario actual; los ejemplos asumen que el huso horario de la sesión es `Europe/London`               `make_timestamptz(2013, 7, 15, 8, 15, 23.5)`-                `make_timestamptz(2013, 7, 15, 8, 15, 23.5, 'America/New_York')`- |
| `now`() `timestamp with time zone`              Fecha y hora actuales (inicio de la transacción actual); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `now()`- |
| `statement_timestamp`() `timestamp with time zone`              Fecha y hora actuales (inicio de la presente declaración); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `statement_timestamp()`- |
| `timeofday`() `text`              Fecha y hora actuales (como `clock_timestamp`, pero como un  `text`en la [sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `timeofday()`- |
| `transaction_timestamp`() `timestamp with time zone`              Fecha y hora actuales (inicio de la transacción actual); véase [la sección 9.9.5](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT)               `transaction_timestamp()`- |
| `to_timestamp`(  `double precision`) . `timestamp with time zone`              Convertir Unaix epoch (segundos desde 1970-01-01 00:00:00-00) a marca de tiempo con hunidad               `to_timestamp(1284352323)`- |

 Además de estas funciones, el SQL  `OVERLAPS`Se admite a operador:

```
(start1, end1) OVERLAPS (start2, end2)
(start1, length1) OVERLAPS (start2, length2)
```

Esta expresión se produce verdadera cuando se superponen dos  períodos de tiempo (definidos por sus puntos finales), falsos cuando no  se superponen. Los endpoints se pueden especificar como pares de fechas, horarios o sellos de tiempo; o como fecha, hora o sello de tiempo  seguido de un intervalo. Cuando se proporciona un par de valores, el  comienzo o el final se puede escribir primero;  `OVERLAPS`toma automáticamente el valor anterior del par como el comienzo. Cada  período de tiempo se considera que representa el intervalo semiabierto     *`start`*`<=`*`time`*`<`*`end`*A menos que  *`start`*y  *`end`*son iguales en cuyo caso representa ese instante de una sola vez. Esto  significa, por ejemplo, que dos períodos de tiempo con sólo un punto  final en común no se superponen.

```
SELECT (DATE '2001-02-16', FECHA '2001-12-21') OVERLAPS
       (DATE '2001-10-30', FECHA '2002-10-30');
Resultado: 
trueSELECT (DATE '2001-02-16', INTERVAL '100 days') OVERLAPS
       (DATE '2001-10-30', FECHA '2002-10-30');
Resultado: 
falseSELECT (DATE '2001-10-29', FECHA '2001-10-30') OVERLAPS
       (DATE '2001-10-30', FECHA '2001-10-31');
Resultado: 
SELECT (DATE '2001-10-30', FECHA '2001-10-30') OVERLAPS
       (DATE '2001-10-30', FECHA '2001-10-31');
 
```

Al añadir un  `interval`valor a (o restando un  `interval`valor de) a  `timestamp`o o  `timestamp with time zone`valor, los meses, días y microsegundos campos de la  `interval`El valor se maneja a su vez. En primer lugar, un campo de campo no dentro  de meses o decrementa la fecha de la marca de tiempo por el número  indicado de meses, manteniendo el día del mes el mismo a menos que  pasara el final del nuevo mes, en cuyo caso se utiliza el último día de  ese mes. (Por ejemplo, el 31 de marzo más 1 mes se convierte en el 30 de abril, pero el 31 de marzo más 2 meses se convierte en mayo 31.) A  continuación, los días de los días avancen o decrepen la fecha de la  marca de tiempo por el número indicado de días. En estos dos pasos la  hora local del día se mantiene igual. Por último, si hay un campo de  microsegundos no cero, se añade o se resta literalmente. Cuando se hace  aritmética en un  `timestamp with time zone`valor en un huso horario que reconoce DST, esto significa que añadir o restar (digiera)  `interval '1 day'`no necesariamente tiene el mismo resultado que añadir o restar `interval '24 hours'`. Por ejemplo, con la zona horaria de sesión fijada en `America/Denver`:

```
de tiempo SELECT con zona horaria '2005-04-02 12:00-07' Intervalo '1 día';
Resultado: 
2005-04-03 12:00:00-06De la zona horaria de SELECT con zona horaria '2005-04-02 12:00-07' intervalo '24 horas';
Resultado: 
```

Esto sucede porque una hora se saltó debido a un cambio en el horario de verano en  `2005-04-03 02:00:00`en zona horaria `America/Denver`.

Tenga en cuenta que puede haber ambiguedad en el  `months`campo devuelto por  `age`porque los meses diferentes tienen diferentes números de días. El enfoque PostgreSQL utiliza el mes desde el principio de las dos fechas al calcular los meses parciales. Por ejemplo,  `age('2004-06-01', '2004-04-30')`utiliza abril para ceder `1 mon 1 day`, mientras que el uso de Mayo cedería  `1 mon 2 days`porque mayo tiene 31 días, mientras que abril tiene sólo 30.

La sutracción de fechas y marcas de tiempo también puede ser  compleja. Una forma conceptualmente simple de realizar la resta es  convertir cada valor en un número de segundos usando `EXTRACT(EPOCH FROM ...)`, entonces restar los resultados; esto produce el número de *segundos* entre los dos valores. Esto se ajustará para el número de días en cada  mes, cambios en la zona horaria y ajustes de horarios de verano.  Sutracción de los valores de fecha o de marca de horario con el`-`El operador devuelve el número de días (24 horas) y horas/minutos/segundos entre los valores, haciendo los mismos ajustes. El  `age`función devuelve años, meses, días y horas/minutos/segundos, realizando resta  de campo por campo y luego ajustando para valores de campo negativos.  Las siguientes consultas ilustran las diferencias en estos enfoques. Los resultados de la muestra se produjeron con `timezone = 'US/Eastern'`; hay un cambio de horario de verano entre las dos fechas utilizadas:

```postgresql
SELECT EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -
       EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00');
Result: 10537200.000000
SELECT (EXTRACT(EPOCH FROM timestamptz '2013-07-01 12:00:00') -
        EXTRACT(EPOCH FROM timestamptz '2013-03-01 12:00:00'))
        / 60 / 60 / 24;
Result: 121.9583333333333333
SELECT timestamptz '2013-07-01 12:00:00' - timestamptz '2013-03-01 12:00:00';
Result: 121 days 23:00:00
SELECT age(timestamptz '2013-07-01 12:00:00', timestamptz '2013-03-01 12:00:00');
Result: 4 mons
```