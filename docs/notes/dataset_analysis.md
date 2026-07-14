# Dataset Analysis

## Dataset Information

**Dataset:** Medicare Physician & Other Practitioners by Provider and Service

**Source:** CMS Open Data Portal

**Version:** 2025 Release (using RY25 dataset)

---

## Dataset Summary

- Rows: 9,781,673
- Columns: 28

---

## Key Business Entities

### Provider

Identified by:

- Rndrng_NPI

Contains provider demographic and location information.

---

### Procedure

Identified by:

- HCPCS_Cd

Represents a medical procedure or service.

---

### Provider Service Statistics

Represents aggregated provider activity for a procedure.

Contains:

- Total beneficiaries
- Total services
- Average submitted charge
- Average Medicare allowed amount
- Average Medicare payment
- Average standardized payment

---

## Data Quality Observations

### Excellent

- No missing NPI values
- No missing HCPCS codes
- No missing payment values

### Expected Missing Values

- Provider middle initial
- Address line 2
- Credentials

These fields are optional and do not impact data integrity.

### ETL Considerations

- ZIP codes should be stored as text.
- State FIPS codes should be stored as text.
- Large dataset (~9.8 million rows) requires chunked processing during ETL.

---

## Candidate Database Tables

- Providers
- Procedures
- Provider_Service_Statistics