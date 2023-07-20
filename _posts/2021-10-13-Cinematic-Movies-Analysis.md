--- 
title: Cinematic Movies Analysis, exploring the factors that lead to a blockbuster production  <img src="/assets/images/code/languages/python.png" height=30 width=30>
layout: posts
categories:
  - Projects
tags:
  - Python
  - Movies 
---
 
The golden era of cinema may have ended in the 1960s with the 5 major studios no longer being able to block book theaters by law after the paramount case, however it gave birth to the Hollywood Renaissance which took place in the 1960s to the 1980s. This was when an influx of new, young and talented filmmakers with fresh ideas came to prominence in the United States. These directors have had a profound impact on what the modern era of cinema looks like today around the world, having given us some of the most iconic, inspiring and best selling movies of all time.

Up and coming directors, students of film and cinephiles may have all once wondered; what are the ingredients behind producing a high selling movie? Using a data-driven approach, I will do my best to answer that question.  

### The Approach

The purpose of this project is to explore the factors that lead to a successful high selling production with a focus on movies from the modern era of cinema (1980 onwards). I will be performing causal analysis to look at the correlation between different variables and the gross income of a movie which will be the measure of success for this analysis.

For this analysis, I will be using the [movie industry dataset](https://www.kaggle.com/danielgrijalvas/movies) which can be found on Kaggle. This dataset contains 4 decades worth of movie data which will be essential to carry out this study. 

Here is a summary of my approach:
- Getting the data from a csv file
- Cleaning and preparing the data for analysis
- Finding correlations in the data
- Drawing a conclusion based on the results

Now, let's start retrieving the data.

## Getting the Data 


```python
# standard imports 
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# configuring plot  
%matplotlib inline
matplotlib.rcParams['figure.figsize'] = (12,8)

# read in the data
df = pd.read_csv("movies-data\movies.csv")
```


```python
# first 5 rows of the data frame
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>rating</th>
      <th>genre</th>
      <th>year</th>
      <th>released</th>
      <th>score</th>
      <th>votes</th>
      <th>director</th>
      <th>writer</th>
      <th>star</th>
      <th>country</th>
      <th>budget</th>
      <th>gross</th>
      <th>company</th>
      <th>runtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Shining</td>
      <td>R</td>
      <td>Drama</td>
      <td>1980</td>
      <td>June 13, 1980 (United States)</td>
      <td>8.4</td>
      <td>927000.0</td>
      <td>Stanley Kubrick</td>
      <td>Stephen King</td>
      <td>Jack Nicholson</td>
      <td>United Kingdom</td>
      <td>19000000.0</td>
      <td>46998772.0</td>
      <td>Warner Bros.</td>
      <td>146.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Blue Lagoon</td>
      <td>R</td>
      <td>Adventure</td>
      <td>1980</td>
      <td>July 2, 1980 (United States)</td>
      <td>5.8</td>
      <td>65000.0</td>
      <td>Randal Kleiser</td>
      <td>Henry De Vere Stacpoole</td>
      <td>Brooke Shields</td>
      <td>United States</td>
      <td>4500000.0</td>
      <td>58853106.0</td>
      <td>Columbia Pictures</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Star Wars: Episode V - The Empire Strikes Back</td>
      <td>PG</td>
      <td>Action</td>
      <td>1980</td>
      <td>June 20, 1980 (United States)</td>
      <td>8.7</td>
      <td>1200000.0</td>
      <td>Irvin Kershner</td>
      <td>Leigh Brackett</td>
      <td>Mark Hamill</td>
      <td>United States</td>
      <td>18000000.0</td>
      <td>538375067.0</td>
      <td>Lucasfilm</td>
      <td>124.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Airplane!</td>
      <td>PG</td>
      <td>Comedy</td>
      <td>1980</td>
      <td>July 2, 1980 (United States)</td>
      <td>7.7</td>
      <td>221000.0</td>
      <td>Jim Abrahams</td>
      <td>Jim Abrahams</td>
      <td>Robert Hays</td>
      <td>United States</td>
      <td>3500000.0</td>
      <td>83453539.0</td>
      <td>Paramount Pictures</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Caddyshack</td>
      <td>R</td>
      <td>Comedy</td>
      <td>1980</td>
      <td>July 25, 1980 (United States)</td>
      <td>7.3</td>
      <td>108000.0</td>
      <td>Harold Ramis</td>
      <td>Brian Doyle-Murray</td>
      <td>Chevy Chase</td>
      <td>United States</td>
      <td>6000000.0</td>
      <td>39846344.0</td>
      <td>Orion Pictures</td>
      <td>98.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#last 5 rows of the data frame
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>rating</th>
      <th>genre</th>
      <th>year</th>
      <th>released</th>
      <th>score</th>
      <th>votes</th>
      <th>director</th>
      <th>writer</th>
      <th>star</th>
      <th>country</th>
      <th>budget</th>
      <th>gross</th>
      <th>company</th>
      <th>runtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7663</th>
      <td>More to Life</td>
      <td>NaN</td>
      <td>Drama</td>
      <td>2020</td>
      <td>October 23, 2020 (United States)</td>
      <td>3.1</td>
      <td>18.0</td>
      <td>Joseph Ebanks</td>
      <td>Joseph Ebanks</td>
      <td>Shannon Bond</td>
      <td>United States</td>
      <td>7000.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>7664</th>
      <td>Dream Round</td>
      <td>NaN</td>
      <td>Comedy</td>
      <td>2020</td>
      <td>February 7, 2020 (United States)</td>
      <td>4.7</td>
      <td>36.0</td>
      <td>Dusty Dukatz</td>
      <td>Lisa Huston</td>
      <td>Michael Saquella</td>
      <td>United States</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Cactus Blue Entertainment</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>7665</th>
      <td>Saving Mbango</td>
      <td>NaN</td>
      <td>Drama</td>
      <td>2020</td>
      <td>April 27, 2020 (Cameroon)</td>
      <td>5.7</td>
      <td>29.0</td>
      <td>Nkanya Nkwai</td>
      <td>Lynno Lovert</td>
      <td>Onyama Laura</td>
      <td>United States</td>
      <td>58750.0</td>
      <td>NaN</td>
      <td>Embi Productions</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7666</th>
      <td>It's Just Us</td>
      <td>NaN</td>
      <td>Drama</td>
      <td>2020</td>
      <td>October 1, 2020 (United States)</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>James Randall</td>
      <td>James Randall</td>
      <td>Christina Roz</td>
      <td>United States</td>
      <td>15000.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>120.0</td>
    </tr>
    <tr>
      <th>7667</th>
      <td>Tee em el</td>
      <td>NaN</td>
      <td>Horror</td>
      <td>2020</td>
      <td>August 19, 2020 (United States)</td>
      <td>5.7</td>
      <td>7.0</td>
      <td>Pereko Mosia</td>
      <td>Pereko Mosia</td>
      <td>Siyabonga Mabaso</td>
      <td>South Africa</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>PK 65 Films</td>
      <td>102.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 7668 entries, 0 to 7667
    Data columns (total 15 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   name      7668 non-null   object 
     1   rating    7591 non-null   object 
     2   genre     7668 non-null   object 
     3   year      7668 non-null   int64  
     4   released  7666 non-null   object 
     5   score     7665 non-null   float64
     6   votes     7665 non-null   float64
     7   director  7668 non-null   object 
     8   writer    7665 non-null   object 
     9   star      7667 non-null   object 
     10  country   7665 non-null   object 
     11  budget    5497 non-null   float64
     12  gross     7479 non-null   float64
     13  company   7651 non-null   object 
     14  runtime   7664 non-null   float64
    dtypes: float64(5), int64(1), object(9)
    memory usage: 898.7+ KB
    

Here is the data we will be working with. We have 7667 movies in this dataset and each movie has the following attributes:
- name: name of the movie
- rating: rating of the movie (R, PG, etc.)
- genre: main genre of the movie.
- year: year of release
- released: release date 
- score: IMDb user rating
- votes: number of user votes
- director: the director
- writer: writer of the movie
- star: main actor/actress
- country: country of origin
- budget: the budget of a movie. Some movies don't have this, so it appears as 0
- gross: revenue of the movie
- company: the production company
- runtime: duration of the movie

### Cleaning and preparing the data for analysis


```python
# checking for missing data
for col in df.columns:
    pct_of_missing = np.mean(df[col].isnull())
    print("{} - {}%".format(col,pct_of_missing))
```

    name - 0.0%
    rating - 0.010041731872717789%
    genre - 0.0%
    year - 0.0%
    released - 0.0002608242044861763%
    score - 0.0003912363067292645%
    votes - 0.0003912363067292645%
    director - 0.0%
    writer - 0.0003912363067292645%
    star - 0.00013041210224308815%
    country - 0.0003912363067292645%
    budget - 0.2831246739697444%
    gross - 0.02464788732394366%
    company - 0.002217005738132499%
    runtime - 0.0005216484089723526%
    


```python
df = df.dropna()
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 5421 entries, 0 to 7652
    Data columns (total 15 columns):
     #   Column    Non-Null Count  Dtype  
    ---  ------    --------------  -----  
     0   name      5421 non-null   object 
     1   rating    5421 non-null   object 
     2   genre     5421 non-null   object 
     3   year      5421 non-null   int64  
     4   released  5421 non-null   object 
     5   score     5421 non-null   float64
     6   votes     5421 non-null   float64
     7   director  5421 non-null   object 
     8   writer    5421 non-null   object 
     9   star      5421 non-null   object 
     10  country   5421 non-null   object 
     11  budget    5421 non-null   float64
     12  gross     5421 non-null   float64
     13  company   5421 non-null   object 
     14  runtime   5421 non-null   float64
    dtypes: float64(5), int64(1), object(9)
    memory usage: 677.6+ KB
    


```python
# checking for missing data
for col in df.columns:
    pct_of_missing = np.mean(df[col].isnull())
    print("{} - {}%".format(col,pct_of_missing))
```

    name - 0.0%
    rating - 0.0%
    genre - 0.0%
    year - 0.0%
    released - 0.0%
    score - 0.0%
    votes - 0.0%
    director - 0.0%
    writer - 0.0%
    star - 0.0%
    country - 0.0%
    budget - 0.0%
    gross - 0.0%
    company - 0.0%
    runtime - 0.0%
    

The first thing I wanted to check was if there was missing data in the dataset. As shown we can see that there are NA values in the columns: rating, released, score, votes, writer, star, country, budget, gross, company and runtime. Incomplete entries in the data will produce inaccurate results therefore we will need to omit those movies. 

As shown, we can now see that the number of movies in the data have reduced from 7667 to 5421 movies and we have completed filtered out the incomplete entries.


```python
# split column released into released date and country of release
country_of_release = list()
release_date = list()

for entry in df['released'].astype(str):
    released = entry.strip(")").split("(",1)
    country_of_release.append(released[1])
    release_date.append(released[0])

df['release date'] = release_date
df['country of release'] = country_of_release

df = df.drop(columns='released')
```


```python
# data
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>rating</th>
      <th>genre</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>director</th>
      <th>writer</th>
      <th>star</th>
      <th>country</th>
      <th>budget</th>
      <th>gross</th>
      <th>company</th>
      <th>runtime</th>
      <th>release date</th>
      <th>country of release</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Shining</td>
      <td>R</td>
      <td>Drama</td>
      <td>1980</td>
      <td>8.4</td>
      <td>927000.0</td>
      <td>Stanley Kubrick</td>
      <td>Stephen King</td>
      <td>Jack Nicholson</td>
      <td>United Kingdom</td>
      <td>19000000.0</td>
      <td>46998772.0</td>
      <td>Warner Bros.</td>
      <td>146.0</td>
      <td>June 13, 1980</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Blue Lagoon</td>
      <td>R</td>
      <td>Adventure</td>
      <td>1980</td>
      <td>5.8</td>
      <td>65000.0</td>
      <td>Randal Kleiser</td>
      <td>Henry De Vere Stacpoole</td>
      <td>Brooke Shields</td>
      <td>United States</td>
      <td>4500000.0</td>
      <td>58853106.0</td>
      <td>Columbia Pictures</td>
      <td>104.0</td>
      <td>July 2, 1980</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Star Wars: Episode V - The Empire Strikes Back</td>
      <td>PG</td>
      <td>Action</td>
      <td>1980</td>
      <td>8.7</td>
      <td>1200000.0</td>
      <td>Irvin Kershner</td>
      <td>Leigh Brackett</td>
      <td>Mark Hamill</td>
      <td>United States</td>
      <td>18000000.0</td>
      <td>538375067.0</td>
      <td>Lucasfilm</td>
      <td>124.0</td>
      <td>June 20, 1980</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Airplane!</td>
      <td>PG</td>
      <td>Comedy</td>
      <td>1980</td>
      <td>7.7</td>
      <td>221000.0</td>
      <td>Jim Abrahams</td>
      <td>Jim Abrahams</td>
      <td>Robert Hays</td>
      <td>United States</td>
      <td>3500000.0</td>
      <td>83453539.0</td>
      <td>Paramount Pictures</td>
      <td>88.0</td>
      <td>July 2, 1980</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Caddyshack</td>
      <td>R</td>
      <td>Comedy</td>
      <td>1980</td>
      <td>7.3</td>
      <td>108000.0</td>
      <td>Harold Ramis</td>
      <td>Brian Doyle-Murray</td>
      <td>Chevy Chase</td>
      <td>United States</td>
      <td>6000000.0</td>
      <td>39846344.0</td>
      <td>Orion Pictures</td>
      <td>98.0</td>
      <td>July 25, 1980</td>
      <td>United States</td>
    </tr>
  </tbody>
</table>
</div>



Looking at the 'released' column, I saw that it contained two seperate pieces of information which were the release date in full format and the country of release which the release date corresponds to. For the sake of data integrity, I decided to split that column into two columns called release date and country of release. 


```python
# variable data types
df.dtypes
```




    name                   object
    rating                 object
    genre                  object
    year                    int64
    score                 float64
    votes                 float64
    director               object
    writer                 object
    star                   object
    country                object
    budget                float64
    gross                 float64
    company                object
    runtime               float64
    release date           object
    country of release     object
    dtype: object




```python
# changing data type  
df['votes'] = df['votes'].astype('int64')
df['budget'] = df['budget'].astype('int64')
df['gross'] = df['gross'].astype('int64')
df.dtypes
```




    name                   object
    rating                 object
    genre                  object
    year                    int64
    score                 float64
    votes                   int64
    director               object
    writer                 object
    star                   object
    country                object
    budget                  int64
    gross                   int64
    company                object
    runtime               float64
    release date           object
    country of release     object
    dtype: object



After looking at the data types of the variables, I was not satisfied that the data type of a few variables matched the nature of the vairable perfectly. I changed the data type to integer as I feel that not only does it match the variable better but it is also easier on the eye. 


```python
# sorting data frame by gross income
df = df.sort_values(by=['gross'],ascending=False)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>rating</th>
      <th>genre</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>director</th>
      <th>writer</th>
      <th>star</th>
      <th>country</th>
      <th>budget</th>
      <th>gross</th>
      <th>company</th>
      <th>runtime</th>
      <th>release date</th>
      <th>country of release</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5445</th>
      <td>Avatar</td>
      <td>PG-13</td>
      <td>Action</td>
      <td>2009</td>
      <td>7.8</td>
      <td>1100000</td>
      <td>James Cameron</td>
      <td>James Cameron</td>
      <td>Sam Worthington</td>
      <td>United States</td>
      <td>237000000</td>
      <td>2847246203</td>
      <td>Twentieth Century Fox</td>
      <td>162.0</td>
      <td>December 18, 2009</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>7445</th>
      <td>Avengers: Endgame</td>
      <td>PG-13</td>
      <td>Action</td>
      <td>2019</td>
      <td>8.4</td>
      <td>903000</td>
      <td>Anthony Russo</td>
      <td>Christopher Markus</td>
      <td>Robert Downey Jr.</td>
      <td>United States</td>
      <td>356000000</td>
      <td>2797501328</td>
      <td>Marvel Studios</td>
      <td>181.0</td>
      <td>April 26, 2019</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>3045</th>
      <td>Titanic</td>
      <td>PG-13</td>
      <td>Drama</td>
      <td>1997</td>
      <td>7.8</td>
      <td>1100000</td>
      <td>James Cameron</td>
      <td>James Cameron</td>
      <td>Leonardo DiCaprio</td>
      <td>United States</td>
      <td>200000000</td>
      <td>2201647264</td>
      <td>Twentieth Century Fox</td>
      <td>194.0</td>
      <td>December 19, 1997</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>6663</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>PG-13</td>
      <td>Action</td>
      <td>2015</td>
      <td>7.8</td>
      <td>876000</td>
      <td>J.J. Abrams</td>
      <td>Lawrence Kasdan</td>
      <td>Daisy Ridley</td>
      <td>United States</td>
      <td>245000000</td>
      <td>2069521700</td>
      <td>Lucasfilm</td>
      <td>138.0</td>
      <td>December 18, 2015</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>7244</th>
      <td>Avengers: Infinity War</td>
      <td>PG-13</td>
      <td>Action</td>
      <td>2018</td>
      <td>8.4</td>
      <td>897000</td>
      <td>Anthony Russo</td>
      <td>Christopher Markus</td>
      <td>Robert Downey Jr.</td>
      <td>United States</td>
      <td>321000000</td>
      <td>2048359754</td>
      <td>Marvel Studios</td>
      <td>149.0</td>
      <td>April 27, 2018</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5640</th>
      <td>Tanner Hall</td>
      <td>R</td>
      <td>Drama</td>
      <td>2009</td>
      <td>5.8</td>
      <td>3500</td>
      <td>Francesca Gregorini</td>
      <td>Tatiana von Fürstenberg</td>
      <td>Rooney Mara</td>
      <td>United States</td>
      <td>3000000</td>
      <td>5073</td>
      <td>Two Prong Lesson</td>
      <td>96.0</td>
      <td>January 15, 2015</td>
      <td>Sweden</td>
    </tr>
    <tr>
      <th>2434</th>
      <td>Philadelphia Experiment II</td>
      <td>PG-13</td>
      <td>Action</td>
      <td>1993</td>
      <td>4.5</td>
      <td>1900</td>
      <td>Stephen Cornwell</td>
      <td>Wallace C. Bennett</td>
      <td>Brad Johnson</td>
      <td>United States</td>
      <td>5000000</td>
      <td>2970</td>
      <td>Trimark Pictures</td>
      <td>97.0</td>
      <td>June 4, 1994</td>
      <td>South Korea</td>
    </tr>
    <tr>
      <th>3681</th>
      <td>Ginger Snaps</td>
      <td>Not Rated</td>
      <td>Drama</td>
      <td>2000</td>
      <td>6.8</td>
      <td>43000</td>
      <td>John Fawcett</td>
      <td>Karen Walton</td>
      <td>Emily Perkins</td>
      <td>Canada</td>
      <td>5000000</td>
      <td>2554</td>
      <td>Copperheart Entertainment</td>
      <td>108.0</td>
      <td>May 11, 2001</td>
      <td>Canada</td>
    </tr>
    <tr>
      <th>272</th>
      <td>Parasite</td>
      <td>R</td>
      <td>Horror</td>
      <td>1982</td>
      <td>3.9</td>
      <td>2300</td>
      <td>Charles Band</td>
      <td>Alan J. Adler</td>
      <td>Robert Glaudini</td>
      <td>United States</td>
      <td>800000</td>
      <td>2270</td>
      <td>Embassy Pictures</td>
      <td>85.0</td>
      <td>March 12, 1982</td>
      <td>United States</td>
    </tr>
    <tr>
      <th>3203</th>
      <td>Trojan War</td>
      <td>PG-13</td>
      <td>Comedy</td>
      <td>1997</td>
      <td>5.7</td>
      <td>5800</td>
      <td>George Huang</td>
      <td>Andy Burg</td>
      <td>Will Friedle</td>
      <td>United States</td>
      <td>15000000</td>
      <td>309</td>
      <td>Daybreak</td>
      <td>85.0</td>
      <td>October 1, 1997</td>
      <td>Brazil</td>
    </tr>
  </tbody>
</table>
<p>5421 rows × 16 columns</p>
</div>




```python
# dropping for duplicate data

df = df.drop_duplicates()
```

Finally, I have dropped all duplicate columns and made sure that the rows were sorted by gross earnings in descending order so that it is easier to see the list of top selling movies.

## Analysis

I will start by looking at a correlation matrix of the dataset and try to see if there are any interesting insights that can be taken away from in the numerical data. I will be using Pearson parametric correlation test.

### Correlation matrix for numerical variables


```python
correlation_matrix = df.corr(method="pearson")
correlation_matrix
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>budget</th>
      <th>gross</th>
      <th>runtime</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>year</th>
      <td>1.000000</td>
      <td>0.056386</td>
      <td>0.206021</td>
      <td>0.327722</td>
      <td>0.274321</td>
      <td>0.075077</td>
    </tr>
    <tr>
      <th>score</th>
      <td>0.056386</td>
      <td>1.000000</td>
      <td>0.474256</td>
      <td>0.072001</td>
      <td>0.222556</td>
      <td>0.414068</td>
    </tr>
    <tr>
      <th>votes</th>
      <td>0.206021</td>
      <td>0.474256</td>
      <td>1.000000</td>
      <td>0.439675</td>
      <td>0.614751</td>
      <td>0.352303</td>
    </tr>
    <tr>
      <th>budget</th>
      <td>0.327722</td>
      <td>0.072001</td>
      <td>0.439675</td>
      <td>1.000000</td>
      <td>0.740247</td>
      <td>0.318695</td>
    </tr>
    <tr>
      <th>gross</th>
      <td>0.274321</td>
      <td>0.222556</td>
      <td>0.614751</td>
      <td>0.740247</td>
      <td>1.000000</td>
      <td>0.275796</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>0.075077</td>
      <td>0.414068</td>
      <td>0.352303</td>
      <td>0.318695</td>
      <td>0.275796</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
correlation_matrix = df.corr(method="pearson")
sns.heatmap(correlation_matrix,annot=True)
plt.title("Correlation Matrix for Numeric Features")
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show()
```


    
![png](/images/posts/movies-casual-analysis/output_28_0.png)
    


Amongst the numeric features, we can see with this heatmap that there are two particular variables that have a strong positive correlation with gross earnings, budget and votes. They are the only two variables with a correlation greater than 0.5 with the variable, gross. The next variable with the strongest correlation has an r value of 0.26 so we can say that the correlation with the other variables, excluding budget and gross, is weak.

### Budget vs. Gross Earnings Plot


```python
# Budget vs. Gross scatter plot
sns.regplot(x="budget",y="gross",data=df,scatter_kws={"color":"blue"},line_kws={"color":"orange"}).set(
    title="Budget vs. Gross Earnings", xlabel="Budget (in millions)",ylabel="Gross income (in 100 millions)")

```




    [Text(0.5, 1.0, 'Budget vs. Gross Earnings'),
     Text(0.5, 0, 'Budget (in millions)'),
     Text(0, 0.5, 'Gross income (in 100 millions)')]




    
![png](/images/posts/movies-casual-analysis/output_31_1.png)
    


Looking at numerical data is not enough. What if the prestige of a company has a role to play in the success of a movie? Is it possible that the writer of the novel has a role to play in the success of the production? We will need to convert all the non-numerical data into numerical data and find out for sure.

### Correlation matrix for all variables


```python
# preparing dataframe
df_numerised = df

for col in df_numerised.columns:
    if(df_numerised[col].dtype == "object"):
        df_numerised[col] = df_numerised[col].astype("category")
        df_numerised[col] = df_numerised[col].cat.codes
        
df_numerised
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>rating</th>
      <th>genre</th>
      <th>year</th>
      <th>score</th>
      <th>votes</th>
      <th>director</th>
      <th>writer</th>
      <th>star</th>
      <th>country</th>
      <th>budget</th>
      <th>gross</th>
      <th>company</th>
      <th>runtime</th>
      <th>release date</th>
      <th>country of release</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5445</th>
      <td>386</td>
      <td>5</td>
      <td>0</td>
      <td>2009</td>
      <td>7.8</td>
      <td>1100000</td>
      <td>785</td>
      <td>1263</td>
      <td>1534</td>
      <td>47</td>
      <td>237000000</td>
      <td>2847246203</td>
      <td>1382</td>
      <td>162.0</td>
      <td>496</td>
      <td>47</td>
    </tr>
    <tr>
      <th>7445</th>
      <td>388</td>
      <td>5</td>
      <td>0</td>
      <td>2019</td>
      <td>8.4</td>
      <td>903000</td>
      <td>105</td>
      <td>513</td>
      <td>1470</td>
      <td>47</td>
      <td>356000000</td>
      <td>2797501328</td>
      <td>983</td>
      <td>181.0</td>
      <td>124</td>
      <td>47</td>
    </tr>
    <tr>
      <th>3045</th>
      <td>4909</td>
      <td>5</td>
      <td>6</td>
      <td>1997</td>
      <td>7.8</td>
      <td>1100000</td>
      <td>785</td>
      <td>1263</td>
      <td>1073</td>
      <td>47</td>
      <td>200000000</td>
      <td>2201647264</td>
      <td>1382</td>
      <td>194.0</td>
      <td>502</td>
      <td>47</td>
    </tr>
    <tr>
      <th>6663</th>
      <td>3643</td>
      <td>5</td>
      <td>0</td>
      <td>2015</td>
      <td>7.8</td>
      <td>876000</td>
      <td>768</td>
      <td>1806</td>
      <td>356</td>
      <td>47</td>
      <td>245000000</td>
      <td>2069521700</td>
      <td>945</td>
      <td>138.0</td>
      <td>498</td>
      <td>47</td>
    </tr>
    <tr>
      <th>7244</th>
      <td>389</td>
      <td>5</td>
      <td>0</td>
      <td>2018</td>
      <td>8.4</td>
      <td>897000</td>
      <td>105</td>
      <td>513</td>
      <td>1470</td>
      <td>47</td>
      <td>321000000</td>
      <td>2048359754</td>
      <td>983</td>
      <td>149.0</td>
      <td>132</td>
      <td>47</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5640</th>
      <td>3794</td>
      <td>6</td>
      <td>6</td>
      <td>2009</td>
      <td>5.8</td>
      <td>3500</td>
      <td>585</td>
      <td>2924</td>
      <td>1498</td>
      <td>47</td>
      <td>3000000</td>
      <td>5073</td>
      <td>1385</td>
      <td>96.0</td>
      <td>847</td>
      <td>41</td>
    </tr>
    <tr>
      <th>2434</th>
      <td>2969</td>
      <td>5</td>
      <td>0</td>
      <td>1993</td>
      <td>4.5</td>
      <td>1900</td>
      <td>1805</td>
      <td>3102</td>
      <td>186</td>
      <td>47</td>
      <td>5000000</td>
      <td>2970</td>
      <td>1376</td>
      <td>97.0</td>
      <td>1386</td>
      <td>39</td>
    </tr>
    <tr>
      <th>3681</th>
      <td>1595</td>
      <td>3</td>
      <td>6</td>
      <td>2000</td>
      <td>6.8</td>
      <td>43000</td>
      <td>952</td>
      <td>1683</td>
      <td>527</td>
      <td>6</td>
      <td>5000000</td>
      <td>2554</td>
      <td>466</td>
      <td>108.0</td>
      <td>1628</td>
      <td>8</td>
    </tr>
    <tr>
      <th>272</th>
      <td>2909</td>
      <td>6</td>
      <td>9</td>
      <td>1982</td>
      <td>3.9</td>
      <td>2300</td>
      <td>261</td>
      <td>55</td>
      <td>1473</td>
      <td>47</td>
      <td>800000</td>
      <td>2270</td>
      <td>582</td>
      <td>85.0</td>
      <td>1442</td>
      <td>47</td>
    </tr>
    <tr>
      <th>3203</th>
      <td>4966</td>
      <td>5</td>
      <td>4</td>
      <td>1997</td>
      <td>5.7</td>
      <td>5800</td>
      <td>651</td>
      <td>161</td>
      <td>1811</td>
      <td>47</td>
      <td>15000000</td>
      <td>309</td>
      <td>504</td>
      <td>85.0</td>
      <td>2021</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>5421 rows × 16 columns</p>
</div>



As you can see we have converted the entire dataframe into numerical data. It is now ready for correlation analysis. Let's have a look at the results.


```python
# correlation matrix
correlation_matrix = df_numerised.corr(method="pearson")
sns.heatmap(correlation_matrix,annot=True)
plt.title("Correlation Matrix for Numeric Features")
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show()
```


    
![png](/images/posts/movies-casual-analysis/output_36_0.png)
    



```python
# pairs of variables with a strong postive correlation
correlation_matrix = df_numerised.corr()

corr_pairs = correlation_matrix.unstack()
sorted_pairs = corr_pairs.sort_values()
high_corr = sorted_pairs[(sorted_pairs > 0.5)] 
high_corr
```




    gross               votes                 0.614751
    votes               gross                 0.614751
    budget              gross                 0.740247
    gross               budget                0.740247
    name                name                  1.000000
    runtime             runtime               1.000000
    company             company               1.000000
    gross               gross                 1.000000
    budget              budget                1.000000
    country             country               1.000000
    star                star                  1.000000
    writer              writer                1.000000
    director            director              1.000000
    votes               votes                 1.000000
    score               score                 1.000000
    year                year                  1.000000
    genre               genre                 1.000000
    rating              rating                1.000000
    release date        release date          1.000000
    country of release  country of release    1.000000
    dtype: float64



After looking at the correlation matrix for all the variables, we can see that the only two variables that have a strong positive correlation with gross earnings remain budget and votes. All of the categorical variables in fact have shown no real correlation and has not changed the initial results.

## Conclusion

So, to answer the question: what are the ingredients behind producing a high selling movie? Well if I was going to answer it in one word it would be budget. The results have shown that the greater the budget, the greater the gross income of the film is. We can also justify this correlation as well. The budget often covers costs of acquiring the script, payments to talent, and production costs. The online popularity of the movie also has a high correlation to the gross earnings of a movie. Increasing online presence on cinematography platforms such as IMBD plays a role in the success of the movie you produce.  

Contrary to the question, we can also say that the production company name has no value to the success of the movie. In the past, this would have been different but in this new modern age the young student of film does not need to work for an elite production company to produce a blockbuster fortunately. Unfortunately, they would need a lot of money. 
