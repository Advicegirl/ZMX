# Finder Automation 

**Guides**

**1. Download data from finder table "Monthly Traffic/PV by Channel Data"**

**2. Copy the path of the downloaded Excel file**

**3. Running the code**

```
  cd Desktop
  git clone https://github.com/EvelynZhaoZMX/ZMX.git
  python ZMX/Finder.py
```
**4. Input the path as required**

```
  eg. /Users/joinjaye/Downloads/PV by Channel Data_20241009.xlsx
```

**5. Paste the result of resultDF to the Excel sheet**

**6. Manually Check channels that failed to be matched**

# Fetching Monthly Traffic Data from Google Analytic 

**Guides**

**1.   Export report(data) from Google Analytics to Google Sheets**

*   Set time period (Month)
*   Add "Session source / medium" as the second column
*   Share this report -> Download file -> Export to Google Sheets

**2.   Input the link of the sheet as "csv_url"**

*   Share -> Anyone with the link & Editor -> Copy link

**3.   Copy target channel names(Web column) from the Excel sheet as "inputs"**

**4.   Paste the "Sessions" column of resultDF to the Excel sheet**

**5.   Manually Check channels that were failed to be matched on Google Analytics**
