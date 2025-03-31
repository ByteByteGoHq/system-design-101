---
title: "Running C, C++, or Rust in a Web Browser"
description: "Explore running C, C++, and Rust code in web browsers using WASM."
image: "https://assets.bytebytego.com/diagrams/0406-how-wasm-work.jpeg"
createdAt: "2024-02-21"
draft: false
categories:
  - software-development
tags:
  - "WebAssembly"
  - "Performance"
---

![](https://assets.bytebytego.com/diagrams/0406-how-wasm-work.jpeg)

What is **web assembly** (WASM)? Why does it attract so much attention?

The diagram shows how we can run native C/C++/Rust code inside a web browser with WASM.

Traditionally, we can only work with Javascript in the web browser, and the performance cannot compare with native code like C/C++ because it is interpreted.

However, with WASM, we can **reuse** existing native code libraries developed in C/C++/Rust, etc to run in the web browser. These web applications have near-native performance.

For example, we can run the **video encoding/decoding** library (written in C++) in the web browser.

This opens a lot of possibilities for cloud computing and **edge computing**. We can run serverless applications with fewer resources and instant startup time.
