---
title: 'Short/long polling, SSE, WebSocket'
description: 'Explore real-time web updates: polling, SSE, and WebSockets.'
image: 'https://assets.bytebytego.com/diagrams/0337-short-long-polling-sse-websocket.jpeg'
createdAt: '2024-01-25'
draft: false
categories:
  - api-web-development
tags:
  - WebSockets
  - SSE
---

![](https://assets.bytebytego.com/diagrams/0337-short-long-polling-sse-websocket.jpeg)

An HTTP server cannot automatically initiate a connection to a browser. As a result, the web browser is the initiator. What should we do next to get real-time updates from the HTTP server?

Both the web browser and the HTTP server could be responsible for this task.

*   **Web browsers do the heavy lifting**: short polling or long polling. With short polling, the browser will retry until it gets the latest data. With long polling, the HTTP server doesn’t return results until new data has arrived.
*   **HTTP server and web browser cooperate**: WebSocket or SSE (server-sent event). In both cases, the HTTP server could directly send the latest data to the browser after the connection is established. The difference is that SSE is uni-directional, so the browser cannot send a new request to the server, while WebSocket is fully-duplex, so the browser can keep sending new requests.
