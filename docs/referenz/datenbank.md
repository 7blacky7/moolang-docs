# Datenbank

SQLite-basierte DB-Builtins. Die Verbindungszeichenkette startet ueblicherweise mit `sqlite:///`.

## `db_verbinde` / `db_connect` / `dbv`

**Signatur**: `db_verbinde(url) → db`
**Zweck**: Oeffnet eine Datenbank-Verbindung (legt SQLite-Datei bei Bedarf an).

**Beispiel** (aus `beispiele/adressbuch.moo`):
```moo
setze db auf db_verbinde("adressbuch.db")
db_ausführen(db, "CREATE TABLE IF NOT EXISTS kontakte (id INTEGER PRIMARY KEY, name TEXT, email TEXT, telefon TEXT)")
```

## `db_ausführen` / `db_execute` / `dbe`

**Signatur**: `db_ausführen(db, sql) → nichts`
**Zweck**: Fuehrt ein SQL-Statement ohne Ergebnisrueckgabe aus (DDL, INSERT, UPDATE, DELETE).

**Beispiel** (aus `beispiele/adressbuch.moo`):
```moo
db_ausführen(db, "INSERT INTO kontakte (name, email, telefon) VALUES ('" + name + "', '" + email + "', '" + telefon + "')")
```

## `db_abfrage` / `db_query` / `dba`

**Signatur**: `db_abfrage(db, sql) → liste<liste>`
**Zweck**: Fuehrt ein SELECT aus und liefert die Ergebniszeilen als Liste.

**Beispiel** (aus `beispiele/adressbuch.moo`):
```moo
setze ergebnis auf db_abfrage(db, "SELECT id, name, email, telefon FROM kontakte ORDER BY name")
für zeile in ergebnis:
    zeige zeile
```

## `db_schliessen` / `db_close` / `dbs`

**Signatur**: `db_schliessen(db) → nichts`
**Zweck**: Schliesst die Verbindung und gibt Ressourcen frei.

**Beispiel** (aus `beispiele/adressbuch.moo`):
```moo
db_schliessen(db)
```
