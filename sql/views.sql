-- =====================================================
-- Provider Summary
-- =====================================================

CREATE VIEW vw_provider_summary AS
SELECT
    p.npi,
    p.last_org_name,
    p.first_name,
    p.provider_type,
    COUNT(ps.id) AS services_reported,
    SUM(ps.total_services) AS total_services,
    SUM(ps.total_beneficiaries) AS total_beneficiaries
FROM providers p
LEFT JOIN provider_service_statistics ps
ON p.npi = ps.provider_npi
GROUP BY
    p.npi,
    p.last_org_name,
    p.first_name,
    p.provider_type;


-- =====================================================
-- HCPCS Summary
-- =====================================================

CREATE VIEW vw_hcpcs_summary AS
SELECT
    h.hcpcs_code,
    h.description,
    COUNT(ps.id) AS provider_count,
    SUM(ps.total_services) AS total_services,
    AVG(ps.avg_payment_amount) AS average_payment
FROM hcpcs_codes h
LEFT JOIN provider_service_statistics ps
ON h.hcpcs_code = ps.hcpcs_code
GROUP BY
    h.hcpcs_code,
    h.description;


-- =====================================================
-- Detailed Provider Claims
-- =====================================================

CREATE VIEW vw_provider_service_details AS
SELECT
    p.npi,
    p.last_org_name,
    p.first_name,
    p.provider_type,

    h.hcpcs_code,
    h.description AS hcpcs_description,

    pos.place_of_service_code,
    pos.description AS place_of_service_description,

    ps.total_beneficiaries,
    ps.total_services,
    ps.total_bene_day_services,

    ps.avg_submitted_charge,
    ps.avg_allowed_amount,
    ps.avg_payment_amount,
    ps.avg_standardized_amount

FROM provider_service_statistics ps

JOIN providers p
ON ps.provider_npi = p.npi

JOIN hcpcs_codes h
ON ps.hcpcs_code = h.hcpcs_code

JOIN place_of_service pos
ON ps.place_of_service_code = pos.place_of_service_code;