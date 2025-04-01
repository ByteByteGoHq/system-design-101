---
title: "MVC, MVP, MVVM, VIPER Patterns"
description: "Comparing MVC, MVP, MVVM, and VIPER architectural patterns."
image: "https://assets.bytebytego.com/diagrams/0143-client-arch-patterns.png"
createdAt: "2024-03-12"
draft: false
categories:
  - software-architecture
tags:
  - "architectural patterns"
  - "software design"
---

![MVC, MVP, MVVM, VIPER Patterns](https://assets.bytebytego.com/diagrams/0143-client-arch-patterns.png)

What distinguishes MVC, MVP, MVVM, MVVM-C, and VIPER architecture patterns from each other?

These architecture patterns are among the most commonly used in app development, whether on iOS or Android platforms. Developers have introduced them to overcome the limitations of earlier patterns. So, how do they differ?

*   MVC, the oldest pattern, dates back almost 50 years

*   Every pattern has a "view" (V) responsible for displaying content and receiving user input

*   Most patterns include a "model" (M) to manage business data

*   "Controller," "presenter," and "view-model" are translators that mediate between the view and the model ("entity" in the VIPER pattern)

*   These translators can be quite complex to write, so various patterns have been proposed to make them more maintainable
