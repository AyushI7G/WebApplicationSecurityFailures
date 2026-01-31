# Baseline System Architecture

The baseline web application implements a conventional architecture common
in modern web systems.

## Core Components
- Authentication handled via session-based login
- Authorization enforced at route level
- Input validation performed at request boundaries
- Client-server interaction over RESTful APIs

## Trust Boundaries
- Boundary between client and server
- Boundary between authenticated and unauthenticated users
- Boundary between user roles (e.g., user and admin)

This baseline serves as a reference system against which alternative
architectural variants are evaluated.
