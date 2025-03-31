---
title: "Linux File Permissions Illustrated"
description: "Understand Linux file permissions: owner, group, and others."
image: "https://assets.bytebytego.com/diagrams/0259-linux-permissions-copy.png"
createdAt: "2024-03-08"
draft: false
categories:
  - devtools-productivity
tags:
  - "Linux"
  - "File Management"
---

![](https://assets.bytebytego.com/diagrams/0259-linux-permissions-copy.png)

## Ownership

Every file or directory is assigned 3 types of owner:

*   **Owner**: the owner is the user who created the file or directory.

*   **Group**: a group can have multiple users. All users in the group have the same permissions to access the file or directory.

*   **Other**: other means those users who are not owners or members of the group.

## Permission

There are only three types of permissions for a file or directory.

*   **Read (r)**: the read permission allows the user to read a file.

*   **Write (w)**: the write permission allows the user to change the content of the file.

*   **Execute (x)**: the execute permission allows a file to be executed.
