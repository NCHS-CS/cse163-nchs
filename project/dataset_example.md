# Datasets Example 

:::{note}
Here is a short example. Your dataset documentation is likely to be longer!
:::

## Datasets Summary:

All the data can be found on this [Fake link to Google Folder](https://support.google.com/drive/answer/7166529?hl=en).  

This shows that we are using only three datasets.

|DataSet|Source|Size|Notes|
|-------|------|----|-----|
|Report_Card_Graduation_2018-19.csv| Your link must be a deep link that goes to the data like this:<br> [catalog.data.gov](https://catalog.data.gov/dataset/report-card-graduation-2018-19/resource/7ecfc182-8237-4c5f-a2d1-14377a249e4e)| 81,267 |Graduation information for washington state.|
|teachers_2014.csv|<a href="https://data.gov">data.gov</a>|48x10|Contains full-time teacher pay and benefits by school district|
|geo_wa_counties.json|[Natural Earth](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/)|NA|Contains geometry data for the counties in Washington state|

### Graduation_2018.csv

This dataset contains graduation rates of high school students in the year 2018 only. The rates are by race and school district.

|Column|Description|
|------|-----------|
|DistrictName|string: The name of the school district|
|County|string: A list of county names that the school district is in. A district may span multiple counties|
|StudentGroup|string: The race of the students in this row. Races included are [`White`, `Hispanic/ Latino of any race(s)`, `Black/ African American`, `Asian`...]|
|GraduationRate|double: The percent of students of this race that graduated high school in four years.|

### Teachers_2014.csv

This dataset contains salary & benefits information for full-time teachers by school district in the year 2014.  

|Column|Description|
|------|-----------|
|DNUM|integer: The number for the school district. For example, Northshore is 417.|
|PERV|integer: The number of personal vacation days that a teacher gets per year.|
|BASE|double: The Base salary of a full-time teacher.|
|HRPAY|double: The additional pay given to a teacher beyond their base salary for simply being a teacher.|
|SPST|double: The average additional pay (stipend) given to a teacher for coaching a sport.|
|APST|double: The additional pay (stipend) given to an AP Teacher.|

### Data Challenges

The datasets come from different years because we could not get accurate data for both sets during the same year. If we correlate the data across different years, we are not representing the true data. We need to highlight this!  

While the teacher pay dataset is extensive, there is no single column that gives a simple summary how much an "average" teacher makes. This is because we don't know how many teachers receive certain types of stipends.   

It would be valuable to track the changes of graduation rates over time as related to the changes of salary over time. I will be doing some extra work to find more datasets to allow graphing over time.  

The School Districts don't map easily across datasets. One dataset uses a number while the other uses a string. I may need to manually create a mapping dataset that allows me to join the two together.  

It would be good to geospatially plot graduation rates, but the geometry data that I've found so far is only by county while the school districts can span many counties. I may have to manually pick, or randomly guess, which county a school district mostly represents. Or, perhaps I can locate geometry for the school districts themselves. 
