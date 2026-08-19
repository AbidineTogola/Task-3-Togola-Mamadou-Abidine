# Phishing Awareness Analysis

A lightweight Python-based tool for analyzing messages and identifying common phishing indicators.

The project analyzes suspicious language, credential requests, threats, payment-related content, and potentially suspicious URLs. It then calculates a risk score and assigns a risk level to help users understand why a message may be suspicious.

---

## Overview

Phishing attacks use deceptive messages to manipulate users into revealing sensitive information, making payments, or clicking malicious links.

The goal of this project is to provide a simple and explainable phishing awareness tool capable of analyzing a message and identifying several common phishing indicators.

The analyzer does not attempt to determine with absolute certainty whether a message is malicious. Instead, it evaluates observable indicators and produces a risk assessment.

---

## Objectives

The main objectives of the project are to:

- Detect common phishing indicators in messages.
- Identify urgency and pressure tactics.
- Detect credential and security-related requests.
- Detect threats and suspicious consequences.
- Detect payment and financial-related indicators.
- Extract URLs from messages.
- Identify suspicious URL characteristics.
- Calculate a risk score.
- Classify the message into a risk level.
- Explain why the message was considered suspicious.
- Provide automated tests to verify the reliability of the application.

---

## Features

### Message Analysis

The analyzer checks messages for four categories of phishing indicators:

- **Urgency**
- **Credentials**
- **Threats**
- **Payment**

The keyword rules support both English and French.

Example indicators include:

```text
urgent
immediately
verify your account
security code
suspicious activity
payment failed
credit card
