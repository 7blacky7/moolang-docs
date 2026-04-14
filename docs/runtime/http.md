# HTTP & Netzwerk

Eingebauter HTTP-Client (via libcurl) sowie WebSocket-, TCP- und MQTT-APIs.

## HTTP-Client

```moo
setze antwort auf http_hole("https://api.example.com/daten")
zeige antwort

setze ergebnis auf http_sende("https://api.example.com/senden", {"name": "Anna"})
zeige ergebnis
```

Englisch: `http_get`, `http_post`.

## Mit Headers

```moo
setze antwort auf http_hole("https://api.example.com/daten", {
    "Authorization": "Bearer xyz",
    "Accept": "application/json"
})
```

## WebSocket-Server

Moolang bringt einen vollständigen WebSocket-Server mit:

```moo
importiere websocket

websocket_server_starten(8080, funktion(nachricht, client_id):
    zeige "Client " + text(client_id) + ": " + nachricht
    gib_zurück "Echo: " + nachricht
)
```

## TCP-Sockets

Low-Level-Sockets für Proxys, Chat-Server, eigene Protokolle:

```moo
setze server auf tcp_lauschen(5555)
solange wahr:
    setze client auf tcp_akzeptieren(server)
    setze nachricht auf tcp_lesen(client)
    tcp_schreiben(client, "Hallo " + nachricht)
    tcp_schliessen(client)
```

## Siehe auch

- [Beispiel: http_api.moo](https://github.com/7blacky7/moo/blob/master/beispiele/http_api.moo) — Weather-API-Client
- [Beispiel: websocket_server.moo](https://github.com/7blacky7/moo/blob/master/beispiele/websocket_server.moo)
- [Beispiel: chat/](https://github.com/7blacky7/moo/tree/master/beispiele/chat) — Live-Chat-Server mit Browser-UI
- [Beispiel: mqtt_broker.moo](https://github.com/7blacky7/moo/blob/master/beispiele/mqtt_broker.moo) — eigener MQTT-Broker
- [Beispiel: proxy.moo](https://github.com/7blacky7/moo/blob/master/beispiele/proxy.moo)
