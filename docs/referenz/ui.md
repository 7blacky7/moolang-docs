# Natives UI (Desktop-Fenster)

## Was ist das?

moo hat ein **natives, OS-neutrales UI-Modul**: echte Desktop-Fenster mit Widgets, Menüs, Tray-Icon und Event-Loop — unter Linux via GTK3, unter Windows via Win32, unter macOS via Cocoa. Die API ist auf allen drei Systemen **identisch** (dieselben Signaturen, nur das Backend dahinter wechselt), Widgets sehen also überall nativ aus. Alle Widget-Handles sind normale moo-Werte; Callbacks werden automatisch verwaltet (nichts manuell freigeben).

Das Grundmuster: Fenster bauen → Widgets hineinsetzen → `ui_zeige(fenster)` → `ui_laufen()` startet die **eine** gemeinsame Event-Loop (Fenster und Tray teilen sie sich).

Fenster-Flags steuern das Verhalten (als Bitfeld bzw. bequem über `ui_flags`): resizable, maximiert, fullscreen, modal — vom starren Login-Dialog bis zur vollflexiblen Hauptanwendung.

Die vollständigen Signaturen der Widget-Grundschicht (Fenster, Label, Knopf, Eingabe, Checkbox, Dropdown, Liste/Tabelle, Textbereich, Menü, Datetime, Clipboard, Event-Hooks für Resize/Enter/Key/Scroll, Tray) stehen in `compiler/runtime/moo_ui.h` — darüber liegt die hier dokumentierte **stdlib-Schicht**, der empfohlene Einstieg.

---

## Deklarativ bauen: `ui_baue`

**Signatur**: `ui_baue(container, titel, breite, hoehe, setups, resizable, maximiert, parent) → fenster`
**Zweck**: Baut ein Fenster aus einer Liste von Setup-Funktionen (Komponenten) — deklarativer Stil statt Einzelaufrufe. `ui_debug_baue` (gleiche Signatur) protokolliert dabei jeden Schritt. `ui_flags(resizable, maximiert, fullscreen, modal)` packt die Fenster-Flags.

## Layout-System

Statt Pixel-Koordinaten: Zeilen und Spalten mit Abstand, Padding und Ausrichtung — das Layout rechnet Positionen selbst.

| Funktion | Signatur | Zweck |
|---|---|---|
| `ui_zeile` / `ui_spalte` | `(parent, x, y, b, h) → layout` | Horizontaler/vertikaler Container |
| `ui_layout_padding` | `(layout, oben, rechts, unten, links)` | Innenabstand |
| `ui_layout_abstand` | `(layout, gap)` | Abstand zwischen Kindern |
| `ui_layout_hinzufuegen` | `(layout, widget, opts)` | Beliebiges Widget einhängen |
| `ui_layout_neu_berechnen` | `(layout)` | Positionen neu berechnen (z.B. nach Resize) |
| `ui_layout_label/knopf/eingabe/checkbox/dropdown` | `(layout, …, opts)` | Widget direkt im Layout erzeugen |

## Data-Binding: Widgets ↔ State

Ein State-Dict hält die Daten, `ui_bind_*` verdrahtet Widgets in beide Richtungen — ändert sich der State, aktualisiert sich das Widget (und umgekehrt beim Sync).

| Funktion | Zweck |
|---|---|
| `ui_bind_text(widget, state, key)` | Eingabefeld ↔ State |
| `ui_bind_checked` / `ui_bind_wert` / `ui_bind_auswahl` | Checkbox / Zahlwert / Dropdown-Auswahl |
| `ui_bind_label` / `ui_bind_textbereich` | Anzeige-Bindings |
| `ui_bind(widget, state, key, typ)` | Generische Variante |
| `ui_state_hole` / `ui_state_setze` | State lesen/schreiben (pusht zu gebundenen Widgets) |
| `ui_state_on_change(state, key, cb)` | Reagieren auf Änderungen |
| `ui_state_sync_von_widgets(state)` | Widgets → State einsammeln |

## Aktionen, Toolbar & Menü

Zentrale Aktions-Registry: eine Aktion (Name, Titel, Shortcut, Callback) einmal definieren, dann als Toolbar-Knopf **und** Menü-Eintrag verwenden.

`ui_aktion(g, name, titel, shortcut, callback)` · `ui_aktionen_liste(g)` · `ui_toolbar(parent, x, y, b, h, aktionsliste)` · `ui_toolbar_aus_g(g, x, y, b, h)` · `ui_menue_aktion(menue_handle, aktion)`

## Fertige Komponenten

`stdlib/ui_komponenten.moo` liefert einbaufertige Setup-Bausteine für `ui_baue`: `setup_login_form`, `setup_user_form`, `setup_toolbar`, `setup_status_bar` / `setup_statusbar_erweitert`, `setup_app_header`, `setup_action_buttons`, `setup_notes_area`, `setup_about_info`, `setup_settings_panel`, `setup_file_browser`, `setup_wizard_pages`, `setup_keyboard_shortcuts`, `setup_suchleiste`, `setup_liste_mit_aktion`, `setup_log_konsole` (mit `log_anhaengen` / `log_leeren`).

## Listen & Tabellen

`ui_liste_fuellen(liste, zeilen)` · `ui_liste_spalten_breiten(liste, breiten)` · `ui_liste_alle_sortierbar(liste, anzahl)` / `ui_liste_sortierbar_flags(liste, flags)` · `ui_liste_konfiguriere(liste, config)` — dazu Bulk-Insert und Scroll-Steuerung in der Grundschicht für große Datenmengen.

## Introspektion & UI-Tests

Jedes Fenster kann seinen Widget-Baum offenlegen — die Grundlage für Automation und Snapshot-Tests:

| Funktion | Zweck |
|---|---|
| `ui_widget_dump(widget)` / `ui_widget_baum_json(fenster)` | Widget-Baum als Text/JSON |
| `ui_widget_anzahl` / `ui_widget_typen_zaehlen` | Baum-Statistik |
| `ui_test_klick_id(fenster, id)` | Klick per Widget-ID injizieren |
| `ui_test_text_setze_id(fenster, id, text)` | Text per ID setzen |
| `ui_test_aktion(fenster, aktion_dict)` | Generische Test-Aktion |
| `ui_test_snapshot_mit_sidecar(fenster, pfad_basis)` | Screenshot + JSON-Sidecar (Widget-Baum, Backend, Zeitstempel) |
| `ui_test_snapshot_serie(fenster, ordner, prefix, frames, abstand_ms)` | Frame-Serie |
| `ui_test_frame` / `ui_test_sequenz` | Aktion ausführen + Snapshot, ganze Test-Drehbücher |

## Canvas-Helfer

Für Zeichenflächen: `ui_leinwand_zentriert_text`, `ui_leinwand_drag_init` / `ui_leinwand_drag_rechteck` (Drag-Auswahl), `ui_leinwand_status_text`.

## Ausblick

Die Drei-Backend-Architektur mit einheitlicher API, Layout-Engine, Data-Binding und Introspektion ist die Grundlage für **eigene, systemunabhängige Custom-Widgets** — geplant ist, dass sich eigene Elemente genauso registrieren und stylen lassen wie die eingebauten.
