# Profiler

## Was ist das?

Ein Profiler (Performance-Profiler, Function Profiler) misst, wo dein Programm
wirklich Zeit verbringt — welche Funktionen wie oft aufgerufen werden und wie
lange sie kumuliert laufen. Das ist die Grundlage jeder Optimierung, weil
Vermutungen ("das ist sicher langsam") fast immer daneben liegen. Das Modell
entspricht `cProfile` in Python, `-pg`/`gprof` in C oder eingebauten Profilern
in JVM/V8: der moo-Compiler fügt bei einem speziellen Build-Flag automatisch
**Enter**- und **Exit**-Haken in jede Nutzer-Funktion ein (Instrumentierung zur
Kompilierzeit) und druckt am Programm-Ende einen Report. Du schreibst dafür
keinen eigenen Code — einfach mit Flag neu kompilieren und laufen lassen.

---

Es gibt **keine Profile-Builtins auf Sprachebene** — die Instrumentierung wird
vom Compiler eingefügt.

## Aktivierung

CLI-Flag beim `compile`-Befehl:

```sh
moo-compiler compile programm.moo --profile -o programm
./programm
```

Der Compiler ruft dann automatisch für jede Nutzer-Funktion auf:

- `moo_profile_enter(name)` am Funktions-Anfang
- `moo_profile_exit(name)` an jedem Return-Pfad
- `moo_profile_report()` am Ende von `main`

(Definiert in `compiler/src/codegen.rs` Zeilen 195–200, 1125–1141.)

## Runtime-Funktionen (intern)

Diese werden vom Compiler eingefügt und sind nicht direkt aus moo aufrufbar —
sie existieren als Symbole in der C-Runtime:

| Symbol | Zweck |
|---|---|
| `moo_profile_enter(name)` | Funktions-Eintritt messen |
| `moo_profile_exit(name)` | Funktions-Austritt messen |
| `moo_profile_report()` | Aggregierten Report auf stdout drucken |

## Beispiel

```sh
moo-compiler compile beispiele/snake.moo --profile -o /tmp/snake_prof
/tmp/snake_prof
# Nach Programmende wird automatisch die Profile-Tabelle ausgegeben.
```

## Hinweis

Der Profiler ist ein Entwicklungs-Werkzeug. Für Production-Builds
das `--profile`-Flag weglassen — der Overhead der Instrumentierung
ist spürbar bei Hot-Loops.
