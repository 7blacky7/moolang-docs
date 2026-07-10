# Tokenizer & Chat-Template

## Was ist das?

Ein Tokenizer macht aus Text Zahlen (und zurück) — der erste Schritt jedes Sprachmodells. moo bringt zwei mit: den einfachen **Zeichen-Tokenizer** (`text_tokenizer` / `char_tokenizer`, ideal zum Lernen) und einen trainierbaren **Byte-level-BPE-Tokenizer** wie in echten LLMs. Obendrauf sitzt ein **Chat-Template** mit reservierten Rollen-Tokens für Dialog-Training.

## Zeichen-Tokenizer

**Signatur**: `text_tokenizer(korpus) → dict` (auch: `char_tokenizer`)
**Zweck**: Baut aus einem Text ein Vokabular echter Zeichen (`"ä"` ist EIN Zeichen) und liefert u.a. `ids` und `vokab`.

```moo
setze tok auf text_tokenizer("Es war einmal …")
zeige tok["vokab"]
```

## BPE-Tokenizer

Merges laufen auf rohen UTF-8-Bytes: jedes der 256 Bytes ist ein Basis-Token, daher gibt es **nie** ein UNK-Token, und `dekodiere(kodiere(x)) == x` ist byte-exakt — auch für Emoji, Umlaute und ungültiges UTF-8. Das Training ist **deterministisch ohne Seed** (kanonische Tie-Break-Regeln): zwei Läufe auf identischem Korpus sind bit-identisch. Der Tokenizer ist sein Artefakt (Format `MOOBPE01`).

| Builtin (DE / EN) | Signatur | Zweck |
|---|---|---|
| `tokenizer_trainiere` / `tokenizer_train` | `(korpus, vokab_groesse)` | BPE trainieren → Artefakt |
| `tokenizer_kodiere` / `tokenizer_encode` | `(tok, text)` | Text → Tensor der Token-Ids |
| `tokenizer_dekodiere` / `tokenizer_decode` | `(tok, ids)` | Ids → exakte Bytes |
| `tokenizer_kodiere_stapel` / `tokenizer_encode_batch` | `(tok, texte)` | Liste von Texten → Liste von Tensoren |
| `tokenizer_speichern` / `tokenizer_save` | `(tok, pfad)` | Artefakt byte-identisch in Datei |
| `tokenizer_laden` / `tokenizer_load` | `(pfad)` | Artefakt laden (Header-validiert) |
| `tokenizer_info` | `(tok)` | Dict: version, vokab, merges, spezial, flags, hash |
| `tokenizer_hash` | `(tok)` | Stabiler 64-bit-Artefakt-Hash (Versions-Anker für Shards/Checkpoints) |

## Chat-Template

Für Dialog-Training (SFT) gibt es einen reservierten Token-Satz: `bos`, `eos`, `pad`, `ende` plus die Rollen `system`, `user`, `assistant`, `tool`, `tool_result`. **Injection-Schutz eingebaut**: `kodiere()` kann diese Spezial-Tokens nie aus Nutzertext erzeugen — sie entstehen ausschließlich über die Render-API.

| Builtin (DE / EN) | Signatur | Zweck |
|---|---|---|
| `tokenizer_chat_init` / `chat_tokenizer` | `(tok)` | Hängt den Chat-Token-Satz an ein BPE-Artefakt |
| `tokenizer_spezial_id` / `tokenizer_special_id` | `(tok, name)` | Id eines Spezial-Tokens, z.B. `"assistant"`, `"eos"` |
| `tokenizer_rendern` / `tokenizer_render` | `(tok, dialog, mit_bos?)` | Dialogliste `[{rolle, inhalt}, …]` → Dict `{ids, loss_maske, stop_ids}` |

Die **Loss-Maske** entsteht beim Rendern: 1 auf Assistant-Inhalt (+ dessen Ende-Token), 0 auf allem anderen — der Trainings-Code muss keine Rollen kennen.
