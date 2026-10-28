# Cardholder Data (PCI)

Cardholder account data and sensitive authentication data covered by the PCI DSS regime. Its storage, transmission, and processing are contractually mandated by the card brands.

## Classification
- **Sensitivity:** restricted
- **Regulatory regime:** PCI

## Handling requirements
- Storage of sensitive authentication data after authorization is prohibited.
- Access restricted to roles with documented business justification; each user carries a unique id.
- Encryption in transit and at rest over public networks.
- Quarterly vulnerability scans on in-scope systems.

## Retention
Per PCI DSS and card-brand retention limits; sensitive authentication data is never retained.

## Provenance
- **Established by:** CR-IC-CAT-04
- **Owner / steward:** Emmanuel A. Otchere / Emmanuel A. Otchere
- **Evidence:** PCI DSS (current version), card-brand operating regulations; internal cardholder-data policy; owner: Payment Security function.
