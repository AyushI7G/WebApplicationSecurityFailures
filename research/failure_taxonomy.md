# Failure Taxonomy

This taxonomy categorizes web application security failures based on their
underlying system-level causes rather than their surface manifestations.

## 1. Trust Boundary Violations
Failures arising from incorrect assumptions about where trust begins and ends.
Examples include client-side enforcement of security policies or implicit trust
in upstream components.

## 2. Implicit Assumption Failures
Failures caused by unstated assumptions about data shape, execution order, or
user behavior that are violated under adversarial conditions.

## 3. Authorization Logic Drift
Failures where access-control logic is inconsistently applied across system
components, routes, or layers, leading to privilege escalation or data exposure.

## 4. Abstraction Leakage
Failures where high-level abstractions obscure critical security-relevant
details, causing developers to unknowingly rely on unsafe defaults.

## 5. Composition-Induced Failures
Failures that emerge only when multiple components interact, even if each
component appears correct in isolation.
