# Neuronale Netze & Training

## Was ist das?

moos NN-Stack hat drei Ebenen: die **Kinderleicht-API** (ein Netz in 5 Zeilen), die **Schicht-Bausteine** (vom Dense-Layer bis zum kompletten Transformer mit Attention, RoPE und MoE) und die **Low-Level-Werkzeuge** (Optimizer, Verlustfunktionen, Autograd) für volle Kontrolle. Alle drei nutzen dieselben Tensoren — man kann jederzeit die Ebene wechseln.

## Kinderleicht-API

**Beispiel** (verifiziert, `beispiele/ki_kinderleicht.moo` — XOR in 5 Zeilen):
```moolang
setze daten auf tensor_aus_liste([[0,0],[0,1],[1,0],[1,1]])
setze ziele auf tensor_aus_liste([[0],[1],[1],[0]])
setze netz auf ki_netz([schicht_dicht(2, 8, "tanh", 7), schicht_dicht(8, 1, "sigmoid", 8)])
setze verlauf auf netz.trainiere(daten, ziele, {"epochen": 400, "rate": 0.05})
zeige netz.vorhersage(daten).zu_liste()
```

| Builtin (DE / EN) | Zweck |
|---|---|
| `ki_netz(schichten)` / `ai_net` | Stapelt Schichten zu einem Netz |
| `netz.trainiere(x, y, optionen)` / `.train` | Trainiert; gibt Fehler-Verlauf als Liste zurück |
| `netz.vorhersage(x)` / `.predict` | Forward-Pass |
| `netz.genauigkeit(x, y)` / `.accuracy` | Trefferquote |
| `netz.speichern(pfad)` / `.save` | Schreibt `.mook` (= safetensors-Format!) |
| `ki_laden(pfad)` / `ai_load` | Lädt ein `.mook`-Netz |
| `safetensors(pfad)` | Fremd-safetensors importieren → Dict `{name: Tensor}` |

**Trainings-Optionen** (Dict, alle mit Standardwerten):

| Option | Bedeutung |
|---|---|
| `"epochen"` | Wie oft alle Beispiele gezeigt werden |
| `"rate"` | Lernrate |
| `"batch"` | Beispiele pro Schritt |
| `"optimierer"` | `"adam"` (Default), `"adamw"`, `"sgd"` |
| `"verlust"` | `"auto"`: endet das Netz auf softmax → Kreuzentropie (Ziele dürfen Klassen-Nummern sein), sonst MSE |
| `"ausgabe"` | `1` = Fortschritt drucken, `0` = still |
| `"seed"` | Deterministisches Mischen |
| `"clip"` | Gradient-Clipping (kappt zu große Lernschritte) |
| `"lr_plan"` | `"cosine"`, `"step"`, `"warmup"` — Lernraten-Plan |
| `"geduld"` / `"min_besserung"` | Early Stopping |
| `"checkpoint"` | Pfad — speichert laufend das beste Modell |

## Schicht-Bausteine

| Builtin | Signatur | Zweck |
|---|---|---|
| `schicht_dicht` / `layer_dense` | `(ein, aus, aktivierung?, seed?)` | Vollverbundene Schicht |
| `schicht_faltung` / `layer_conv2d` | `(kanaele_ein, kanaele_aus, kernel, schritt?, polster?, aktivierung?, seed?)` | 2D-Faltung auf NHWC-Bildern; Ausgabe bleibt NHWC |
| `schicht_pooling` / `layer_pooling` | `(art?, groesse?, schritt?)` | Räumliches `"max"`- oder `"mittel"`-Pooling |
| `schicht_flach` / `layer_flatten` | `()` | Formt `[batch, h, w, kanaele]` zu `[batch, merkmale]` um |
| `schicht_dropout` | `(rate)` | Deterministisches Dropout |
| `schicht_layernorm` | `(dim)` | LayerNorm (gamma/beta) |
| `schicht_rmsnorm` | `(dim)` | RMSNorm — Standard moderner LLMs |
| `schicht_ffn_gated` | `(dim, versteckt, art?)` | Gated-FFN: `"swiglu"` oder `"geglu"` |
| `schicht_embedding` | `(vokabular, dim, seed?)` | Token-Embedding (Gather) |
| `schicht_attention` | `(dim, koepfe, seed?, kv_koepfe?, maske?, fenster?, rope?)` | Multi-Head-Attention: GQA/MQA über `kv_koepfe`, kausale Maske, Sliding Window über `fenster`, RoPE-Rotations-Encoding |
| `schicht_position` | `(max_laenge, dim, art?, seed?)` | Positions-Encoding |
| `schicht_moe` | `(dim, versteckt, n_experten, k, seed?)` | Mixture-of-Experts (Top-k-Router) |

Dazu auf Netz-Ebene: `moe_balance(netz)` (Balance-Verlust nach dem Forward), `cache_leeren(netz)` (KV-Cache für Inferenz zurücksetzen), `sequence_packen(docs, block_len)` + `packung_setzen(netz, maske, positionen)` (mehrere Dokumente pro Block ohne Cross-Attention) und `checkpoint(netz, x)` (Activation Checkpointing — Speicher sparen durch Segment-Re-Forward).

## Low-Level: selbst trainieren

**Beispiel** (aus `docs/lernen.md` Stufe 3 — das macht `trainiere` intern):
```moolang
setze schichten auf [schicht_dicht(2, 8, "tanh"), schicht_dicht(8, 1, "sigmoid")]
setze opt auf optimierer_adam(parameter(schichten), 0.05)
setze i auf 0
solange i < 400:
    setze fehler auf mse(vorwaerts(schichten, daten), ziele)
    fehler.rueckwaerts()
    opt.schritt()
    setze i auf i + 1
```

| Builtin | Zweck |
|---|---|
| `parameter(schichten)` | Alle trainierbaren Tensoren einsammeln |
| `vorwaerts(schichten, x)` | Forward durch eine Schicht-Liste |
| `mse(y, ziel)` / `kreuzentropie(logits, ziel)` | Verlustfunktionen (CE fused auf Logits = Profi-Pfad) |
| `kontrastiv(a, b, temperatur?)` / `contrastive` | Symmetrischer InfoNCE-Verlust für gepaarte Embeddings |
| `kosinus(a, b)` / `cosine` | Kosinus-Ähnlichkeit je Zeile |
| `optimierer_adam` / `optimierer_adamw` / `optimierer_sgd` | `(params, rate)` → Optimizer mit `.schritt()` |
| `gradienten_kappen(params, max_norm)` | Globales L2-Gradient-Clipping; gibt die Norm zurück |

`opt["rate"]` darf zwischen Schritten geändert werden (eigene Lernraten-Pläne).

## Checkpoints & Daten-Shards

**Voll-Checkpoints** (Training exakt fortsetzbar — Gewichte, Optimizer-Zustand, Dropout-Zähler, Dataloader-Position; Resume ist bit-identisch):

| Builtin (DE / EN) | Signatur |
|---|---|
| `checkpoint_speichern` / `checkpoint_save` | `(zustand, pfad)` — atomisch (tmp + rename) |
| `checkpoint_laden` / `checkpoint_load` | `(pfad, erwartete_version?)` |
| `checkpoint_rotieren` / `checkpoint_rotate` | `(verzeichnis, praefix, n)` — letzte n + bestes behalten |

**Token-Shards** (Streaming-Datenpipeline für LM-Training): `shard_schreiben`/`shard_write`, `shard_info`, `shard_pruefen`/`shard_check`, `shard_fenster`/`shard_window`, `shard_fenster_maske`/`shard_mask_window`, `shard_reihenfolge`/`shard_order` — deterministische Fenster-Zugriffe auf tokenisierte Korpora, inklusive Loss-Masken. Beispiele: `beispiele/ki_*`.
