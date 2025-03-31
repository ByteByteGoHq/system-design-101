---
title: "How Scan to Pay Works"
description: "Explore the mechanics behind scan-to-pay systems and digital wallets."
image: "https://assets.bytebytego.com/diagrams/0323-scan-to-pay.png"
createdAt: "2024-03-05"
draft: false
categories:
  - payment-and-fintech
tags:
  - "Payment Systems"
  - "QR Codes"
---

![](https://assets.bytebytego.com/diagrams/0323-scan-to-pay.png)

How do you pay from your digital wallet, such as Paypal, Paytm and Venmo, by scanning the QR code?

To understand the process involved, we need to divide the “scan to pay” process into two sub-processes:

1. Merchant generates a QR code and displays it on the screen
2. Consumer scans the QR code and pays

Here are the steps for generating the QR code:

1. When you want to pay for your shopping, the cashier tallies up all the goods and calculates the total amount due, for example, $123.45. The checkout has an order ID of SN129803. The cashier clicks the “checkout” button.
2. The cashier’s computer sends the order ID and the amount to PSP.
3. The PSP saves this information to the database and generates a QR code URL.
4. PSP’s Payment Gateway service reads the QR code URL.
5. The payment gateway returns the QR code URL to the merchant’s computer.
6. The merchant’s computer sends the QR code URL (or image) to the checkout counter.
7. The checkout counter displays the QR code.

These 7 steps complete in less than a second. Now it’s the consumer’s turn to pay from their digital wallet by scanning the QR code:

1. The consumer opens their digital wallet app to scan the QR code.
2. After confirming the amount is correct, the client clicks the “pay” button.
3. The digital wallet App notifies the PSP that the consumer has paid the given QR code.
4. The PSP payment gateway marks this QR code as paid and returns a success message to the consumer’s digital wallet App.
5. The PSP payment gateway notifies the merchant that the consumer has paid the given QR code.
