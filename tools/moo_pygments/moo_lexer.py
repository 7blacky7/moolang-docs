"""Pygments-Lexer für moo/moolang.

Keyword-Listen maschinell extrahiert aus moo spec/tokens.yaml (SSoT,
Stand 2026-07-10, status=active, Vereinigung DE/EN/Kurzformen).
Bei neuen Keywords: Liste aus tokens.yaml neu generieren (siehe Repo-README).
"""
from pygments.lexer import RegexLexer, words, bygroups
from pygments.token import (Comment, String, Number, Keyword, Name,
                            Operator, Punctuation, Whitespace)

__all__ = ["MooLexer"]

KEYWORDS = (
    "als", "and", "as", "auf", "aufräumen", "aus", "break", "case", "catch",
    "class", "const", "continue", "data", "daten", "default", "defer",
    "else", "erwarte", "expect", "export", "exportiere", "fa", "fall",
    "fange", "fange_fehler", "fn", "for", "from", "fu", "fuer",
    "fuer_jedes", "func", "funktion", "funktion_definiere", "für",
    "garantiere", "gib_wert_zurück", "gib_zurück", "gr", "guard", "if",
    "im", "implementiert", "implements", "import", "importiere",
    "importiere_modul", "in", "interface", "kl", "klasse", "ko",
    "konstante", "match", "nachbedingung", "neu", "neue_klasse", "new",
    "nicht", "not", "oder", "or", "order", "parallel", "postcondition",
    "pr", "precondition", "prüfe", "return", "schnittstelle", "se",
    "selbst", "select", "set", "setze", "setze_variable", "show", "sl",
    "so", "solange", "solange_wiederhole", "sonst", "sonst_alternative",
    "sortiere", "st", "standard", "stopp", "test", "teste", "this",
    "throw", "to", "try", "un", "und", "unsafe", "unsicher", "ve",
    "versuche", "versuche_ausfuehrung", "von", "vorbedingung", "we",
    "weiter", "wenn", "wenn_bedingung", "where", "while", "wirf", "wo",
    "wt", "wähle", "ze", "zeige", "zeige_auf_bildschirm",
)

LITERALS = ("wahr", "falsch", "true", "false", "nichts", "none")

IDENT = r"[A-Za-zÄÖÜäöüß_][A-Za-z0-9ÄÖÜäöüß_]*"


class MooLexer(RegexLexer):
    name = "moo"
    aliases = ["moolang"]
    filenames = ["*.moo"]
    mimetypes = ["text/x-moo"]

    tokens = {
        "root": [
            (r"[ \t]+", Whitespace),
            (r"#.*$", Comment.Single),
            (r'f"', String.Interpol, "fstring"),
            (r'"', String.Double, "string"),
            (r"\d+\.\d+", Number.Float),
            (r"0x[0-9A-Fa-f]+", Number.Hex),
            (r"\d+", Number.Integer),
            (words(LITERALS, suffix=r"\b"), Keyword.Constant),
            (words(KEYWORDS, suffix=r"\b"), Keyword),
            (IDENT + r"(?=\s*\()", Name.Function),
            (IDENT, Name),
            (r"[+\-*/%<>=!&|^~]+", Operator),
            (r"[()\[\]{}.,:;]", Punctuation),
            (r"\n", Whitespace),
        ],
        "string": [
            (r'[^"\\]+', String.Double),
            (r"\\.", String.Escape),
            (r'"', String.Double, "#pop"),
        ],
        "fstring": [
            (r"\{[^}]*\}", String.Interpol),
            (r'[^"\\{]+', String.Double),
            (r"\\.", String.Escape),
            (r'"', String.Interpol, "#pop"),
        ],
    }
