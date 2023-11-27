---
layout: archive
title: "Data Import"
permalink: /code/Data-Import
author_profile: true
redirect_from: Data-Import
---

With R, you can read data from multiple files at once and writing data from R to a file.

#### Prerequisites
```r
library(tidyverse)
```

## Reading data from a file
To begin, we will focus on the most common data file type: CSV (Comma-separated values). In a CSV file, the first row is the the header row which gives us the column names
```
Student ID,Full Name,favourite.food,mealPlan,AGE
1,Sunil Huffmann,Strawberry yoghurt,Lunch only,4
2,Barclay Lynn,French fries,Lunch only,5
3,Jayendra Lyne,N/A,Breakfast and lunch,7
4,Leon Rossini,Anchovies,Lunch only,
5,Chidiegwu Dunkel,Pizza,Breakfast and lunch,five
6,Güvenç Attila,Ice cream,Lunch only,6
```
