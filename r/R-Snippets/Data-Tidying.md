---
layout: archive
title: "Data Tidying"
permalink: /code/Data-Tidying
author_profile: true
redirect_from: Data-Tidying
---

In R, there is a consistent way to organise your data using a system called **tidy data**. Once you have tidy data and the tidy tools provided by packages in the tidyverse, you will spend much less time munging data from one representation to another.

The package of interest here that provides a bunch of tools to help tidy up messy datasets is tidyr, which is part of the tidyverse package.

```r
library(tidyverse)
```

There are three interrelated rules that make a dataset tidy:

1.  Each variable is a column; each column is a variable
2.  Each observation is a row; each row is an observation
3.  Each value is a cell, each cell is a single value

### Lengthening Data

tidyr provides two functions for pivoting data. The first of the two is the pivot_longer() function.

```r
billboard
```

In this dataset, each observation is a song. The first three columns (`artist`, `track` and `date.entered`) are variables that describe the song. Then we have 76 columns (`wk1`-`wk76`) that describe the rank of the song in each week.

To tidy this, we use pivot_longer():

```r
billboard |> 
  pivot_longer(
    cols = starts_with("wk"),
    names_to = "Week",
    values_to = "Rank",
    values_drop_na = TRUE
  )
```

To make future computations easier, we will convert values of week from strings to integers:

```r
billboard |> 
  pivot_longer(
    cols = starts_with("wk"),
    names_to = "Week",
    values_to = "Rank",
    values_drop_na = TRUE
  ) |> 
  mutate(Week = parse_number(Week))
```

#### Many variables in column names

There are times when you have multiple pieces of information crammed into the column names, and you would like to store these in separate new variables.

Example in the WHO2 dataset (by the World Health Organisation):

```r
who2
```

There are two columns that are already variables and are easy to interpret: `country` and `year`. They are followed by 56 columns like `sp_m_014`, `ep_m_4554`, and `rel_m_3544`.

Each column name is made up of three pieces separated by `_`. The first piece, `sp`/`rel`/`ep`, describes the method used for the diagnosis, the second piece, `m`/`f` is the `gender` (coded as a binary variable in this dataset), and the third piece, `014`/`1524`/`2534`/`3544`/`4554`/`5564`/`65` is the `age` range (`014` represents 0-14, for example).

The solution to fixing this:

```r
who2 |> 
  pivot_longer(
    cols = !(country:year),
    names_to = c("diagnosis", "gender", "age"),
    names_sep = "_",
    values_to = "count"
  )
```

#### Data and variable names in the column headers

There are also times when the column names include a mix of variable values and variable names:

```r
household
```

This dataset contains data about five families, with the names and dates of birth of up to two children. To make this dataset tidy:

```r
household |> 
  pivot_longer(
    cols = !family,
    names_to = c(".value","child"),
    names_sep = "_",
    values_drop_na = TRUE
  )
```

When you use `".value"` in `names_to`, the column names in the input contribute to both values and variable names in the output.

### Widening Data

Now looking at the second function, pivot_wider().

```r
cms_patient_experience
```

In this dataset, provided by the Centers of Medicare and Medicaid services, collects data about patient experiences.

The core unit being studied is an organization, but each organization is spread across six rows, with one row for each measurement taken in the survey organization. We can see the complete set of values for  `measure_cd` and `measure_title`  by using [`distinct()`](https://dplyr.tidyverse.org/reference/distinct.html):

```r
cms_patient_experience |> 
  distinct(measure_cd,measure_title)
```

`pivot_wider()` has the opposite interface to `pivot_longer()`: instead of choosing new column names, we need to provide the existing columns that define the values (`values_from`) and the column name (`names_from)`:

```r
cms_patient_experience |> 
  pivot_wider(
    names_from = measure_cd,
    values_from = prf_rate,
    id_cols = starts_with("org")
  )
```

The argument id_cols is the unique identifier for the observations to minimise redundant data, which takes columns.

#### Steps to using pivot_wider()

Example data frame :

```r
df <- tribble(
  ~id, ~measurement, ~value,
  "A",        "bp1",    100,
  "B",        "bp1",    140,
  "B",        "bp2",    115, 
  "A",        "bp2",    120,
  "A",        "bp3",    105
)
```

(ID: Patient A & B \| Measurement: bp1 & bp2 \| value: measurement)

1.  Figure out what will go in the rows and columns. The new column names will be the unique values of `measurement`.

    ```r
    df |> 
      distinct(measurement) |> 
      pull() 
    ```

2.  The variables that are not going into the new names or values are the id_cols.

    ```r
    df |> 
      select(-measurement, -value) |> 
      distinct()
    ```

The Solution:

```r
df |> 
  pivot_wider(
    names_from = measurement,
    values_from = value,
    id_cols = id
  )
```
