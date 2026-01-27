# Challenges

Challenge goals help us to define expectations while still offering flexibility for you to design your own project. Meeting the requirements of a challenge goal is described here.

## Challenge Description

Read the list of possible challenge tasks below and make sure you understand what it takes to meet the requirements of a Challenge Goal. Then, set aside ample time to completely fulfill the goal.  

Many students underestimate the amount of work to meet a Challenge. A typical mistake is to assume that they can meet the demands of "Multiple Datasets" because they have a few datasets downloaded. In reality, to qualify you must work with **four** or more datasets what require **merging** together in various ways. The datasets need to have a valid reason for merging; the merging must add value to the research.   

Others think that learning a new library will be quick and easy. They end up either not doing it at all or slapping on a piece of code that took 5-minutes to look up on the internet. The size of a student's accomplishments will impact a student's grade. Note that the amount of time spent is not graded, but it is very difficult to have a large accomplishment in a small amount of time.    

## Valuable Unit Testing

To qualify, you must deliver valuable Unit Tests of the methods that clean and organize your data. You need to provide some fake data and run the tests that validate the results. You should use Python's Unit Test framework. Look at past warmup or projects where there was a `run_tests.py` file and tests folder. Copy that infrastructure.

## Multiple Datasets

To qualify, you must work with **four** or more datasets what require **merging** together in various ways. The merging must be necessary to come up with a richer analysis. This requirement is not just about using more than one dataset across your research questions, but is more about combining (via **merge**) the datasets to make a more in-depth analysis.  

## Web Scraping or API Usage

To qualify, you must successfully scrape hundreds of rows of data off one or more web page. Or, you must use some public API to collect data from some data service (e.g. Spotify). The resulting data would be saved as a CSV file for later organization and analysis. To Web Scrape, consider using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

See more info on web scraping [here](../project/scraping.md)

## Statistical Validation

To qualify, you must do some extra work on top of your results to verify the validity of the results. For example, using some test of statistical significance to verify your results aren’t likely to happen by chance. The statistical analysis needs to be visible in the plots themselves and briefly discussed in your write-ups. You cannot simply use `seaborn` to plot a regression and consider this challenge fulfilled.

## Machine Learning

Many students have attempted this with great failure. This challenge goal requires going above and beyond the fundamental steps of a Machine Learning pipeline we introduced in class. You cannot simply create a model, present some accuracy number and call it quits. To qualify you need to:

* Explore and use a new Machine Learning model: You cannot use the simple `DecisionTree`. Work to adjust the hyperparameters during training to improve the model's accuracy. You must then **PRESENT** your exploration during the Final Presentation.  
* Explore the predictions made by the model to either:   
   * provide insight into how the model makes its predictions. You can look at [Machine Learning -> Regression-Distance Study (TBD)](../tbd.md). Look at how the Model Graphs provide clear insight into how the model makes predictions.
   * make some predictions about the future or situation not present in the data.  
* Dive deep into applying machine learning to your dataset to gain insights about the data or use it to make predictions about the future. Be explicit with what your goal is and how you will assess if you meet that goal. One example could be looking at various model types (and different settings of their hyperparameters) to identify which model is “best” (by how you define best). Another could be looking at how to use an “interpretable model” to understand which features are the most informative for how a decision is made. This challenge goal requires going above and beyond the fundamental steps of a Machine Learning pipeline we introduced in class. To achieve this challenge goal, you need to demonstrate exploration of more ideas in machine learning. 

## New Library
Learn a new Python library and use it in your project in a significant way to help with your analysis. Part of this class is being able to learn libraries in Python. Show that you are able to take what you’ve learned in the context of learning a library we have not discussed in-depth in this course. Here are some recommended libraries.
* Download from Web: [requests](https://pypi.org/project/requests/)
* Scientific Computing: [SciPy](https://www.scipy.org/)
* Folium for interactive geo plots:[Folium](https://python-visualization.github.io/folium/latest/getting_started.html)
* Natural Language Processing: [spaCy](https://spacy.io/)
* Advanced/Interactive Visualizations: [altair](https://altair-viz.github.io/) or [plotly](https://plot.ly/python/).  
  * Note that interactive plots work best for data that has lots of different filtering options. For example: filter by year, by age, by gender, by position. 
  * > Note that you need to **make a video** of the interaction with your plots.  
