---
title: "How ACH Payment Works"
description: "Learn how ACH payments work in the US, including direct deposit."
image: "https://assets.bytebytego.com/diagrams/0067-how-does-ach-payment-work.png"
createdAt: "2024-03-14"
draft: false
categories:
  - payment-and-fintech
tags:
  - ACH
  - Payments
---

![](https://assets.bytebytego.com/diagrams/0067-how-does-ach-payment-work.png)

Do you know how you get paid at work? In the US, tech companies usually run payrolls via Automatic Clearing House (**ACH**).

ACH handles retail transactions and is part of American retail payment systems. It processes transactions in **batches**, not in real-time. The diagram above shows how ACH direct deposit works with payrolls.

### How ACH Direct Deposit Works

*   Step 0: Before we can use the ACH network, the originator who starts the transactions needs to open an account at a commercial bank because only banks are allowed to initiate ACH transactions directly. The bank is called ODFI (Originating Depository Financial Institution). Then the transaction receiver needs to authorize the originator for certain types of transactions.

*   Step 1: The originator company originates salary payment transactions. The transactions are sent to a 3rd-party processor like Gusto. The third-party processor helps with ACH-related services like generating ACH files, etc.

*   Step 2: The third-party processor generates ACH files on behalf of the originator. The files are uploaded to an SFTP established by the ODFI. This should be done by the 7 PM cut-off time, as specified by the ODFI bank.

*   Step 3: After normal business hours in the evening, the ODFI bank forwards the ACH files to the ACH operator for clearing and settlement. There are two ACH operators, one is the Federal Reserve (FedACH), and the other is EPN (Electronic Payment Network – which is operated by a private company).

*   Step 4: The ACH files are processed around midnight and made available to the receiving bank RDFI (Receiving Depository Financial Institution.)

*   Step 5: The RDFI operates on the receiver’s bank accounts based on the instructions in the ACH files. In our case, the receiver receives $100 from the originator. This is done when the RDFI opens for business at 6 AM the next day.

ACH is a next-day settlement system. It means transactions sent out by 7 PM on one day will arrive the following morning.

Since 2018, it’s possible to choose Same Day ACH so funds can be transferred on the same business day.
