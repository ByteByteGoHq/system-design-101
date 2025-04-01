---
title: "Log Parsing Cheat Sheet"
description: "A handy guide to log parsing commands for efficient log analysis."
image: "https://assets.bytebytego.com/diagrams/0263-log-parsing.png"
createdAt: "2024-03-12"
draft: false
categories:
  - devops-cicd
tags:
  - "Log Analysis"
  - "Command Line"
---

![](https://assets.bytebytego.com/diagrams/0263-log-parsing.png)

The diagram below lists the top 6 log parsing commands.

## Log Parsing Commands

*   **GREP**

    GREP searches any given input files, selecting lines that match one or more patterns.

*   **CUT**

    CUT cuts out selected portions of each line from each file and writes them to the standard output.

*   **SED**

    SED reads the specified files, modifying the input as specified by a list of commands.

*   **AWK**

    AWK scans each input file for lines that match any of a set of patterns.

*   **SORT**

    SORT sorts text and binary files by lines.

*   **UNIQ**

    UNIQ reads the specified input file comparing adjacent lines and writes a copy of each unique input line to the output file.

These commands are often used in combination to quickly find useful information from the log files. For example, the below commands list the timestamps (column 2) when there is an exception happening for xxService.

```bash
grep “xxService” service.log | grep “Exception” | cut -d” “ -f 2
```
