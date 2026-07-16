/*
=========================================================
Healthcare Claims Analytics Database Schema
=========================================================

Description:
Relational schema for analyzing CMS Medicare Physician &
Other Practitioners Provider and Service data.
*/

-- =====================================================
-- Providers
-- =====================================================

CREATE TABLE providers (
    npi BIGINT PRIMARY KEY,

    last_org_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(100),
    middle_initial CHAR(1),
    credentials VARCHAR(50),

    entity_code CHAR(1) NOT NULL,

    address_line1 VARCHAR(255) NOT NULL,
    address_line2 VARCHAR(255),

    city VARCHAR(100) NOT NULL,
    state CHAR(2) NOT NULL,
    zip_code VARCHAR(10) NOT NULL,
    country VARCHAR(50) NOT NULL,

    provider_type VARCHAR(150) NOT NULL,

    medicare_participating BOOLEAN NOT NULL
);

-- =====================================================
-- HCPCS Codes
-- =====================================================

CREATE TABLE hcpcs_codes (
    hcpcs_code VARCHAR(10) PRIMARY KEY,

    description TEXT NOT NULL,

    drug_indicator BOOLEAN NOT NULL
);

-- =====================================================
-- Place of Service
-- =====================================================

CREATE TABLE place_of_service (
    place_of_service_code CHAR(1) PRIMARY KEY,

    description VARCHAR(100) NOT NULL
);

-- =====================================================
-- Provider Service Statistics
-- =====================================================

CREATE TABLE provider_service_statistics (
    
    provider_npi BIGINT NOT NULL,

    hcpcs_code VARCHAR(10) NOT NULL,

    place_of_service_code CHAR(1) NOT NULL,

    total_beneficiaries INTEGER NOT NULL,

    total_services NUMERIC(12,2) NOT NULL,

    total_bene_day_services INTEGER NOT NULL,

    avg_submitted_charge NUMERIC(12,2) NOT NULL,

    avg_allowed_amount NUMERIC(12,2) NOT NULL,

    avg_payment_amount NUMERIC(12,2) NOT NULL,

    avg_standardized_amount NUMERIC(12,2) NOT NULL,

    CONSTRAINT fk_provider
        FOREIGN KEY (provider_npi)
        REFERENCES providers(npi),

    CONSTRAINT fk_hcpcs
        FOREIGN KEY (hcpcs_code)
        REFERENCES hcpcs_codes(hcpcs_code),

    CONSTRAINT fk_place
        FOREIGN KEY (place_of_service_code)
        REFERENCES place_of_service(place_of_service_code)
    
    PRIMARY KEY (
    provider_npi,
    hcpcs_code,
    place_of_service_code
    )
);

-- =====================================================
-- Indexes
-- =====================================================

CREATE INDEX idx_provider
ON provider_service_statistics(provider_npi);

CREATE INDEX idx_hcpcs
ON provider_service_statistics(hcpcs_code);

CREATE INDEX idx_state
ON providers(state);

CREATE INDEX idx_provider_type
ON providers(provider_type);