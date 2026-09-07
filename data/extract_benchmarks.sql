-- Provenance for data/nonprofit_award_benchmarks_fy2021.csv.
--
-- Source: USASpending.gov public bulk-download API
-- (POST https://api.usaspending.gov/api/v2/bulk_download/awards/), prime award types
-- 02/03/04/05 (grants), action_date within FY2021, loaded into a local SQLite table
-- `grant_awards` (112 USASpending columns + source_file + fiscal_year).
--
-- The full FY2021 database (~2.2GB) is not bundled with this repo. This query is provided
-- so the benchmark table can be regenerated against a fresh pull of the same public dataset,
-- or extended to other fiscal years.

SELECT
  cfda_number,
  cfda_title,
  awarding_agency_name,
  COUNT(*) AS award_count,
  CAST(ROUND(AVG(CAST(federal_action_obligation AS REAL))) AS INTEGER) AS avg_award_amount,
  CAST(MIN(CAST(federal_action_obligation AS REAL)) AS INTEGER) AS min_award_amount,
  CAST(MAX(CAST(federal_action_obligation AS REAL)) AS INTEGER) AS max_award_amount,
  COUNT(DISTINCT recipient_state_code) AS states_represented
FROM grant_awards
WHERE business_types_description LIKE '%NONPROFIT WITH 501C3%'
  AND cfda_number IS NOT NULL AND cfda_number <> ''
  AND CAST(federal_action_obligation AS REAL) > 0
GROUP BY cfda_number, cfda_title, awarding_agency_name
HAVING award_count >= 5
ORDER BY award_count DESC
LIMIT 500;
