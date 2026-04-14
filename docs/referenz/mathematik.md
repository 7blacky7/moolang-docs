# Mathematik

Numerische Stdlib-Funktionen der moolang-Laufzeit.

## Grundlagen

### `abs`

**Signatur**: `abs(x: Zahl) → Zahl`
**Zweck**: Absolutwert.

```moo
zeige abs(-5)   # 5
```

### `wurzel` / `sqrt`

**Signatur**: `wurzel(x: Zahl) → Zahl`
**Zweck**: Quadratwurzel.

```moo
zeige wurzel(16)   # 4
```

## Rundung

### `runde` / `round`

**Signatur**: `runde(x: Zahl) → Zahl`
**Zweck**: Rundet zur nächsten ganzen Zahl (kaufmännisch).

### `boden` / `floor`

**Signatur**: `boden(x: Zahl) → Zahl`
**Zweck**: Rundet ab (nächste ganze Zahl ≤ x).

Beispiel aus `beispiele/welten.moo`:
```moo
setze gx auf boden(spieler_x)
setze gz auf boden(spieler_z)
```

### `decke` / `ceil`

**Signatur**: `decke(x: Zahl) → Zahl`
**Zweck**: Rundet auf (nächste ganze Zahl ≥ x).

## Min / Max

### `min`

**Signatur**: `min(a, b) → Zahl`
**Zweck**: Kleinerer der beiden Werte.

### `max`

**Signatur**: `max(a, b) → Zahl`
**Zweck**: Größerer der beiden Werte.

Beispiel aus `beispiele/welten.moo`:
```moo
gib_zurück max(vmin, min(vmax, wert))
```

## Trigonometrie

### `sinus` / `sin`

**Signatur**: `sinus(x: Zahl) → Zahl`
**Zweck**: Sinus (Argument in Radianten).

### `cosinus` / `cos`

**Signatur**: `cosinus(x: Zahl) → Zahl`
**Zweck**: Kosinus (Argument in Radianten).

### `tangens` / `tan`

**Signatur**: `tangens(x: Zahl) → Zahl`
**Zweck**: Tangens.

### `atan2`

**Signatur**: `atan2(y, x) → Zahl`
**Zweck**: Arkustangens von `y/x` unter Berücksichtigung der Quadranten.

Beispiel aus `beispiele/welten.moo`:
```moo
setze spieler_x auf spieler_x + sinus(blick_winkel) * BEWEGUNG
setze spieler_z auf spieler_z + cosinus(blick_winkel) * BEWEGUNG
```

## Zufall

### `zufall` / `random`

**Signatur**: `zufall() → Zahl`
**Zweck**: Pseudozufallszahl zwischen 0.0 und 1.0.

```moo
setze r auf zufall()
wenn r < 0.5:
    zeige "klein"
```

Für kryptografisch sichere Zufallszahlen siehe `sichere_zufall` / `secure_random` in der Krypto-Referenz.
