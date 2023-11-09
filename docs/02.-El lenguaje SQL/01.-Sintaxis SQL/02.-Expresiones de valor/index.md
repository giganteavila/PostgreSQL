 Las expresiones de valor se utilizan en una variedad de contextos, como en la lista de destino de la  `SELECT`comando, como nuevos valores de columna en  `INSERT`o o `UPDATE`, o en condiciones de búsqueda en una serie de comandos. El resultado de una expresión de valor se llama a veces un *escalar*, para distinguirlo del resultado de una expresión de tabla (que es una  tabla). Por lo tanto, las expresiones de valor también se llaman *expresiones escalaras* (o incluso simplemente *expresiones*). La sintaxis de la expresión permite el cálculo de valores de partes  primitivas usando aritmética, lógica, configuración y otras operaciones.

Una expresión de valor es una de las siguientes:

- Un valor constante o literal
- Una columna de referencia
- Una referencia de parámetros posicionales, en el cuerpo de una definición de función o declaración preparada
- Una expresión subscripti
- Una expresión de selección de campo
- Una invocación de operador
- Una llamada de función
- Una expresión agregada
- Llama de función de ventana
- Un elenco tipo
- Una expresión de cotejar
- Una subecuencia escalar
- Un constructor de matrices
- Un constructor de filas
- Otra expresión de valor entre paréntesis (utilizada para las subexpresiones de grupo y sobrediferencia)

Además de esta lista, hay una serie de construcciones que pueden  clasificarse como una expresión pero no siguen ninguna regla general de  sintaxis. Estos generalmente tienen la semántica de una función u  operador y se explican en la ubicación apropiada en [el capítulo](https://www.postgresql.org/docs/current/functions.html) 9. Un ejemplo es el  `IS NULL`cláusula.

Ya hemos discutido las constantes en [la sección 4.1](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-CONSTANTS).2. En las secciones siguientes se examinan las opciones restantes.
