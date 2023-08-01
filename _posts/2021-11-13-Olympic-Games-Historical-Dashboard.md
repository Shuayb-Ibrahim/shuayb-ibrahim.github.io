--- 
title: The Ultimate Olympic Games Dashboard, visualising historical data about the modern olympic games <img src="/assets/images/code/languages/powerbi.png" height=25 width=25><img src="/assets/images/code/languages/sql.webp" height=60 width=40>
layout: posts
categories: 
  - Projects
tags:
  - SQL
  - Power BI
  - Olympic Games 
---

<img src="/assets/images/posts/olympic-games-historical-analysis/dashboard-capture.PNG" width=400vh height=300vh display=inline><img src="/assets/images/posts/olympic-games-historical-analysis/sql-capture.PNG" width=400vh height=300vh display=inline>

---
## Business Problem
The business problem is **“As a data analyst working at a news company you are asked to visualize data that will help readers understand how countries have performed historically in the summer Olympic Games. You also know that there is an interest in details about the competitors, so if you find anything interesting then don’t hesitate to bring that in also. The main task is still to show historical performance for different countries, with the possibility to select your own country.”**

Breaking down the task, I identified that I needed to create an interactive dashboard as I was asked to "visualise data... with the possibility to select your own country" and that the data I will be working with is data that has been collected over a long time period relating to performance of many nations in the Olympic Games.

---
## Data Collection & Table Structures
The necessary data was first put into a SQL database and afterwards transformed using the transformations that you can see below.
```SQL
SELECT	
		[ID],
		[Name] AS 'Olympian Name', -- renamed column
		CASE WHEN Sex='M' THEN 'Male' ELSE 'Female' END AS [Sex],-- Better name for filters and visualisations
		[Age],
		CASE WHEN [Age] <18 THEN 'Under 18'
			 WHEN [Age] BETWEEN 18 AND 25 THEN '18-25'
			 WHEN [Age] BETWEEN 25 AND 30 THEN '25-30'
			 WHEN [Age] > 30 THEN 'Over 30'
		END AS [Age Group],
		[Height],
		[Weight],
		[NOC] AS 'Nation Code', --Explained Abbreviation
		LEFT(Games, CHARINDEX(' ',Games)-1) AS [Year], --split column Games to isolate Year, based on space
--		RIGHT(Games, CHARINDEX(' ',Games)-1) AS [Season], -- split column Games to filter by season, based on space
--		[City], -- Not needed for the analysis
		[Sport],
		[Event],
		CASE WHEN Medal = 'NA' THEN 'Not Registered' ELSE Medal END AS [Medal] --Replaced NA with Not Registered
FROM [olympic_games].[dbo].[athletes_event_results]
WHERE RIGHT(Games,CHARINDEX(' ',REVERSE(Games))-1) = 'Summer'; --Where clause to isolate Summer Season 
```

---
## Data Model
As this is a view where dimensions and facts have been combined, the data model that is created in Power BI is one table. The query from previous step was loaded in directly.

<img src="/assets/images/posts/olympic-games-historical-analysis/data-model-capture.PNG" height=350vh>

---
## Calculations
The following calculations were created in the Power BI reports using DAX (Data Analysis Expressions). To lessen the extent of coding, the re-use of measures (measure branching) was emphasized:


```DAX
No. of Olympians = DISTINCTCOUNT( ‘Olympic Data'[ID] )

No. of Medals = COUNTROWS( ‘Olympic Data’ )

No. Of Medals (Registered) = CALCULATE( [No. of Medals], FILTER( ‘Olympic Data’, ‘Olympic Data'[Medal] = “Bronze” || ‘Olympic Data’ [Medal] = “Gold” || ‘Olympic Data'[Medal] = “Silver” ))
```
---
## Dashboard

The finished dashboard consist of visualizations and filters that gives an easy option for the end users to navigate the summer games through history. Some possibilities are to filter by period using year, nation code to focus on one country or look into either a competitor or specific sports over time.

**Click on the image to use the dashboard**

<a href="https://app.powerbi.com/view?r=eyJrIjoiODY2OWQ5ZjAtYWIxNy00MDdlLWExYTEtZDRiMzY2YzdkZWMxIiwidCI6IjUwMDYzZDAzLTZjM2UtNGEzOC04MWY3LWQ5MWMwZjQyOTZjNyJ9">
     <img alt="Dashboard" src="/assets/images/posts/olympic-games-historical-analysis/dashboard-capture.PNG">
</a>
