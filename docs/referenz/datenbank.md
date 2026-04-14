# Datenbank

## Was ist das?

Eine Datenbank (Database, DB, RDBMS) speichert strukturierte Daten in Tabellen mit Spalten und Zeilen und erlaubt Abfragen ueber SQL (Structured Query Language). moo benutzt darunter SQLite — eine eingebettete, serverlose Datenbank, die einfach eine Datei auf der Platte ist. Damit lassen sich kleine Anwendungen, Tools und Prototypen ohne separaten DB-Server bauen.

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

## `db_abfrage_mit_params` / `db_query_with_params`

**Signatur**: `db_abfrage_mit_params(db, sql, params_liste) → liste<dict>`
**Zweck**: Wie `db_abfrage`, aber SQL darf `?`-Platzhalter enthalten; die
`params_liste` wird positional gebunden (1-based). Das ist der **empfohlene
Weg**, um Nutzer-Eingaben in Queries einzubauen — Parameter-Binding verhindert
SQL-Injection auf C-Ebene (sqlite3_bind_*), ohne dass Strings manuell escaped
werden muessen.

Typ-Mapping: Ganzzahlen → `INTEGER`, Kommazahlen → `REAL`, Strings → `TEXT`,
`nichts` → `NULL`, Boolean → `INTEGER` (0/1), alles andere wird als JSON-Text
gebunden.

**Beispiel** (verifiziert, `/tmp/moo-verify/db_prep_1_basic.moo`):
```moo
setze r auf db_abfrage_mit_params(db, "SELECT id, name, age FROM u WHERE age > ?", [26])
zeige r
```

## `db_ausführen_mit_params` / `db_execute_with_params`

**Signatur**: `db_ausführen_mit_params(db, sql, params_liste) → zahl`
**Zweck**: Wie `db_ausführen`, aber mit `?`-Platzhaltern und Parameter-Binding.
Gibt die Anzahl betroffener Zeilen zurueck.

**Beispiel**:
```moo
setze n auf db_ausführen_mit_params(db,
    "INSERT INTO u (name, age) VALUES (?, ?)", ["Anna", 25])
zeige n
```

Injection-Sicher: selbst wenn der gebundene Wert wie SQL aussieht (`"'; DROP TABLE u; --"`),
wird er als Datentext in die Spalte geschrieben, nicht als SQL ausgefuehrt.

> **Hinweis**: `sql_bereinigen` (aus [Kryptografie](krypto.md)) bleibt funktional, ist
> aber ab sofort **deprecated** fuer neuen Code — Prepared-Statements via
> `db_*_mit_params` sind der sichere Weg.

## `db_schliessen` / `db_close` / `dbs`

**Signatur**: `db_schliessen(db) → nichts`
**Zweck**: Schliesst die Verbindung und gibt Ressourcen frei.

**Beispiel** (aus `beispiele/adressbuch.moo`):
```moo
db_schliessen(db)
```
