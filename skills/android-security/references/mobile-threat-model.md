# Mobile Threat Model (Practical Baseline)

## Assets to protect

- Authentication tokens
- Personally identifiable information
- Payment-sensitive fields
- Internal API endpoints and abuse controls

## Common threat surfaces

- Reverse engineering and static extraction
- MITM or network traffic manipulation
- Device compromise and runtime tampering
- Insecure local persistence and logs

## Baseline controls

- Secure storage for sensitive material
- Strict TLS and certificate validation strategy
- Minimized and rotated token lifetimes
- Build/release pipeline secret hygiene
- Integrity checks where abuse risk warrants it

## Residual risk mindset

Client security is layered risk reduction, not total prevention.
Prioritize controls by exploitability and business impact.
