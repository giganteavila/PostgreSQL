PostgreSQL proporciona varios tipos de índices: B-ár, Hash, GiST, SP-GiST, GIN, BRIN y la [floración de](https://www.postgresql.org/docs/current/bloom.html) extensión. Cada tipo de índice utiliza un algoritmo diferente que mejor se adapta a diferentes tipos de consultas. Por defecto, el  [`CREATE INDEX`](https://www.postgresql.org/docs/current/sql-createindex.html)El comando crea índices de árbol B, que se ajustan a las situaciones más  comunes. Los otros tipos de índice se seleccionan escribiendo la palabra clave  `USING`seguido por el nombre tipo índice. Por ejemplo, para crear un índice Hash:

```
CREATE INDEX  nameEn el  tableUSING HASH (column);
```