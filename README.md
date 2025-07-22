# 🏗️ Building Site Selection and Protection

An ArcGIS-based model integrating machine learning and time series analysis for optimized building site selection and protection in disaster-prone areas.

---

## 📖 Introduction

Frequent natural disasters make building site selection and protection increasingly complex. Traditional mechanisms for disaster insurance and resource allocation often lack efficiency and foresight.  
This project proposes an optimization framework that combines geographic data, machine learning, and time series forecasting to support spatial planning decisions. Mexico City is used as a case study area.

---

## 📁 Data Overview

### 🔍 1. Disaster Insurance Decision-Making Indicators

- [Number of Natural Disaster Events](https://ourworldindata.org/grapher/number-of-natural-disaster-events)  
- [Direct Economic Loss from Disasters](https://ourworldindata.org/grapher/direct-economic-loss-attributed-to-disasters)  
- [GDP Share of Disaster Loss](https://ourworldindata.org/explorers/natural-disasters?tab=map&time=2020&Disaster+Type=All+disasters&Impact=Economic+damages+%28%25+GDP%29&Timespan=Decadal+average&Per+capita=false&country=~OWID_WRL)

### 🗺️ 2. Building Site Selection – Six Risk Indicators

- **Population Density**  
   [Our World in Data – Population Density](https://ourworldindata.org/explorers/population-and-demography?indicator=Population+density&Sex=Both+sexes&Age=Total&Projection+scenario=None&country=CHN~IND~USA~IDN~PAK~NGA~BRA~JPN)

- **Geological Hazards** (Earthquakes, Floods, Volcanoes)  
   [EM-DAT – The International Disaster Database](https://www.emdat.be/)

- **Forest Fires**  
   [Global Forest Watch – Mexico Fire Dashboard](https://www.globalforestwatch.org/dashboards/country/MEX/?category=fires&location=WyJjb3VudHJ5IiwiTUVYIl0%3D)

---

## 📦 Data Sources and Licenses

### 🔹 Our World in Data

Some datasets in this repository are sourced from [Our World in Data](https://ourworldindata.org/), a project of the **Global Change Data Lab**, a UK-based nonprofit (Charity No. 1186433).  

- **License:** [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
- **Usage:** Freely share, adapt, and use with appropriate attribution.  
- **Tools/software:** Licensed under MIT.  
- See: [About & Licensing](https://ourworldindata.org/about#licensing-and-how-to-cite)

---

### 🔹 EM-DAT (CRED / UCLouvain)

Disaster records were sourced from [EM-DAT: The International Disaster Database](https://public.emdat.be/), maintained by the **Centre for Research on the Epidemiology of Disasters (CRED)** at **Université catholique de Louvain (UCLouvain)**.

> **Citation:**  
> *EM-DAT: The International Disaster Database – Université catholique de Louvain (UCLouvain), CRED, Belgium – [www.emdat.be](https://www.emdat.be)*

---

### 🔹 Global Forest Watch (GFW)

Forest fire and land use data were sourced from [Global Forest Watch (GFW)](https://www.globalforestwatch.org/), a platform offering high-quality forest-related data.

- **License:** [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
- **Usage:** Openly accessible for both commercial and non-commercial use with proper attribution.  
- Some datasets on GFW may originate from third parties and carry separate terms.  
- Official portal: [https://data.globalforestwatch.org](https://data.globalforestwatch.org)

> Please **do not imply endorsement** by GFW or use their logos.

---
