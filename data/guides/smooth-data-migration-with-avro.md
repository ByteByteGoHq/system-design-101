---
title: "Smooth Data Migration with Avro"
description: "Learn how Apache Avro facilitates smooth data migration with schema evolution."
image: "https://assets.bytebytego.com/diagrams/0080-avro.png"
createdAt: "2024-02-01"
draft: false
categories:
  - database-and-storage
tags:
  - "Data Migration"
  - "Apache Avro"
---

![](https://assets.bytebytego.com/diagrams/0080-avro.png)

How do we ensure when performing data migration? The diagram above shows how Apache Avro manages the schema evolution during data migration.

Avro was started in 2009, initially as a subproject of Apache Hadoop to address Thrift’s limitation in Hadoop use cases. Avro is mainly used for two things: Data serialization and RPC.

Key points in the diagram:

*   We can export the data to **object container files**, where schema sits together with the data blocks. Avro **dynamically** generates the schemas based on the columns, so if the schema is changed, a new schema is generated and stored with new data.

*   When the exported files are loaded into another data storage (for example, teradata), anyone can read the schema and know how to read the data. The old data and new data can be successfully migrated to the new database.
    Unlike gRPC or Thrift, which statically generate schemas, Avro makes the data migration process easier.
