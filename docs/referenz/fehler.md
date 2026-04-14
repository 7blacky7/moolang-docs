# Fehlerbehandlung

## Was ist das?

Wenn während der Programmausführung etwas **schief geht** (z.B. Datei nicht gefunden, Division durch Null, ungültige Eingabe), braucht es eine Möglichkeit, den Fehler aus der Tiefe eines Funktionsaufrufs nach oben zu transportieren, ohne jedem Rückgabewert einen Fehlerfall anzuhängen. moolang bietet dafür **Exceptions** — analog zu Python `try/except`, JavaScript `try/catch` oder Rust `panic!`.

Grundidee: Mit `wirf <wert>` löst man einen Fehler aus. Mit `versuche: ... fange name: ...` fängt man ihn auf einer höheren Ebene ab. Als Alternative für erwartbare Fehler (z.B. Parsen) siehe den **Result-Typ**.

## `wirf` / `throw`

**Signatur**: `wirf <ausdruck>`
**Zweck**: Löst einen Fehler aus. Der Wert kann beliebig sein (typisch: ein Text oder ein Dict mit Details).

```moo
funktion dividiere(a, b):
    wenn b == 0:
        wirf "Division durch Null"
    gib_zurück a / b
```

## `versuche` / `fange`

**Syntax**:
```moo
versuche:
    <try-block>
fange <name>:
    <catch-block>
```

**Zweck**: Führt den `versuche`-Block aus. Bei einem Fehler wird der Fehlerwert in `<name>` gebunden und der `fange`-Block ausgeführt.

```moo
versuche:
    setze ergebnis auf dividiere(10, 0)
    zeige ergebnis
fange fehler:
    zeige "Fehler: " + text(fehler)
```

## Fehler abfragen — `get_error` / `fehler_holen`

Innerhalb eines `fange`-Blocks ist der gefangene Wert bereits in der Bind-Variable (z.B. `fange fehler:`). Zusätzlich stellt die Laufzeit die Low-Level-Funktion `moo_get_error` bereit, die den letzten geworfenen Wert zurückgibt.

```moo
versuche:
    wirf {"code": 42, "msg": "Kaputt"}
fange err:
    zeige err["code"]
    zeige err["msg"]
```

## Hinweis zu Reservierten Namen

`versuche` ist ein *Soft-Keyword*: nur als Statement-Start direkt vor `:` wird es als Try-Block interpretiert. Als Variablen-/Funktionsname ist es weiterhin erlaubt.

`wirf` ist ein *hartes* Keyword und kann nicht als Bezeichner verwendet werden.
