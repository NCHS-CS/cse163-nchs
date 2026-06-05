---
title: Pandas DF
---

# DataFrame

## Table of Contents
- [Creating a DataFrame](#creating-a-dataframe)
- [DataFrame Indexing Methods](#dataframe-indexing-methods)
  - [Argument Types](#argument-types)
  - [API Details](#api-details)
  - [Examples](#examples)
- [Iterating a DataFrame](#iterating-a-dataframe)
- [Accessing/Changing Attributes & Values](#accessingchanging-attributes--values)
- [Handy Solutions to Common problems](#handy-solutions-to-common-problems)

Here we will review common and useful actions with a DataFrame.  

First, it is helpful to understand how the Pandas [DataFrame documentation](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) is structured. Painfully, it is not alphabetic! However, wonderfully, it is structured by activity.  

## Creating a DataFrame
**Creating from a list of dictionaries**  
Each dictionary is a row in the `DataFrame`. Each key in the dictionary is the column name with a value for the cell. 
```python
d1 = { 'City':'New York', 'Pop': 8.6, 'Rating': 3 }
d2 = { 'City':'Seattle', 'Pop': .8, 'Rating': 4 }
d3 = { 'City':'Los Angeles', 'Pop': 3.9, 'Rating': 3.5 }
d4 = { 'City':'Houston', 'Pop': 2.1, 'Rating': 4.1 }
my_list = [d1, d2, d2, d4]
pd = pd.DataFrame(my_list)

# The above creates a DataFrame with 4 rows, 3 columns.
# The column names are: 'City', 'Pop', and 'Rating'
```

**Creating from a list of lists**  
In this list of lists, each inner list is a row.  
```python
# This will have 5 rows, 3 columns, using default indexing.
# The column names are provided in the constructor below
data = [["New York", 8.6, 20],
        ["Chicago", 2.7, 20],
        ["Los Angeles", 3.9, 20],
        ["Philadelphia", 1.5, 20],
        ["Houston", 2.1, 20]]
 
# Give names to the columns when constructing
df = pd.DataFrame(data, columns=["City", "Population", "Year(2020)"])
```

**Creating by adding columns**  
Here, we create an empty `DataFrame` and then add on columns.  
```python
df = pd.DataFrame()
# add a column with the name 'seat_number'
df['seat_number'] = [ 1, 2, 3, 4 ]
# add a columns with the name 'student_id`
df['student_id'] = [ 1113, 1125, 1427, 1211]

# df has 4 rows, 2 columns, using default indexing.
```

**Creating from a dictionary**  
The keys are the column names, the values are lists of column values. 
```python
data = { "New York": [8.6, 20],
         "Chicago": [2.7, 20],
         "Los Angeles": [3.9, 20],
         "Philadelphia": [1.5, 20],
         "Houston": [2.1, 20]
       }
# creates 5 columns, 2 rows, default indexing
df = pd.DataFrame(data)
```
> The structure of the dictionary can take many forms. To see the various structures
> take a look at the converse function <a href="https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.DataFrame.to_dict.html" target="_blank">DataFrame.to_dict()</a>.

**Creating from a List**  
This is highly unusual, but possible.  
```python
# to get a dataframe with 1 column from a list of values
list = [ 2, 4, 6, 8 ]
df = pd.DataFrame(list)
# The above code creates 4 rows, 1 column, using default indexing. Column name is 0.
``` 

## DataFrame Indexing Methods

We will explore four methods that index data within a Pandas DataFrame. The abundance of approaches can be overwhelming and this guide aims to provide clarity. For additional information, refer to the [Pandas DataFrame Documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).  

| API | Index/Position | Comment |
|---|---|---|
| `df[]` | rows by position, columns by name | One argument only |
| `df.loc[]` | by index | `[inclusive : inclusive]` |
| `df.iloc[]` | by position | Columns by position, too |
| `df.take()` | by position | `axis=0` take rows<br>`axis=1` take columns |

Except for `loc` the API are `[inclusive : exclusive]`.

### Argument Types

| Type | Example | Notes |
|---|---|---|
| Number | `df.iloc[3]`<br>`df.loc[3]` | Describes the position, or,<br>index |
| Numerical Slice | `df[0:3]`<br>`df.loc[1:3]` | A slice using numbers (positional)<br>(index) |
| Numerical List | `df.take([0, 3])`<br>`df.loc[[1,3]]` | List of numbers (positional)<br>(index) |
| Mask | `df[[True, False, True]]` | Any iterable of True/False values |
| String | `df['A']` | A column name (or index value) |
| String Slice | `df.loc[:, 'C':'words']` | Represents a range of columns |
| String List | `df[['C','D','words']]` | A list of column names |

### API Details
::::{tab-set}

:::{tab-item} df
* `df[]` takes a single argument only.  
* Slices are `[ Inclusive : Exclusive ]`.   
* The most common usage is to get a `Series` (column) from the `DataFrame` via `df['col_name']`.  
* One can add a column to a `DataFrame` with `df['new_column'] = list_of_values`  

It is important to note here that when a numerical slice is used, the values represent positions, not the index. When string values are used, the values represent column names.   

**Valid Argument Types:**  
* **Numerical Slice:** represents the Row **Positions**  
* **Mask:** represents which Rows to keep  
* **String:** column name  
* **String List:** list of column names  

**Invalid Argument Types:**  
* **Numerical List:** You cannot use `df[[0, 5, 8]]` to access a list of rows.  
* **String Slice:** You cannot use `df['first':'exclude_me']` to access a slice of columns. Instead, you must use a list of strings.  

**Examples:**  

| Valid | Results | Invalid | Note |
|---|---|---|---|
| `df[0:1]` | DataFrame<br>All columns, 1 row | `df[0]` | single number **NOT** allowed |
| `df[1:3]` | DataFrame<br>All columns, 2 rows | `df[[0, 3]]` | List must be column names |
| `df[2:10]` | DataFrame<br>All columns. Many rows |  | All rows at those positions. If the slice is completely out of bounds, an empty DataFrame is returned. |
| `df[[True, False]]` | DataFrame<br>All columns, rows where mask==True |  | Length of mask must be len(df) |
| `df[['C', 'D']]` | DataFrame<br>All rows with columns 'C' and 'D' |  | The columns are ordered as they appear in the list. |
| `df[['C']]` | DataFrame<br>All rows, one column 'C' |  | A list of just 1 still results in a DataFrame. |
| `df['C']` | Series. Column 'C' | `df['C':'words']` | Column slices **NOT** allowed. |

Note that, except for the last example, all valid API return a DataFrame.  
:::

:::{tab-item} df.loc
* `df.loc[rows, cols]` takes one or two arguments.  
* To get all rows, use an 'empty' slice: `df.loc[ : , 'Name']`  
* Each argument can describe multiple values or a single value.   
* The type returned depends on the argument types (vectors vs scalar <a href="#footnotes">[1][2]</a>).  
    * If both arguments are vectors, a `DataFrame` is returned.   
    * If exactly one argument is a vector, then a `Series` is returned.   
    * If both arguments are scalar, then the contents of the single cell is returned.    
* Slices are `[ Inclusive : Inclusive ]`.  
* One can set a value. `df.loc[1, 'Name'] = 5` will set the `DataFrame`'s value to 5 at index 1 and row 'Name'.  

The first argument describes the indices of the rows desired.   
The second argument describes the column names desired.  

**Valid Argument Types:**  
* **Slice**: For rows, the slice must match the index type. For columns, the slice indicates the names of the columns to include and every column between.   
* **Mask**: Represents which rows/cols to keep. Mask is an iterable of True/False values (such as a `Series` or a list)  
* **List**: A list of indices or column names to include.   

Examples: 

| Valid | Note |
|---|---|
| `df.loc[0:3]` | Rows with indices 0 & 3, and everything in between |
| `df.loc[11:5]` | Since indices don't need to be sorted, this will have index 11 as the first row and index 5 as the last row, and all rows that are positioned between them. |
| `df.loc[mask1, mask2]` | Gets all the rows where mask1 is True, and all the columns where mask2 is True. len(mask1) == count of rows. len(mask2) == count of columns. |
| `df.loc[ : , df.columns != 'Bad']` | Gets all the rows and all the columns except for 'Bad'. df.columns is a list of column names. The result of comparing the list to 'Bad' is a list of True/False values... a mask |
| `df.loc[ [0, 8, 11], ['One', 'Three'] ]` | Each list represents which row/column to keep. The result has the same order as that provided in the list. |

```{admonition} Why Inclusive?
:class: note 
The reason this API is inclusive is because one will often want to get a set of columns that one knows about. It is better to say:  
> "I want all the columns starting with 'One' and ending with 'Last'"   

than it is to say:
> "I want all the columns starting with 'One' and goes until the column after the 'Last' column that I want named... gosh, what is the name of the column that I don't want?  

The same can be true for rows when the index is not sorted.  
```
:::

:::{tab-item} df.iloc
* `df.iloc[rows, cols]` takes 1 or 2 arguments.  
* Arguments are primarily **integers** that represent **position**, but can also be a boolean mask.  
* Arguments can also be a lambda for with the argument of the lambda is the calling object, either a DataFrame or Series.  
* There are no string arguments.  

**Valid Argument Types:**  
* **integer** that represents the position of the row or column.  
* **Numerical Slice** that represents the positions of the rows or columns.  
* **Numerical List** that represents the positions of the rows or columns.   
:::

:::{tab-item} df.take
`df.take()` is primarily a **positional** based indexer/slicer. It will return the **columns** or **rows** in the position specified by the inputs, which will either be a **single value**, **list**, or **slice**. It has another parameter, `axis`, which is set to _0 by default_. The default parameter refers to the **index/rows**, meaning we are selecting rows to extract. If you set `axis` to 1, then it will select **columns**.

Since `df.take()` is **positional** based, you **cannot** input labels. They must be integers. Additionally, it _ignores whatever custom index you may have applied_, even if it is an integer index. It will use the _underlying positional index_ to collect the data. Remember, you **need** to include the square brackets, because the function takes only lists.

```python
'''
Series based on a row
'''
s1 = df.take([1]) # returns a series representing row 1

'''
Series based on a column
'''
s2 = df.take([1], axis=1) # returns a series representing column 1

'''
DataFrame based on rows
'''
d1 = df.take([1, 3, 0]) # returns a dataframe containing rows 1, 3, and 0

# Setting `axis` to 1 indicates whether the list of indexes is for **rows** or **columns**
d2 = df.take([1, 3, 0], axis=1) # returns a dataframe containing columns 1, 3, and 0
```

**Exceptions and Oddities**
* Make sure to look out for `IndexError` exceptions, which will arise if you _input a number that is not in the index_. This means you **can't** use `len(df)` as a parameter in order to get the _last row of the dataframe_.
* You can use **negative indices**. This works similarly to slicing in lists in base python, where _the -1 index corresponds to the last value of the set_.
* `df.take([0])` returns the first (0 position) row.
:::
::::

### Examples

::::{tab-set}
:::{tab-item} Common
df = ![Default Index](../static/df_slice_1.png)  

| Result | API |
|--------|-----|
| ![Default Index](../static/df_slice_1a.png) | `df[0:1]`<br>`df.loc[0:0]`<br>`df.iloc[0:1]`<br>`df.take([0])` |
| ![Default Index](../static/df_slice_1b.png) | `df[1:3]`<br>`df.loc[1:2]`<br>`df.iloc[1:3]`<br>`df.take([1,2])` |
| ![Default Index](../static/df_slice_1c.png) | `mask=[True,False,True,False]`<br>`df[mask]`<br>`df.loc[mask]`<br>`df.loc[[0, 2]]`<br>`df.iloc[mask]`<br>`df.iloc[[0, 2]]`<br>`df.take([0, 2])`<br>`df[[0, 2]]` <span style="background-color: yellow">FAILS!!</span> |
| ![Default Index](../static/df_slice_1d.png) | `mask=[False,False,True,True,True,False]`<br>`df[['C', 'D', 'words']]`<br>`df.loc[:, mask]`<br>`df.loc[:, 'C':'words']`<br>`df.loc[:, ['C', 'D', 'words']]`<br>`df.iloc[:, mask]`<br>`df.iloc[:, [0, 2]]`<br>`df.take([2, 3, 4], axis=1)`<br>`df['C':'words']` <span style="background-color: yellow">FAILS!!</span> |
| ![Default Index](../static/df_slice_1e.png) | `df.loc[:, mask]`<br>`df.loc[:, 'A':'A']`<br>`df.loc[:, ['A']]`<br>`df.iloc[:, 0:1]`<br>`df.iloc[:, mask]`<br>`df.iloc[:, [0]]`<br>`df.take([0], axis=1)`<br>`df.loc[:, 'A']` <span style="background-color: yellow">WRONG!! Returns Series</span> |
| Series: Column 'A'<br><pre>0    1<br>1    2<br>2    3<br>3    4<br>Name: A, dtype: int64</pre> | `df['A']`<br>`df.loc[:, 'A']`<br>`df.loc[:, mask]`<br>`df.iloc[:, 0]`<br>`df.iloc[:, mask]` |
| Series: 2nd Row with index 1<br><pre>A          2<br>B          6<br>C         10<br>D         14<br>words    cat<br>jumpy      2<br>Name: 1, dtype: object0</pre> | `df.loc[1, :]`<br>`df.iloc[1, :]` |
| Scalar Value:<br>`7` | `df.loc[2, 'B']`<br>`df.iloc[2, 1]` |
:::

:::{tab-item} Unsorted Index
|DataFrame|Result|API|
|---------|------|---|
|![Default Index](../static/df_slice_2.png)|![Default Index](../static/df_slice_2a.png)|`df[0:1]`<br>`df.loc[9:9]`<br>`df.iloc[0:1]`<br>`df.take([0])`|  
|  |![Default Index](../static/df_slice_2b.png)|`df[1:3]`<br>`df.loc[2:11]`<br>`df.iloc[1:3]`<br>`df.take([1,2])`|
:::

:::{tab-item} String Index
|DataFrame|Result|API|
|---------|------|---|
|![Default Index](../static/df_slice_3.png)|![Default Index](../static/df_slice_3a.png)|`df[0:1]`<br>`df.loc['ax']`<br>`df.iloc[0:1]`<br>`df.take([0])`|  
|  |![Default Index](../static/df_slice_3b.png)|`df[1:3]`<br>`df.loc['cat':'dog']`<br>`df.iloc[1:3]`<br>`df.take([1,2])`|
:::
::::

#### Footnotes
[1] **Vector** is intended to a data structure that can hold multiple values such as a list, slice, or array, even when these structures contain a single value.    
[2] **Scalar** is intended to mean a single value such as a string or integer. It is NOT a list, slice, or array.

## Iterating a DataFrame

There are several ways to iterate through a DataFrame.

```python
# iterates through the columns
for n in df2:
    print(n)

# iterates through the tuples (col_name, col_series)
for col_name, col_series in df2.iteritems():
    print(col_name)
    print(col_series)

# identical to the above
for col_name, col_series in df2.items():
    print(col_name)
    print(col_series)
```

## Accessing/Changing Attributes & Values

You can access and modify DataFrame attributes and values in several ways:

### Renaming Columns

Rename columns using the `rename()` method with a dictionary mapping old names to new names:

```python
df = df.rename(columns={'old_name': 'new_name', 'A': 'Alpha'})
```

Rename all columns at once by assigning to `df.columns`:

```python
df.columns = ['col1', 'col2', 'col3']
```

### Index and Reindexing

Get the index (row labels) or columns:

```python
df.index      # returns the index (row labels)
df.columns    # returns the column labels
```

Set a column as the index:

```python
df = df.set_index('column_name')
```

Reset the index to default integer values:

```python
df = df.reset_index(drop=True)
```

Reindex to change the order or add new indices:

```python
df = df.reindex([2, 0, 1])  # reorder rows by index
```

### Accessing Values

Access a single value by label or position:

```python
value = df.at[3, 'col1']      # by label
value = df.iat[0, 1]          # by position
```

Set a value:

```python
df.at[3, 'col1'] = 42
df.iat[0, 1] = 99
```

### Changing Data Types

Convert a column to a different type:

```python
df['col1'] = df['col1'].astype(float)
```

Convert all columns to numeric (invalid parsing will be set as NaN):

```python
df = df.apply(pd.to_numeric, errors='coerce')
```

### Adding/Removing Columns

Add a new column:

```python
df['new_col'] = [1, 2, 3, 4]
```

Remove a column:

```python
df = df.drop(columns=['col_to_remove'])
```

### Adding/Removing Rows

Add a new row (returns a new DataFrame):

```python
df = pd.concat([df, pd.DataFrame([{'col1': 5, 'col2': 6}])], ignore_index=True)
```

Remove a row by index:

```python
df = df.drop(index=2)
```

### Summary Table

| Operation                | Example                                      |
|--------------------------|----------------------------------------------|
| Rename columns           | `df.rename(columns={'A': 'Alpha'})`          |
| Set column as index      | `df.set_index('col')`                        |
| Reset index              | `df.reset_index(drop=True)`                  |
| Access value (label)     | `df.at[3, 'col1']`                           |
| Access value (position)  | `df.iat[0, 1]`                               |
| Change dtype             | `df['col1'].astype(float)`                   |
| Add column               | `df['new'] = ...`                            |
| Remove column            | `df.drop(columns=['col'])`                   |
| Add row                  | `pd.concat([...], ignore_index=True)`        |
| Remove row               | `df.drop(index=2)`                           |

## Handy Solutions to Common problems
* `pd.read_csv` [documenation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html?highlight=read_csv#pandas.read_csv)
> Example: `pd.read_csv(name, thousands=',', na_values='---', usecols=['c1', 'c2'], dtype={'c1':np.float64, 'c2':np.int32}, skiprows=3)`  
* setting NaN (`na_values='---'`), or the comma separator (via `thousands=','` for currency  
* changing all columns to be numeric: `df = df.apply(pd.to_numeric, errors='coerce')`  
* one can reduce time & memory of reading a file using the argument `usecols=['col1_name', 'col4_name']'`    
* `dtype` argument can set the types of each columns  
* `skiprows=5` can be used to skip the first 5 lines of a CSV file if there are some header lines to be ignored  

* df.sort_index()
* df.sample(n=30)
* df.reset_index(inplace=True)
* df.melt(value_name='value', var_name='source', ignore_index=False)
