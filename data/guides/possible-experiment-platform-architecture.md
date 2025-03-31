---
title: "Experiment Platform Architecture"
description: "Explore the architecture of an experiment platform with key components."
image: "https://assets.bytebytego.com/diagrams/0189-experiment-framework.jpg"
createdAt: "2024-03-08"
draft: false
categories:
  - how-it-works
tags:
  - "A/B Testing"
  - "Experimentation"
---

[![diagram](https://assets.bytebytego.com/diagrams/0189-experiment-framework.jpg)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd79ea50e-e386-41c9-9f66-e28006ed1115_1677x1536.jpeg)

The architecture of a potential experiment platform is depicted in the diagram below. This content of the visual is from the book: "Trustworthy Online Controlled Experiments" (redrawn by me). The platform contains 4 high-level components.

## Key Components

*   **Experiment definition, setup, and management via a UI.** They are stored in the experiment system configuration.

*   **Experiment deployment** to both the server and client-side (covers variant assignment and parameterization as well).

*   **Experiment instrumentation.**

*   **Experiment analysis.**
