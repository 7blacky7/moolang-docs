# Threads & Channels

Echtes Multithreading (pthread-basiert) mit sicheren Channel-primitiven.

## Threads starten

```moo
funktion arbeiter(id):
    für i in [0, 1, 2, 3, 4]:
        zeige "Thread " + text(id) + ": " + text(i)
        warte(100)

thread_starten(arbeiter, [1])
thread_starten(arbeiter, [2])
thread_starten(arbeiter, [3])

warte(2000)    # Hauptthread wartet
```

## Channels (Go-Stil)

```moo
setze k auf kanal(16)     # Puffer für 16 Nachrichten

# Producer-Thread
funktion produzent():
    für i in [1, 2, 3]:
        k.senden("Wert " + text(i))
        warte(100)

# Consumer-Thread
funktion konsument():
    solange wahr:
        setze nachricht auf k.empfangen()
        zeige "Empfangen: " + nachricht

thread_starten(produzent, [])
thread_starten(konsument, [])
warte(1000)
```

Englisch: `channel(16)`, `ch.send(...)`, `ch.receive()`.

## Mutex

```moo
setze sperre auf mutex()
setze zaehler auf [0]

funktion inkrementieren():
    sperre.locken()
    zaehler[0] = zaehler[0] + 1
    sperre.entsperren()
```

## Anwendung: Parallel-Map

```moo
funktion parallel_map(fn, liste):
    setze kanal_aus auf kanal(länge(liste))
    für item in liste:
        thread_starten(lambda(x): kanal_aus.senden(fn(x)), [item])

    setze ergebnisse auf []
    für _ in liste:
        ergebnisse.hinzufügen(kanal_aus.empfangen())
    gib_zurück ergebnisse
```
