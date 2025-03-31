---
title: "Payment System"
description: "Explore the architecture and flow of a typical payment system."
image: "https://assets.bytebytego.com/diagrams/0299-payment-system.jpeg"
createdAt: "2024-03-07"
draft: false
categories:
  - payment-and-fintech
  - how-it-works
tags:
  - "Payment Processing"
  - "System Design"
---

![](https://assets.bytebytego.com/diagrams/0299-payment-system.jpeg)

Here is how money moves when you click the Buy button on Amazon or any of your favorite shopping websites.

## Payment Flow

*   When a user clicks the “Buy” button, a payment event is generated and sent to the payment service.

*   The payment service stores the payment event in the database.

*   Sometimes a single payment event may contain several payment orders. For example, you may select products from multiple sellers in a single checkout process. The payment service will call the payment executor for each payment order.

*   The payment executor stores the payment order in the database.

*   The payment executor calls an external PSP to finish the credit card payment.

*   After the payment executor has successfully executed the payment, the payment service will update the wallet to record how much money a given seller has.

*   The wallet server stores the updated balance information in the database.

*   After the wallet service has successfully updated the seller’s balance information, the payment service will call the ledger to update it.

*   The ledger service appends the new ledger information to the database.

*   Every night the PSP or banks send settlement files to their clients. The settlement file contains the balance of the bank account, together with all the transactions that took place on this bank account during the day.
