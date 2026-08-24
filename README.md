# Does-the-London-Fire-Brigade-meet-its-6-minute-response-target-equally-across-London-
Project Analysis: Does the London Fire Brigade meet its 6 minute response target equally across London?

# The Findings
London Fire Brigade are able to meet its published pan-London target of a 6 minute and that is 360 seconds. 
Two boroughs which i will compare is Hillingdon and Kensington and Chelsea. Hillingdon was the slowest whilst Kensington and Chelsea were the fastest borough for LFB(London Fire Brigade) to reach. 

# Why this matters
LFB reports performance as a single pan-London average. On that measure the service passes. Measuring borough by borough shows residents of outer boroughs wait consistently longer than the target the Brigade sets itself. 

# Data
<img width="857" height="282" alt="image" src="https://github.com/user-attachments/assets/2e23e09b-3b5a-425f-bbf4-af5ee4fc1e7d" />

# Scope 
2026 was excluded. The file ended at 30 June 2026. Including half year alongside full 2024 and 2025 would show false 50% drop in incident volume. Therefore analysis covers 2024 and 2025 only, with 272,104 incidents. 

Out of that 13,989 incidents which makes up 5.1% have no recorded first pump attendance time (how long it takes for fire truck to reach to an incident). 

<img width="882" height="262" alt="image" src="https://github.com/user-attachments/assets/3fc63456-e2b9-4561-ba83-9754316d9bf2" />

Most of the missing time were in the special services which was 90%. These are non fire call outs like flooding, lockout, lift releases and many of which are not blue light dispatches and therefore have no meaningful dispatch to arrive clock. However the special services reports are unevely distributed across boroughs so including them would compare different mixes of work rather than comparing response speed. 

This analysis uses Fire and False Alarm only, where the data is whopping 99% complete.

Fire and False Alarm: 
A false alarm is dispatched exactly same as a fire, the call rings, engine is turned on, drives to address. The only difference is once it arrives and clock stops. 

Nulls were excluded. Missing attendance times are under 1%. 

**Note on missing data distribution****
Missing times( incident did not have a recorded time it took to reach) were more common in inner london (Tower hamlets 8.8%, Hackney 7.9%), than outer (Bromley 3.6%, Croydon 3.9%). This tracks the higher share of Special Service callouts in inner boroughs.

#My Findings
**1. 114 seconds spread between boroughs****
Slowest: Hillingdon 385s, Havering 372s, Bromley 372s, Enfield 360s. Fastest: Kensington and Chelsea 271s, Lambeth 273s, Tower Hamlets 282s.
(Times according to LFB are measured in seconds for how long it took truck to reach incident)

Across the scoped set, the mean is 320 seconds and the median 300 seconds. 70% of individual responses arrive within 6 minutes. The target is defined as an average rather than a percentage, so this is not a breach, but it shows how much variation sits behind the headline figure.

**2. Station count does not explain the gap.****

My first hypothesis was that slower boroughs have fewer fire station. BUT I WAS WRONG.
<img width="861" height="311" alt="image" src="https://github.com/user-attachments/assets/ace966ac-f4eb-4a44-bdd4-585cb95a98cd" />
Bromley has more than twice the stations of Kensington and Chelsea and is 101 seconds slower. What matters is how much ground each station has to cover, not how many there are

**3. Cover from a neighbouring station costs 115 seconds..****
When the first engine comes from a station other than the one whose ground the incident sits on, the local station was unavailable and a neighbour covered.

<img width="875" height="158" alt="image" src="https://github.com/user-attachments/assets/21708b11-9607-4b9a-8cb9-c6481475be97" />

29% of responses required cover from outside the local station ground.

**4. The borough-level pattern reverses, and that is the interesting part**
If out-of-ground cover costs two minutes, the boroughs relying on it most should be slowest. They are the fastest.

<img width="852" height="365" alt="image" src="https://github.com/user-attachments/assets/8604edda-6060-4d0c-a18f-cf2547d82a04" />

**5. Hillingdon is a different problem.**

Hillingdon's out-of-ground penalty is 112 seconds. Its local station response averages 349 seconds, the highest in London.

Hillingdon is slow even when its own station responds. Availability is not the cause there. The distances involved are, and no amount of improving appliance availability would fix it.

Conclusion

Two distinct causes sit behind the borough gap.

Boroughs such as Havering, Redbridge and Enfield are slow when local cover fails, because the fallback station is far away. This is an availability problem and could in principle be improved by resourcing.

Hillingdon is slow at baseline, before availability is considered. This is a geographic coverage problem and resourcing existing stations would not address it.

Reporting a single pan-London average obscures both. A borough-level breakdown, or a percentage-within-target measure alongside the average, would make the variation visible.

#Data download
Due to large file size I could not upload here but you can see it on London fire brigade official website: 
https://data.london.gov.uk/dataset/london-fire-brigade-incident-records-em8xy

