# Stdlib-Module

Zusätzlich zu den eingebauten Laufzeit-Funktionen liefert moolang mehrere Stdlib-Module als `.moo`-Dateien unter `stdlib/`. Import per `importiere <modul>`.

## `importiere mathe`

Quelle: `stdlib/mathe.moo`.

| Funktion | Signatur | Zweck |
|---|---|---|
| `fakultaet(n)` | `(Zahl) → Zahl` | Fakultät `n!` (rekursiv). |
| `fibonacci(n)` | `(Zahl) → Zahl` | `n`-te Fibonacci-Zahl (iterativ). |
| `ist_gerade(n)` | `(Zahl) → Bool` | `n % 2 == 0`. |
| `ggt(a, b)` | `(Zahl, Zahl) → Zahl` | Größter gemeinsamer Teiler. |
| `ist_primzahl(n)` | `(Zahl) → Bool` | Primzahl-Test (Trial Division). |
| `klemme(wert, lo, hi)` | `(Zahl, Zahl, Zahl) → Zahl` | Klemmt `wert` in das Intervall `[lo, hi]`. |
| `lerp(a, b, t)` | `(Zahl, Zahl, Zahl) → Zahl` | Lineare Interpolation. |

```moo
importiere mathe
zeige fakultaet(10)
zeige fibonacci(20)
zeige ggt(48, 18)
zeige klemme(150, 0, 100)
zeige lerp(0, 100, 0.5)
```

## `importiere liste`

Quelle: `stdlib/liste.moo`.

| Funktion | Signatur | Zweck |
|---|---|---|
| `summe(l)` | `(Liste<Zahl>) → Zahl` | Summe aller Elemente. |
| `produkt(l)` | `(Liste<Zahl>) → Zahl` | Produkt aller Elemente. |
| `minimum(l)` | `(Liste<Zahl>) → Zahl` | Kleinstes Element. |
| `maximum(l)` | `(Liste<Zahl>) → Zahl` | Größtes Element. |
| `flach_machen(l)` | `(Liste<Liste>) → Liste` | Flacht verschachtelte Liste um eine Ebene ab. |
| `eindeutig(l)` | `(Liste) → Liste` | Entfernt Duplikate (erhält Reihenfolge). |

```moo
importiere liste
zeige summe([1,2,3,4,5])
zeige maximum([3,7,2,9,1])
zeige eindeutig([1,2,2,3,3,3])
```

## `importiere text`

Quelle: `stdlib/text.moo`.

| Funktion | Signatur | Zweck |
|---|---|---|
| `wiederhole(t, n)` | `(Text, Zahl) → Text` | Wiederholt `t` `n`-mal. |
| `ist_leer(t)` | `(Text) → Bool` | Wahr, wenn `länge(t) == 0`. |

```moo
importiere text
zeige wiederhole("ab", 3)   # "ababab"
zeige ist_leer("")          # wahr
```

## `importiere primzahl`

Quelle: `stdlib/primzahl.moo`. Primzahl-spezifische Helfer (teilweise überlappend mit `mathe`).

| Funktion | Signatur | Zweck |
|---|---|---|
| `ist_primzahl(n)` | `(Zahl) → Bool` | Primzahl-Test. |
| `ggt(a, b)` | `(Zahl, Zahl) → Zahl` | Größter gemeinsamer Teiler. |
| `klemme(wert, lo, hi)` | `(Zahl, Zahl, Zahl) → Zahl` | Wert klemmen. |
