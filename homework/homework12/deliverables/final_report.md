# Final Report — Stage 12

## Executive Summary
- Baseline scenario delivers stable returns with moderate risk.  
- Scenario A (alt_impute) slightly reduces performance compared to baseline.  
- Scenario B (alt_outlier) improves average return but raises volatility.  

## Key Charts & Interpretation

### Scatter: Risk vs Return
- **What it shows:** Volatility vs average return for each scenario.  
- **Key insight:** Higher risk links to higher return; best points are on the efficient frontier.  
- **Assumption:** Sample is representative; outliers may distort results.  

![risk_return](deliverables/images/risk_return.png)

### Bar: Return by Scenario
- **What it shows:** Average return across Baseline and alternative scenarios.  
- **Key insight:** Baseline > alt_impute; alt_outlier > baseline.  
- **Assumption:** Based on historical averages; sensitive to sample size.  

![return_by_scenario](deliverables/images/return_by_scenario.png)

### Line: MetricA Over Time
- **What it shows:** MetricA trend across scenarios over time.  
- **Key insight:** Upward trend overall; baseline recovers faster than alt_impute.  
- **Assumption:** Data quality is consistent; short spikes may be noise.  

![metricA_trend](deliverables/images/metricA_trend.png)

## Assumptions & Risks
- Data is assumed clean and consistent across the time horizon.  
- Relationships between variables are stable; no regime shifts.  
- Risks include sensitivity to imputation method and volatility spikes.  

## Sensitivity Analysis Summary
- **Baseline:** Average return stable.  
- **Alt_impute:** Δ vs baseline = slight decrease in average return.  
- **Alt_outlier:** Δ vs baseline = noticeable increase in average return, with higher volatility.  
- **Interpretation:** Even small assumption changes cause meaningful shifts in outcome.  

(Full results exported to: `deliverables/sensitivity_table.csv`)  

## Decision Implications (What this means for you)
- Prediction holds if volatility and data quality remain within historical ranges.  
- Model/report is sensitive to imputation and outlier handling.  
- Stakeholder takeaway: Baseline is conservative and reliable; alt_outlier offers upside with higher risk.  
- Recommendation: adopt baseline/alt_impute for stability, monitor metrics weekly, and revisit assumptions if deviations exceed thresholds.  
