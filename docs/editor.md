# Editor-Integration

## VS Code

Eine Extension für **Syntax-Highlighting** und einen einfachen **Language Server** (Diagnostics, Keyword-Completion) liegt im Quell-Repo.

### Installation

1. Quell-Repo klonen:
   ```sh
   git clone https://github.com/7blacky7/moo ~/dev/moo
   ```
2. Extension in das VS-Code-Extensions-Verzeichnis kopieren:

    === "Linux (Code - OSS)"

        ```sh
        cp -r ~/dev/moo/editors/vscode/moo ~/.vscode-oss/extensions/moo-lang-0.2.0
        ```

    === "Linux/macOS (VS Code)"

        ```sh
        cp -r ~/dev/moo/editors/vscode/moo ~/.vscode/extensions/moo-lang-0.2.0
        ```

    === "Windows (VS Code)"

        ```powershell
        xcopy /E moo\editors\vscode\moo %USERPROFILE%\.vscode\extensions\moo-lang-0.2.0\
        ```

3. VS Code neu starten (oder `Strg+Shift+P` → „Developer: Reload Window").

### Workspace Trust

!!! warning "Restricted Mode blockiert den LSP"
    Beim ersten Öffnen eines `.moo`-Ordners fragt VS Code nach **Workspace Trust**.
    Wenn du „Restricted Mode" aktiv lässt, startet der LSP-Server **nicht** — du siehst dann nur Syntax-Highlighting, aber keine Fehler-Diagnostics.

    Klicke oben im Banner auf **„Trust"** oder wähle in der Statusleiste unten links „Restricted" → „Manage Workspace Trust" → „Trust".

### Language Server einschalten (optional)

Der LSP-Server ist in Python geschrieben und liefert Fehler-Diagnostics und Keyword-Completion. Er braucht **Python 3.12+** und **[uv](https://github.com/astral-sh/uv)**:

```sh
cd ~/dev/moo
uv sync
```

Danach startet die Extension den LSP automatisch bei `.moo`-Dateien (`uv run moo lsp`).

### Was die Extension kann

- **Syntax-Highlighting** für `.moo`-Dateien (Keywords DE+EN, Strings, f-Strings, Zahlen, Kommentare, Operatoren, Builtins)
- **Auto-Closing** für `()`, `[]`, `{}`, `""`, `''`
- **Einrück-Regeln** (Python-Style: `:` am Zeilenende → einrücken)
- **Fehler-Diagnostics** (live beim Tippen, via LSP)
- **Keyword-Completion** (Deutsch + Englisch)

### Was (noch) nicht

- Kein Go-to-Definition
- Kein Rename-Refactoring
- Kein Typsystem (Lexer-/Parser-Level only)

## Andere Editoren

Aktuell gibt es **nur** die VS-Code-Extension. Bei Bedarf: Die `moo.tmLanguage.json`-Grammatik lässt sich auch in Sublime Text, Atom, TextMate und JetBrains-IDEs einbinden — Kontaktaufnahme per [Issue](https://github.com/7blacky7/moo/issues).
