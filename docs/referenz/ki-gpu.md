# GPU-Training (Vulkan)

## Was ist das?

moos Tensor-Runtime kann Training komplett auf der GPU ausführen — über **Vulkan Compute** (herstellerunabhängig, kein CUDA nötig). Gewichte, Aktivierungen, Gradienten und Optimizer-Zustand bleiben *resident* im VRAM; über die Leitung gehen nur der Batch hinein und der Loss heraus. Für den Nutzer ist das transparent: dieselben Builtins, die Runtime routet große Tensor-Ops automatisch auf die GPU.

Resident laufen u.a.: MatMul (tiled), alle Elementwise-Ops, Achsen-Reduktionen, Softmax + Kreuzentropie, Norm-Kerne (LayerNorm/RMSNorm), RoPE- und Head-Slicing-Kernels, SGD-/Adam-Schritte und die Gradienten-Akkumulation. Verifiziert per Gate: die GPU-Loss-Kurve entspricht der CPU-Referenz innerhalb dokumentierter Toleranz, zwei GPU-Läufe sind bit-identisch.

## `gpu_statistik` / `gpu_statistik_reset`

**Signatur**: `gpu_statistik() → dict`, `gpu_statistik_reset() → none`
**Zweck**: Telemetrie der GPU-Schicht — Submits, Uploads, Downloads, CPU-Fallbacks. Damit lässt sich *beweisen*, dass ein Training wirklich resident läuft (`cpu_fallbacks == 0`, im Steady-State keine Uploads).

**Beispiel**:
```moolang
gpu_statistik_reset()
netz.trainiere(daten, ziele, {"epochen": 10})
zeige gpu_statistik()
```

## STRIKT-Modus

Mit der Umgebungsvariable `MOO_KI_GPU_STRIKT=1` wirft die Runtime einen Fehler, statt still auf die CPU auszuweichen — das Beweis-Werkzeug der GPU-Gates: kein versteckter Fallback bleibt unentdeckt.

## Checkpoints über Geräte hinweg

Der Voll-Checkpoint-Pfad (`checkpoint_speichern` / `checkpoint_laden`, siehe [Netze & Training](ki-netze.md)) funktioniert cross-device: auf der GPU trainieren, auf der CPU fortsetzen — oder umgekehrt. Das Format bleibt dasselbe (safetensors-kompatibel), Grad-Puffer werden nicht serialisiert (nach abgeschlossenem Schritt transient).
