---
title: "How does SSH work?"
description: "Explore the inner workings of SSH, a secure network protocol."
image: "https://assets.bytebytego.com/diagrams/0224-how-does-ssh-work.png"
createdAt: "2024-03-05"
draft: false
categories:
  - security
tags:
  - "SSH"
  - "Security"
---

![](https://assets.bytebytego.com/diagrams/0224-how-does-ssh-work.png)

SSH (Secure Shell) is a network protocol used to securely connect to remote machines over an unsecured network. It encrypts the connection and provides various mechanisms for authentication and data transfer.

SSH has two versions: SSH-1 and SSH-2. SSH-2 was standardized by the IETF.

It has three main layers: Transport Layer, Authentication Layer, and Connection Layer.

## Transport Layer

The Transport Layer provides encryption, integrity, and data protection to ensure secure communication between the client and server.

## Authentication Layer

The Authentication Layer verifies the identity of the client to ensure that only authorized users can access the server.

## Connection Layer

The Connection Layer multiplexes the encrypted and authenticated communication into multiple logical channels.
