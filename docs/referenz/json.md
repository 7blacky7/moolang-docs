# JSON

Builtins fuer JSON-Serialisierung und -Deserialisierung. Aliase sind in `compiler/src/codegen.rs` hinterlegt; jede Variante ruft denselben Runtime-Entrypoint auf.

## `json_lesen` / `json_parse` / `jp`

**Signatur**: `json_lesen(text) → wert`
**Zweck**: Parst einen JSON-String zu einem moo-Wert (Dict, Liste, Zahl, String, Boolean, nichts).

**Beispiel** (aus `beispiele/showcase.moo`):
```moo
setze json_str auf json_text({"sprache": "moo", "version": 3})
setze parsed auf json_lesen(json_str)
zeige f"Parsed: {parsed}"
```

## `json_text` / `json_string` / `js`

**Signatur**: `json_text(wert) → text`
**Zweck**: Serialisiert einen moo-Wert (Dict, Liste, Primitiv) zu einem JSON-String.

**Beispiel** (aus `beispiele/showcase.moo`):
```moo
setze json_str auf json_text({"sprache": "moo", "version": 3})
zeige f"JSON: {json_str}"
```
