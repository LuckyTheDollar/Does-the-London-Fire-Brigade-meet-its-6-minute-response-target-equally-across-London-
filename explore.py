import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE incident AS SELECT * FROM read_csv_auto('lfb.csv', sample_size=-1)")

results = con.execute("""

SELECT
    ProperCase AS Borough,
    COUNT(*) AS Total_Incidents,
    ROUND(100.0 * AVG(CASE WHEN LOWER(TRIM(IncidentStationGround)) != LOWER(TRIM(FirstPumpArriving_DeployedFromStation))
                           THEN 1 ELSE 0 END), 2) AS Pct_Out_Of_Ground,
    ROUND(AVG(FirstPumpArriving_AttendanceTime), 0) AS Average_Time

FROM incident

WHERE CalYear IN (2024, 2025)
  AND IncidentGroup IN ('Fire', 'False Alarm')
  AND FirstPumpArriving_AttendanceTime IS NOT NULL

GROUP BY ProperCase
ORDER BY Pct_Out_Of_Ground DESC

""").df()

print(results)