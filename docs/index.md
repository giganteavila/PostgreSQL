# PostgreSQL
## Qué es PostgreSQL?

PostgreSQL es un potente sistema de bases de datos de **código abierto** que utiliza y extiende el lenguaje SQL combinado con muchas características que almacenan y escalan las cargas de datos más complicadas. Los orígenes de PostgreSQL se remontan a **1986** como parte del proyecto [POSTGRES](https://www.postgresql.org/docs/current/history.html) en la Universidad de California en Berkeley y tiene más de 35 años de desarrollo activo en la plataforma central.

PostgreSQL se ha ganado una sólida reputación por su **arquitectura probada**, **fiabilidad**, **integridad de datos**, conjunto de **características robustas**, **extensibilidad** y la **dedicación de la comunidad** de código abierto detrás del software para ofrecer constantemente soluciones eficaces e innovadoras. PostgreSQL se ejecuta en [todos los principales sistemas operativos](https://www.postgresql.org/download/), ha sido [compatible](https://en.wikipedia.org/wiki/ACID) con [ACID](https://en.wikipedia.org/wiki/ACID) desde 2001, y tiene potentes complementos como el popular extensor de bases de datos geoespaciales [PostGIS](https://postgis.net/). No es de extrañar que PostgreSQL se haya convertido en la base de datos relacional de código abierto de elección para muchas personas y organizaciones.

[Empezar](https://www.postgresql.org/docs/current/tutorial.html) con el uso de PostgreSQL nunca ha sido más fácil: elige un proyecto que quieres construir, y deja que PostgreSQL almacene de forma segura y robusta tus datos.

## Por qué usar PostgreSQL?

PostgreSQL viene con [muchas características](https://www.postgresql.org/about/featurematrix/) destinadas a ayudar a los desarrolladores a construir aplicaciones, administradores para proteger la integridad de los datos y construir entornos tolerantes a fallos, y ayudarle a administrar sus datos sin importar el conjunto de datos tan grande o pequeño. Además de ser [de código libre y abierto](https://www.postgresql.org/about/license/), PostgreSQL es **muy extensible**. Por ejemplo, puede definir sus propios tipos de datos, construir funciones personalizadas, incluso escribir código de [diferentes lenguajes](https://www.postgresql.org/docs/current/xplang.html) de [programación](https://www.postgresql.org/docs/current/xplang.html) sin recompilar su base de datos.

PostgreSQL trata de ajustarse al [estándar SQL](https://www.postgresql.org/docs/current/features.html) donde tal conformidad no contradice las características tradicionales o podría conducir a malas decisiones arquitectónicas. Muchas de las características requeridas por el estándar SQL son compatibles, aunque a veces con una sintaxis o función ligeramente diferente. Se pueden esperar nuevos pasos hacia la conformidad con el tiempo. A partir de la versión 16 de septiembre de 2023, PostgreSQL se ajusta al menos a 170 de las 179 funciones obligatorias para la conformidad del núcleo SQL:2023. A partir de este escrito, ninguna base de datos relacional cumple con toda la conformidad con esta norma.

A continuación se muestra una lista no exhaustiva de varias características que se encuentran en PostgreSQL, se añaden más en cada [versión importante:](https://www.postgresql.org/developer/roadmap/)

- **Tipos de datos**
    - Primitivas: entero, numérico, cadena, booleano
    - Estructurado: Fecha/hora, Array, Range / Multirange, UUID
    - Documento: JSON/JSONB, XML, Clave-valor (Hstore)
    - Geometría: Punto, Línea, Círculo, Polígono
    - Personalizaciones: Composite, Tipos personalizados
- **Integridad de los datos**
    - UNIQUE, NO NULL
    - Claves primarias
    - Claves foráneas
    - Restricciones de exclusión
    - Explicit Locks, Advisory Locks
- **Concurrencia, Rendimiento**
    - Indización: Árbol B, Multicolumna, Expresiones, Partial
    - Indización avanzada: GiST, SP-Gist, KNN Gist, GIN, BRIN, Covering indexes, Bloom filters
    - Sofisticado planificador de consultas/optimizador, escaneos de solo índice, estadísticas multicolumna
    - Transacciones, Operaciones anidadas (a través de puntos de ahorro)
    - Control de concurrencia Multi-Versión (MVCC)
    - Paralelización de las consultas de lectura y la construcción de índices de árbol B
    - Particionado de tablas
    - Todos los niveles de aislamiento de las transacciones definidos en la norma SQL, incluyendo Serializable
    - Compilatión de expresiones Just-In-Time (JIT)
- **Fiabilidad, Recuperación de Desastres**
   - Write-ahead Logging (WAL)
   - Replication: Asynchronous, Synchronous, Logical
   - Point-in-time-recovery (PITR), active standbys
   - Tablespaces
- **Seguridad**
    - Autenticación: GSSAPI, SSPI, LDAP, SCRAM-SHA-256, Certificado, y más
    - Sistema de control de acceso robusto
    - Seguridad a nivel de columna y fila
    - La autenticación multifactor con certificados y un método adicional
- **Extensibilidad**
    - Funciones y procedimientos almacenados
    - Lenguajes procedurales: PL/pgSQL, Perl, Python y Tcl. Hay otros lenguajes disponibles a través de extensiones, por ejemplo. Java, JavaScript (V8), R, Lua y Rust
    - Constructores SQL/JSON y expresiones de ruta
    - Envoltorios de datos extranjeros: conéctese a otras bases de datos o flujos con una interfaz SQL estándar
    - Interfaz de almacenamiento personalizable para tablas
    - Muchas extensiones que proporcionan funcionalidad adicional, incluyendo PostGIS
- **Internacionalización, Búsqueda de Texto**
    - Apoyo a conjuntos internacionales de caracteres, por ejemplo, a través de las recopilaciones de la UCI
    - Cifras de casos insensibles e insensibles a los acentos
    - Búsqueda de texto completo

Hay muchas más características que se pueden descubrir en la [documentación](https://www.postgresql.org/docs/) PostgreSQL. Además, PostgreSQL es altamente extensible: muchas características, como los índices, tienen API definidas para que se pueda construir con PostgreSQL tus desafíos.

PostgreSQL ha demostrado ser altamente escalable tanto en la cantidad de datos que puede gestionar y en el número de usuarios concurrentes que puede acomodarse. Hay clústeres activos PostgreSQL en entornos de producción que manejan muchos terabytes de datos, y sistemas especializados que manejan petabytes.

## Alguna pregunta?

El primer lugar al que acudir para cualquier pregunta en PostgreSQL es su [documentación de renombre mundial](https://www.postgresql.org/docs/) que discute cómo usar PostgreSQL en profundidad.

También hay muchas **[listas de correo](https://www.postgresql.org/list/)** donde te puedes conectar y participar en la [comunidad](https://www.postgresql.org/community/). También hay muchos [eventos](https://www.postgresql.org/about/events/) y [grupos de usuarios locales](https://www.postgresql.org/community/user-groups/) donde te puedes conectar con otros usuarios de PostgreSQL.