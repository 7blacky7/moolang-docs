# Datenbank

Eingebauter SQLite-Support, dazu Client-Libraries für MySQL, PostgreSQL und Redis in den Beispielen.

## SQLite

```moo
setze db auf db_verbinde("sqlite:///meine_daten.db")

db_ausführen(db, "CREATE TABLE IF NOT EXISTS nutzer (id INTEGER PRIMARY KEY, name TEXT)")
db_ausführen(db, "INSERT INTO nutzer (name) VALUES ('Anna')")

setze ergebnis auf db_abfrage(db, "SELECT * FROM nutzer")
für zeile in ergebnis:
    zeige zeile

db_schliessen(db)
```

Englisch: `db_connect`, `db_execute`, `db_query`, `db_close`.

## Prepared Statements

```moo
db_ausführen(db, "INSERT INTO nutzer (name, alter) VALUES (?, ?)", ["Ben", 30])
```

## Externe Datenbanken (Beispiele)

moolang bringt komplette Client-Implementierungen als Beispiele mit:

- [MySQL-Client](https://github.com/7blacky7/moo/blob/master/beispiele/mysql_client.moo) (~470 Zeilen)
- [Postgres-Client](https://github.com/7blacky7/moo/blob/master/beispiele/postgres_client.moo) (~420 Zeilen)
- [Redis-Client](https://github.com/7blacky7/moo/blob/master/beispiele/redis_client.moo) (~270 Zeilen)
- [Mini-SQL-Engine](https://github.com/7blacky7/moo/blob/master/beispiele/mini_sql.moo) — eigene SQL-Engine in moo (~595 Zeilen)
- [Mini-DB](https://github.com/7blacky7/moo/blob/master/beispiele/mini_db.moo) — key-value Store (~580 Zeilen)
