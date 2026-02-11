# Threat Model

This project assumes a remote adversary interacting with the web application
over standard HTTP interfaces.

## Adversary Capabilities
- Can send arbitrary HTTP requests to exposed endpoints
- Can manipulate request parameters, headers, and payloads
- Can observe system responses and error behavior
- Does not have initial authenticated access unless otherwise stated

## Adversary Goals
- Bypass authentication mechanisms
- Escalate privileges through access-control failures
- Exploit implicit trust assumptions in input handling
- Induce unintended system behavior

## Trust Assumptions
- The server runtime and underlying operating system are trusted
- Cryptographic primitives behave as expected
- Failures arise from application-level design and architecture

This threat model enables controlled analysis of security failures arising
from system design choices rather than infrastructure compromise.

## Non-Goals
- Kernel or OS-level compromise
- Cryptographic primitive failures
- Infrastructure-level attacks (e.g., DDoS)
