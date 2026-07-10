# Tensoren & Autograd

## Was ist das?

Tensoren sind mehrdimensionale Zahlenfelder — die Grundbausteine jeder KI-Berechnung. moo bringt sie als eingebauten Typ mit: Operatoren (`+ - * / ** -`), Matrix-Multiplikation, Reduktionen und Aktivierungsfunktionen, alles DE/EN gleichwertig. Dazu kommt **Autograd**: ein dynamisches Band (Tape) zeichnet Berechnungen auf und liefert per `rueckwaerts()` automatisch alle Ableitungen — dieselbe Mechanik wie in PyTorch, nur eingebaut.

## Tensoren erzeugen

| Builtin (DE / EN) | Signatur | Zweck |
|---|---|---|
| `tensor_aus_liste` / `tensor_from_list` | `(liste) → tensor` | Aus (verschachtelter) Liste, z.B. `[[1,2],[3,4]]` |
| `tensor` | `(form, wert) → tensor` | Konstanter Tensor, z.B. `tensor([2], 5)` |
| `tensor_einsen` / `tensor_ones` | `(form) → tensor` | Alles 1.0 |
| `tensor_nullen` / `tensor_zeros` | `(form) → tensor` | Alles 0.0 |
| `tensor_zufall` / `tensor_random` | `(form, seed) → tensor` | Deterministischer Zufall — gleicher Seed, gleiche Werte |

**Beispiel** (aus dem Test-Gate `test_tensor_builtins.moo`):
```moo
setze a auf tensor_aus_liste([[1, 2], [3, 4]])
setze b auf tensor_einsen([2, 2])
zeige a + b
zeige a * 2
zeige 10 - a
zeige -a
zeige a ** 2
```

Operatoren broadcasten nach NumPy-Regeln (rechts ausgerichtet; Dimensionen kompatibel, wenn gleich oder 1). Division ist IEEE-754: `x/0 = ±inf`, `0/0 = nan` — es wird nicht geworfen (ML-üblich).

## Methoden auf Tensoren

| Methode (DE / EN) | Zweck |
|---|---|
| `.matmul(b)` | Matrix-Multiplikation |
| `.transponieren()` / `.transpose()` | Achsen tauschen |
| `.umformen(form)` / `.reshape(form)` | Neue Form, gleiche Daten |
| `.summe(achse?)` / `.sum(achse?)` | Summe — ohne Achse alles, `0`/`1` = Spalten/Zeilen |
| `.mittel(achse?)` / `.mean(achse?)` | Mittelwert |
| `.max_wert()` / `.max_value()` | Größter Wert |
| `.relu()` `.sigmoid()` `.tanh()` `.gelu()` | Aktivierungsfunktionen |
| `.softmax()` `.logsoftmax()` | Zeilenweise (Wahrscheinlichkeits-)Normierung |
| `.exp()` `.log()` `.sqrt()` | Elementweise Mathematik |
| `.form()` / `.shape()` | Form als Liste |
| `.größe()` / `.size()` | Gesamtzahl der Elemente |
| `.zu_liste()` / `.to_list()` | Zurück in eine moo-Liste |
| `.wert(indizes)` / `.wert_setzen(indizes, x)` | Einzelwert lesen/schreiben |
| `.zeilen(von, bis)` / `.rows(von, bis)` | Zeilen-Ausschnitt |
| `.verketten(b)` / `.concat(b)` | Aneinanderhängen |
| `.als_dtype("bf16")` / `.as_dtype("bf16")` | Speicherformat wechseln (f32 ↔ bf16, Mixed Precision) |

**Reduktions-Vertrag**: Achsen-Reduktionen behalten die Dimension (*keepdims*): `[r,c]` wird mit Achse 0 zu `[1,c]`, mit Achse 1 zu `[r,1]`. So broadcastet das Ergebnis direkt zurück — das Softmax-/Normierungs-Muster funktioniert ohne Umformen.

## Autograd — automatische Ableitungen

**Signaturen**:
`tensor.mit_gradient()` / `.with_gradient()` — markiert den Tensor als trainierbar
`verlust.rueckwaerts()` / `.backward()` — berechnet alle Ableitungen ab einem Skalar
`tensor.gradient()` — liefert den Gradienten als Tensor
`tensor.gradient_loeschen()` / `.zero_gradient()` — setzt den Gradienten auf 0

**Beispiel** — Ableitung von `y = sum(x²)` ist `2x`:
```moo
setze x auf tensor_aus_liste([1, 2, 3]).mit_gradient()
setze y auf (x ** 2).summe()
y.rueckwaerts()
zeige x.gradient().zu_liste()   # [2, 4, 6]
```

Jeder Tensor-Op in der Registry hat einen geprüften Backward (Gradient-Check-Gate über die komplette Op-Registry — kein Op ohne verifizierte Ableitung).
