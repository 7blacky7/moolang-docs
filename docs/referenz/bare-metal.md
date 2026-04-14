# Bare-Metal & System-Programmierung

## Was ist das?

Bare-Metal (freestanding, no-std, embedded, baremetal) bedeutet: der
kompilierte moo-Code laeuft ohne Betriebssystem, ohne `malloc`, ohne
`printf`, ohne dynamische Allokationen — direkt auf Hardware (ESP32,
STM32, RP2040, Kernel, Bootloader). Dafuer bringt moo eine deutlich
kleinere Laufzeitumgebung mit (`moo_bare.c`), die nur Zahlen-Arithmetik,
Boolesche Werte und volatile Memory-I/O kennt. Wer moo fuer
Betriebssystem-Kernels, Treiber oder Embedded-Firmware verwenden will,
steigt hier ein.

> **Warnung**: Die Builtins auf dieser Seite sind `unsafe` in dem Sinne,
> wie Rust oder Zig das Wort benutzen. Falsche Adressen fuehren zu
> Faults, Crashes oder Datenkorruption. Nur verwenden, wenn klar ist, was
> an welcher Adresse liegt (Datasheet, Linker-Script, Peripherieregister).

## Compiler-Flags

Der native Compiler kennt drei bare-metal-relevante Flags:

| Flag | Zweck |
|------|-------|
| `--no-stdlib` | linkt `moo_bare.c` statt der vollen Runtime (kein malloc, kein printf) |
| `--linker_script <pfad>` | gibt ein eigenes Linker-Script an (fuer Flash-/RAM-Layout) |
| `--entry <symbol>` | setzt einen alternativen Entry-Point statt `main` (z.B. `_start` oder `reset_handler`) |

Beispiel:
```bash
moo-compiler compile firmware.moo --no-stdlib \
  --linker_script stm32f103.ld \
  --entry reset_handler \
  -o firmware.elf
```

## Volatile Memory-I/O

### `speicher_lesen` / `mem_read`

**Signatur**: `speicher_lesen(adresse, groesse) → zahl | nichts`
**Zweck**: Liest einen Wert direkt aus einer Speicheradresse als
`volatile` — der Compiler darf den Zugriff weder umordnen noch
wegoptimieren. `groesse` darf `1` (Byte), `2` (Halfword) oder `4` (Word)
sein; jeder andere Wert gibt `nichts` zurueck.

**Beispiel** — GPIO-Input-Register lesen:
```moo
# STM32: GPIOA Input Data Register bei 0x40010808
setze gpio_in auf speicher_lesen(0x40010808, 4)
wenn (gpio_in und 0x0001) != 0:
    zeige "Pin PA0 ist HIGH"
```

### `speicher_schreiben` / `mem_write`

**Signatur**: `speicher_schreiben(adresse, wert, groesse) → nichts`
**Zweck**: Schreibt `wert` direkt in die Speicheradresse als
`volatile`. Groessen `1`/`2`/`4` wie bei `speicher_lesen`.

**Beispiel** — LED umschalten:
```moo
# STM32: GPIOC ODR bei 0x40011010, PC13 ist LED
setze ODR auf speicher_lesen(0x40011010, 4)
speicher_schreiben(0x40011010, ODR xor 0x2000, 4)
```

## Grenzen der bare-metal Runtime

Die volle Runtime (Strings, Listen, Dicts, Threads, Regex, File-I/O, HTTP,
DB, Grafik) ist unter `--no-stdlib` **nicht** verfuegbar. Nur:

- Zahlen (Integer + Double, via Tagged Value)
- Boolean (`wahr` / `falsch`)
- `nichts`
- Arithmetik (`+`, `-`, `*`, `/`, `%`, `**`)
- Vergleiche (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- Logik (`und`, `oder`, `nicht`)
- Bitoperationen (`&`, `|`, `^`, `~`, `<<`, `>>`)
- `speicher_lesen` / `speicher_schreiben`
- `moo_retain` / `moo_release` sind no-ops (kein Refcount, kein Heap)

Alles andere muss bei Bedarf ueber eigene C-Bindings und das Linker-Script
ergaenzt werden. Siehe `compiler/runtime/moo_bare.c` fuer das vollstaendige
Set an Stubs und Primitiven.

## Sicherheitshinweise

- **Keine Schutzmechanismen**: `speicher_schreiben` in nicht gemappte
  oder reservierte Bereiche fuehrt je nach Target zu Hard Fault,
  Crash oder stillem Datenverlust.
- **Alignment beachten**: 32-bit-Zugriffe (`groesse=4`) muessen an
  4-byte-Grenzen erfolgen, 16-bit an 2-byte. ARM Cortex-M und RISC-V
  loesen sonst einen Alignment-Fault aus.
- **Peripherie-Register kein regulaerer Speicher**: Lese/Schreibzyklen
  haben oft Seiteneffekte. Reihenfolge und Zeitpunkte koennen fuer die
  Peripherie signifikant sein — `volatile` schuetzt das, aber die
  Programm-Logik muss es respektieren.
- **Kein Error-Handling**: In bare-metal fliegt kein Exception. Fehler
  muessen explizit abgefragt oder ueber Hardware-Traps behandelt werden.
