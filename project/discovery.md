# Discovery

## Overview

The point of this Deliverable is to assure that you understand your goals, your data, and that your data is sufficient.  

There are several things you must provide:  
* Downloaded & Accessible Data  
* Research Questions & Motivation  
* Data Description  
* Challenge Description  

## Goals

* The main goal of the discovery document is to create the "context and scope" of what you are answering. What is your "research topic" in 3 bullet questions.
* Submit to github a link to your google document or your markdown content in the document folder.
* Submit to GitHub your folder of raw_data (or links to a Google Folder if over 1GB).  
* Target Challenge Goals
* As a guide your document should be between 1500 and 2500 words at most excluding your datasets. (3-5 pages). You will be marked down for going over this.

You do not need to have any code written yet, but you may want to use some code to help you learn about the data. For example, you may want to print out the columns or get some statistical information about the data using code.  

You can use Excel or other tools to view the data.  

Things NOT necessary for this deliverable:  

* web scraping  
* data clean up  
* unit testing  
* plots  
* report  
* presentation  

## Document Purpose 

It is a frequent student behavior to dive into a research project without fully understanding what data is available and challenges ahead. This deliverable is to assure that the student has the necessary data and has the understanding of the pending challenges.  

The Discovery Document's purpose is to:  

1. Illustrate that you have found **appropriate data**. The data must be:
 * Large enough (500 lines or more)  
 * Available for download (CSV file format)   
 * Has the necessary information to successfully conduct your research  
2. Present a few **questions** (about the data)  
 * This is the focal point of your research  
 * Express why your questions are of interest (motivation)  
3. Illustrate that you **understand the data**:  
 * Know how the data was sourced
 * Know how the data may be limited (reliability, accuracy, completeness, messy)  
 * Identify & explain relevant columns: names, format, units, ranges, cleanliness  
 * Issues or challenges in working with the data (e.g. too big, non-standard key formatting making cross-referencing difficult, missing information, too broad or narrow)  
4. Establish **Challenge Goals**:  
 * While this may change, it is important to consider what challenges you intend to take on. 

## Research Questions

A common mistake in a research project is to not have a research goal in mind. Students can seek out data and then aimlessly proceed to execute an exploratory process without direction. While exploration is certainly part of Data Science, you should have some specific questions in mind that you intend to answer. Your questions should revolve around identifying correlations and not causations. Don't worry if you don't expose an obvious correlation; your plots are successful if they identify non-correlations. 

Another common mistake is to take on a project that is only mildly interesting and without consequence or impact. For example, one might identify the most popular genre of movies without an explanation of why we should care. Perhaps there is a very good reason we should care. Don’t simply answer mild curiosities.  

### Keep Questions Updated

In conducting research, the formulation of a research question is a crucial step that evolves over time. As researchers delve deeper into the subject matter, gain new insights, and adapt to changing circumstances, the initial research question may undergo modifications or even a complete transformation. Changes can occur due to many reasons such as:
1. Pilot Study or Data Collection
2. Data Analysis and Initial Findings
3. Feedback and Peer Review

### Demographics

Having multiple research questions that focus on different areas or demographics within a project can enhance the depth and breadth of your study. Here's a description of how to accomplish this and a specific example to illustrate the concept:

To create multiple research questions focusing on different areas or demographics, you should first identify the key dimensions they wish to explore within the broader research topic. These dimensions could be distinct variables, subgroups, or specific factors of interest. Each research question should be clear, relevant, and aligned with the unique characteristics of the subgroup or area under investigation.

### Examples

1. How does the number and rate of aviation accidents correlate with different aspects of the temporal dimension (technological progression)?
2. What is the relationship between aircraft mechanical factors and the likelihood of aviation accidents?
3. How do external environmental factors such as geographical patterns and weather conditions correlate with the occurrence of aviation accidents?
4. What is the role of human factors, including communication, crew-related factors, and staffing levels, in aviation accidents and incidents?
5. To what extent can machine learning extract factorial information from personal narratives of aviation accidents? 

#### Comments

In this example, the researchers have formulated five distinct research questions, each focusing on a different area and demographic. By having multiple research questions, the researchers can collect data specifically tailored to each potential hazard in aerospace engineering as well as factors of ML.

The first two focus on aircraft accidents and their connection to technology. The third question covers environmental and geographical demographics. The fourth is centered towards human behavior and psychology. And lastly, the fifth questions aims to draw connections using a Machine Learning model. 

The different perspectives covered in this research, enviornmental, technology, physiological, and more make it complex and incredibly insightful. It also sets up the stage for conversation between findings. 

### More Examples (Good & Bad)

**Good Research Questions** (Clear, Specific, and Data-Driven)

1. **How does air quality vary across different cities, and what factors contribute most to poor air quality?**  
   *(This question allows for data collection on air quality, weather, and pollution sources, making it suitable for Pandas analysis.)*  

2. **What are the trends in student performance based on study time and extracurricular activities?**  
   *(You can analyze datasets on student grades, study habits, and activity participation to find correlations.)*  

3. **How do different machine learning algorithms perform on predicting house prices based on real estate data?**  
   *(This allows for a comparative analysis using regression models and Pandas for data handling.)*  

**Poor Research Questions** (Too Broad, Opinion-Based, or Lacking Data)

1. **Why do students struggle with math?**  
   *(Too vague and qualitative; lacks a clear dataset or measurable variables.)*  

2. **Is social media good or bad for mental health?**  
   *(Overly broad and subjective; needs a more specific data-driven approach like analyzing sentiment analysis of social media usage.)*  

3. **How has technology changed over time?**  
   *(Too general; should focus on a specific technology and measurable aspects like adoption rates or performance metrics.)*  

## Data Description

:::{note}
The ultimate focus of this deliverable is to **understand** your data. 
:::

You will extensively document your data to illustrate that you understand it. Here are some things that you should document:  

* **Data Collection**: Explain when and how the data was collected. Explain what biases might be present in the data.  
* **Data Source**: Provide the URL where the data was collected so that it can be replicated to download the data to verify testing this. Sometimes a site will have various fields to fill out before the data can be downloaded. These steps will not alter the URL seen in the address bar which can be confusing and add difficulty to the process of downloading the data again. Be sure you provide instructions on how to download your data.  

* **Column Descriptions**: Identify the important columns you will work with. You may have only one or two important columns. Or, perhaps you’ll have 20! Find a way to present your information in an easy to read format, such as a table. Here are things you should describe for every important column:  
    * **Name**: Provide column name as found in the file.  
    * **Description**: Give a sentence explaining what the data is. Most datasets have columns that are cryptic and hard to understand. Do not plot data that you do not understand! For example, the data might give a number representing the count of gun incidents at schools which include students inappropriately speaking about guns, pointing their fingers like a pistol, or someone complaining that they saw a police officer with a gun. Know the specific definition of your data!  
    * **Units**: Explain the units such as: dollars per year, square foot, free form human input as a string, list of words, date/time, year. State whether the data is categorical (e.g. Grade level).  
    * **Examples**: Sometimes it can be valuable to provide some examples, especially when it comes to categorical and non-numerical values. This will help you discover what type of normalization and organization is required.  
    * **Foreign Key**: If you intend to do a join with another dataset, you should list out the columns you will use to join on. It is common to have a column that is structured slightly differently from another dataset. For example, in one dataset you may have just the two letter representation of a state (e.g. WA) while in another you have the name (e.g. Washington) while in another you have odd abbreviations (e.g. Wash St). You may need to do work to normalize these columns to enable a seamless join.  
    * **Issues**: Common issues are:  
        * **Free form** human input is riddled with typos, non-conformity, difficult to summarize, and difficult to normalize. If you can’t consume the data in a way that enables you to graph it, then the data is useless.  
        * **Missing data** can be common. If the available data is scant, this can greatly skew your results and make plot creation difficult.  
        * **Errors** in the data can be rampant. Perhaps there are only a few critical errors to be aware of. For example, a column might represent inches of rain per day, but in some cases unbelievable values were used (e.g. 203.4). Discuss what validation you might execute or ways you’ll catch outliers.  
        * **Non-conformity** can destroy your ability to join tables. 

:::{seealso}
See more info on web scraping [here](../project/scraping.md)
:::

## Grading

Grading for this document will follow this rubric guide: [TBD](../tbd.md)
