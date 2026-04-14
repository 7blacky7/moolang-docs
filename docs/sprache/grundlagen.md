# Sprach-Grundlagen

moolang ist **zweisprachig** — Deutsch und Englisch funktionieren beide. Diese Seite zeigt die Deutsch-Variante, darunter jeweils den englischen Alias.

## Variablen

```moo
setze x auf 5
setze name auf "Moritz"
```

Englisch: `set x to 5`

Konstanten (unveränderlich):

```moo
konstante PI auf 3.14159
```

Englisch: `const PI to 3.14159`

## Datentypen

| Typ | Beispiel |
|-----|----------|
| Zahl | `42`, `3.14`, `-7` |
| Text | `"Hallo"`, `'x'` |
| Boolean | `wahr`, `falsch` (`true`, `false`) |
| Nichts | `nichts` (`none`) |
| Liste | `[1, 2, 3]` |
| Dictionary | `{"a": 1, "b": 2}` |

## Bedingungen

```moo
wenn x > 10:
    zeige "groß"
sonst:
    zeige "klein"
```

Englisch: `if x > 10: ... else: ...`

## Schleifen

```moo
solange x < 100:
    setze x auf x + 1

für i in [1, 2, 3]:
    zeige i
```

Englisch: `while`, `for i in ...`

## Funktionen

```moo
funktion quadrat(n):
    gib_zurück n * n

zeige quadrat(7)   # 49
```

Englisch: `func quadrat(n): return n * n`

Mit Default-Werten:

```moo
funktion begrüße(name = "Welt"):
    zeige "Hallo " + name
```

Lambdas:

```moo
setze verdoppeln auf lambda(x): x * 2
zeige verdoppeln(5)   # 10
```

## Listen und Comprehensions

```moo
setze zahlen auf [1, 2, 3, 4, 5]
setze quadrate auf [n * n für n in zahlen]
setze gerade auf [n für n in zahlen wenn n % 2 == 0]
```

## Module

```moo
# mathe.moo
exportiere funktion sinus(x):
    # ...

# main.moo
aus mathe importiere sinus
zeige sinus(3.14)
```

Oder:

```moo
importiere mathe
zeige mathe.sinus(3.14)
```

## Klassen

```moo
klasse Punkt:
    funktion neu(selbst, x, y):
        selbst.x = x
        selbst.y = y

    funktion abstand(selbst, anderer):
        gib_zurück wurzel((selbst.x - anderer.x)**2 + (selbst.y - anderer.y)**2)

setze p auf neu Punkt(3, 4)
setze q auf neu Punkt(0, 0)
zeige p.abstand(q)   # 5.0
```

## Weiterlesen

Vollständiges Tutorial mit allen Themen (JSON, HTTP, Regex, Dateien, Kryptografie, Threads, 2D/3D-Grafik): [Tutorial](../tutorial.md).
