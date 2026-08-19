# Phishing Awareness Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Testing](https://img.shields.io/badge/Tests-15%20passed-success)
![Project](https://img.shields.io/badge/Project-Remote%20Internship-orange)
![Focus](https://img.shields.io/badge/Focus-Cybersecurity-red)

> **Remote Internship Project — DecodeLabs**

A lightweight Python-based phishing awareness analysis tool designed to identify common phishing indicators in messages and suspicious URLs.

## Internship Context

This project was developed as part of my **Remote Internship at DecodeLabs**.

The objective was to build a practical cybersecurity tool capable of analyzing potentially malicious messages, identifying phishing indicators, evaluating suspicious URLs, and assigning an explainable risk level.
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
