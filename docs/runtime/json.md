# JSON

JSON lesen und schreiben ohne externe Libraries.

```moo
setze daten auf json_lesen('{"name": "Anna", "alter": 25}')
zeige daten["name"]                # "Anna"

setze text auf json_text(daten)
zeige text                         # '{"name": "Anna", "alter": 25}'
```

Englisch: `json_parse`, `json_string`.

## Listen und Dicts

```moo
setze obj auf {
    "benutzer": [
        {"name": "Anna", "punkte": 42},
        {"name": "Ben", "punkte": 17}
    ],
    "aktiv": wahr
}

zeige json_text(obj, indent=2)     # hübsch formatiert
```

## JSON laden und speichern

Kombiniert mit den Datei-Builtins:

```moo
setze inhalt auf datei_lesen("config.json")
setze config auf json_lesen(inhalt)

config["version"] = "0.2.0"
datei_schreiben("config.json", json_text(config, indent=2))
```

## Siehe auch

- [Beispiel: json_schema.moo](https://github.com/7blacky7/moo/blob/master/beispiele/json_schema.moo) — JSON-Schema-Validator in ~380 Zeilen moolang.
