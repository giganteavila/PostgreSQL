PostgreSQL diseña un *plan* de *consulta* para cada consulta que recibe. Elegir el plan adecuado para coincidir  con la estructura de consulta y las propiedades de los datos es  absolutamente crítico para el buen rendimiento, por lo que el sistema  incluye un *planificador* complejo que intenta elegir buenos planes. Puedes usar el  [`EXPLAIN`](https://www.postgresql.org/docs/current/sql-explain.html)comando para ver qué plan de consulta crea el planificador para cualquier  consulta. La lectura de planes es un arte que requiere cierta  experiencia para dominar, pero esta sección intenta cubrir lo básico.

Ejemplos en esta sección se extraen de la base de datos de pruebas de regresión después de hacer un `VACUUM ANALYZE`, utilizando 9,3 fuentes de desarrollo. Usted debe ser capaz de obtener  resultados similares si usted prueba los ejemplos usted mismo, pero sus  costos estimados y recuentos de filas pueden variar ligeramente porque `ANALYZE`Las estadísticas son muestras aleatorias más que exactas, y porque los  costos son inherentemente algo dependientes de la plataforma.

Los ejemplos utilizados `EXPLAIN`'s por defecto, texto, formato de salida, que es compacto y conveniente para que los humanos la lean. Si quieres alimentarte `EXPLAIN`'s salida a un programa para un análisis posterior, debe utilizar uno de  sus formatos de salida legibles por máquina (XML, JSON o YAML) en su  lugar.