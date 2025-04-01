---
title: "Session-based Authentication vs. JWT"
description: "Understand the key differences between session and JWT authentication."
image: "https://assets.bytebytego.com/diagrams/0333-what-s-the-difference-between-session-based-authentication-and-jwts.png"
createdAt: "2024-02-28"
draft: false
categories:
  - security
tags:
  - "Authentication"
  - "JWT"
---

![](https://assets.bytebytego.com/diagrams/0333-what-s-the_difference-between-session-based-authentication-and-jwts.png)

Here’s a simple breakdown for both approaches:

## Session-Based Authentication

In this approach, you store the session information in a database or session store and hand over a session ID to the user.

Think of it like a passenger getting just the Ticket ID of their flight while all other details are stored in the airline’s database.

Here’s how it works:

*   The user makes a login request and the frontend app sends the request to the backend server.
*   The backend creates a session using a secret key and stores the data in session storage.
*   The server sends a cookie back to the client with the unique session ID.
*   The user makes a new request and the browser sends the session ID along with the request.
*   The server authenticates the user using the session ID.

## JWT-Based Authentication

In the JWT-based approach, you don’t store the session information in the session store.

The entire information is available within the token.

Think of it like getting the flight ticket along with all the details available on the ticket but encoded.

Here’s how it works:

*   The user makes a login request and it goes to the backend server.
*   The server verifies the credentials and issues a JWT. The JWT is signed using a private key and no session storage is involved.
*   The JWT is passed to the client, either as a cookie or in the response body. Both approaches have their pros and cons but we’ve gone with the cookie approach.
*   For every subsequent request, the browser sends the cookie with the JWT.
*   The server verifies the JWT using the secret private key and extracts the user info.
