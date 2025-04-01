---
title: 'How Browsers Render Web Pages'
description: 'Explore how browsers render web pages: from HTML parsing to display.'
image: 'https://assets.bytebytego.com/diagrams/0090-browser-render-page.jpg'
createdAt: '2024-02-01'
draft: false
categories:
  - api-web-development
tags:
  - browsers
  - rendering
---

![](https://assets.bytebytego.com/diagrams/0090-browser-render-page.jpg)

*   **Parse HTML and generate a Document Object Model (DOM) tree.**

    When the browser receives the HTML data from the server, it immediately parses it and converts it into a DOM tree.

*   **Parse CSS and generate CSSOM tree.**

    The styles (CSS files) are loaded and parsed to the CSSOM (CSS Object Model).

*   **Combine DOM tree and CSSOM tree to construct the Render Tree.** The render tree maps all DOM structures except invisible elements (such as `<head>` or tags with `display:none;`). In other words, the render tree is a visual representation of the DOM.

*   **Layout**

    The content in each element of the rendering tree will be calculated to get the geometric information (position, size), which is called layout.

*   **Painting**

    After the layout is complete, the rendering tree is transformed into the actual content on the screen. This step is called painting. The browser gets the absolute pixels of the content.

*   **Display**

    Finally, the browser sends the absolute pixels to the GPU and displays them on the page.
