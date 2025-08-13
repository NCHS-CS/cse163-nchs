# Intermediate Data Programming

```{card} ![Headshot of Kevin Lin](https://kevinl.info/assets/images/kevin-lin.webp)
:header: **Kevin Lin**
:footer: **Office Hour**: Wed 4:30–6:20 PM
:url: mailto:kevinl@cs.uw.edu

If I'm not working on this class, you can probably find me looking around for travel and restaurant deals, experiencing the latest indie movies at SIFF cinemas, introducing guests to our underwater neighbors at the Seattle Aquarium, or designing new methods to empower students through education.
```

The world has become data-driven. Domain scientists and industry increasingly rely on data analysis to drive innovation and discovery; this reliance on data is not only restricted to science or business, but also is crucial to those in government, public policy, and those wanting to be informed citizens. As the size of data continues to grow, everyone will need to use powerful tools to work with that data.

In this course, students will learn:

1. **How to work with different types of data** such as text, tabular data, images, and geospatial data.
1. **Data science tools and libraries** such as [Jupyter Notebook](https://jupyter.org/), [pandas](https://pandas.pydata.org/), [seaborn](https://seaborn.pydata.org/), and [scikit-learn](https://scikit-learn.org/).
1. **Software engineering skills** such as data structures, object composition, and runtime analysis.
1. **Information representation skills** such as visualization principles, data settings, and data ethics.

This course is designed to support students who have completed:

CSE 160: Data Programming
: Know control structures, file I/O, and data structures in Python. Your first weeks will be a review.

CSE 122: Introduction to Computer Programming II
: Know control structures, file I/O, and data structures in Java. Your first weeks will focus on learning these concepts in Python.

## Why should we learn?

The education you receive in this course can help prepare you for programming jobs, but [this isn't the only purpose for computing education](https://computinged.wordpress.com/2021/11/26/computer-science-was-always-supposed-to-be-taught-to-everyone-but-not-about-getting-a-job-a-historical-perspective/). Education is not only about yourself and your personal gain, but also about all of us and our capacity to live together as a community.

The University of Washington acknowledges the Coast Salish peoples of this land, the land which touches the shared waters of all tribes and bands within the Duwamish, Puyallup, Suquamish, Tulalip and Muckleshoot nations. Among the traditions of the Coast Salish peoples is a value for the connectedness between all living things and a recognition of the [unique ways that each of us comes to know things](https://youtu.be/O6sS1ZI8dDk).

> Modern education has the idea that we all need to know the same thing. At the end of the lesson, everyone will know the same thing. That's why we have tests, that's why we have quizzes, that's why we have homework: to ensure we all know the same thing. And that's powerful---that's important---within a certain context.
>
> But for native culture, the idea that each listener divines or finds their own answer, their own meaning, their own teaching from the story is equally powerful---that each person needs to be able to look at the world and define it for themselves within their culture and then also find a way to live in that world according to the teachings of their people in their culture.

Our course emphasizes the following values.

We are responsible for each others' success
: Everyone has a right to feel like they belong in this course. We'll need to act with compassion and caring to collaborate with each other. Although we will need more than just unexamined commitments to collaboration, listening, empathy, mindfulness, and caring, the following guidelines offer a starting point for ensuring compassion toward each other [@10.37514/PER-B.2022.1824].

  - Listen with intention to understand first and form an opinion only after you fully understand.
  - Take responsibility for the intended and unintended effects of your words and actions on others.
  - Mindfully respond to others' ideas by acknowledging the unique value of each contribution.

: You should expect and demand to be treated by your classmates and teachers with respect. If any incident occurs that challenges this commitment to a supportive, diverse, inclusive, and equitable environment, please let the instructor know so the issue can be addressed. Should you feel uncomfortable bringing up an issue with the instructor directly, meet our advisors during [quick questions](https://www.cs.washington.edu/academics/ugrad/advising#qqs) or contact the [College of Engineering](https://www.engr.washington.edu/bias).

We recognize everyone has unique circumstances
: Do not hesitate to contact the instructor by private discussion post or [appointment](https://kevinl.info/meet/). The sooner we are made aware of your circumstances, the more we can help. Extenuating circumstances include work-school balance, familial responsibilities, religious observations, military duties, unexpected travel, or anything else beyond your control that may negatively impact your performance in the class.
: It is the policy and practice of the University of Washington to create inclusive and accessible learning environments consistent with federal and state law. If you have already established accommodations with [Disability Resources for Students](https://depts.washington.edu/uwdrs/) (DRS), activate your accommodations via myDRS so we can discuss how they will be implemented in this course. If you have a temporary health condition or permanent disability that requires accommodations, contact DRS directly to set up an Access Plan.
: Washington state law requires that UW develop a policy for accommodation of student absences or significant hardship due to reasons of faith or conscience, or for organized religious activities. The UW's policy, including more information about how to request an accommodation, is available at [Religious Accommodations Policy](https://registrar.washington.edu/staffandfaculty/religious-accommodations-policy/). Accommodations must be requested within the first two weeks of this course using the [Religious Accommodations Request form](https://registrar.washington.edu/students/religious-accommodations-request/).

We believe everyone wants to learn
: Education is about shaping your identity as much as it is about learning things. In school, the consequences of making mistakes are relatively small. But the habits you form now---repeated over days, weeks, months, or years---determine who you will be in the future. Now is the best time to practice honest habits.
: We ask that you do not claim to be responsible for work that is not yours. When you receive substantial help from someone else, include a citation. Don't post your solutions publicly. Most importantly, don't deprive yourself or others of the learning opportunities that we've created in this course.
: Academic honesty reflects the trust (or the lack thereof) between students and teachers. We do our best to design the course in ways that ensure trust, but we know our systems are not perfect. If you submit work in violation of these policies but bring it to the attention of the instructor within 72 hours, you may resubmit your own work without further consequence. Rather than blame students, we want to fix or replace broken systems that compel students to lose trust.

## How does learning occur?

In a traditional classroom, you attend class while a teacher lectures until time is up. Then, you go home and do the important work of applying concepts toward practice problems or assignments on your own. Finally, you take an exam to show what you know.

Today, we know that there are more effective ways to learn science, engineering, and mathematics [@10.1073/pnas.1319030111]. Learning skills like software engineering and algorithm analysis requires **deliberate practice**: a learning cycle that starts with sustained motivation, then presents tasks that build on prior knowledge, and concludes with immediate, personalized feedback. Each module in the course will involve several different activities that are designed so that we can make the most of our class time together.

During lecture, participate in the lecture deliberate practice on programming concepts.
: Lecture participation is tracked via completion of PollEverywhere activities.
: After Wednesday lecture, complete the exit ticket in Canvas to prepare for quiz section.

During quiz section, apply what you learned or show what you know in an interview.
: Sections on Thursday will extend the exit ticket and prepare you for code interviews.
: On interview weeks, complete an in-person code interview during section on Thursday.
: If you can't make an interview, make-ups will be in-person during our final exam slot.

Show what you learned by completing the individual homeworks/assessments and a team project.
: In Canvas, submit your completed notebook from JupyterHub and wait for a TA to review it.
: After you receive your TA's review, reply to their questions by writing a submission comment.

**Code interviews** are a key standardized assessment in this course. Rather than treat your submitted program code as the final artifact for evaluation, it is instead a starting point for a conversation that demonstrates your programming fluencies such as code writing, code reading, code debugging, and code communication skills. Communicating your ideas and explaining your decision-making is important in this course. But we know that live discussions during class may not be accessible for everyone and we would be happy to work with you to design accommodations that would allow you to communicate your programming fluencies in an accessible format for you.

Expect to spend 4 hours in class and 8 hours outside of class working on this course. Some weeks may require more or less time than other weeks. If you find the workload is significantly exceeding this expectation, talk to your TA.

{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}

Devices may be used in-class at student discretion but with the community agreement that use should generally be on-task and minimize distractions to others. We agree to common courtesy including closing laptops and significantly turning down brightness when the device is not in direct use. Students who have urgent matters that would take an extended period of time to address during class should step outside the room to use their devices—learning is not likely to happen even if you stayed in class, and the urgency of your work would distract others.

All work is designed to be completed with what has been taught in class. Keep your submitted work within the scope of what has been taught. Work that is found to be out of scope with what we have taught will be penalized. Generative AI or other external resources may be used only for clarifying concepts, supporting debugging, or explaining problems at a high level. If you are consulting generative AI or external resources in permitted ways, include citations for what you used and how you used it. Writeups should all be your own words and ideas; you will not be penalized for grammar or mechanics as long as we understand what you are saying and your arguments are reasonable. Regardless of how much help you receive from others, in order to pass the code interviews, you'll need to be deeply familiar with data programming. Do not deprive yourself or others of learning opportunities in this course.

Encouraged
: Discussing examples shown in class. These examples are part of the course's learning materials.
: Working with a TA to improve your understanding of a task and resolve a particular problem.
: Communicating with other students without sharing code or exact details to reproduce a solution.

Permitted with caution
: Working alongside one or more other people on an assessment.
: Sharing or generating small snippets of code that are not specific to any part of an assessment.

Prohibited
: Obtaining or generating solutions to any part of an assessment in any form for any reason.
: Giving, receiving, or generating a walkthrough to an assessment from anyone or anything else.
: Posting solutions to an assessment in a public place even after the course is over.

## How is this course graded?

Grading in this course is determined by **module completion**, **participation**, **assessment marks**, and **project marks**. Up to 1 quiz section activity will be automatically dropped. No lecture participation will be automatically dropped, but students may miss up to 7 lectures over the quarter and make up for missing participation by completing the lecture absence form, watching the Panopto recording to completion for that day, and answering the quiz questions embedded in the recording. Students who need to miss more than this allotment should let the staff know in the first 2 weeks of the course to discuss alternatives.

The following combinations of work will be guaranteed certain final grades.

1.0 or greater
: Complete the Python and Pandas modules.
: Satisfactory participation through the Pandas module.

2.0 or greater
: Complete the Python, Pandas, and Software Engineering modules.
: Satisfactory participation through the Software Engineering module.

3.0 or greater
: Complete the Python, Pandas, Software Engineering, and Applications modules.
: Satisfactory participation through the Applications module.
: Satisfactory marks across all assessments' rubric criteria.

4.0
: Complete the Python, Pandas, Software Engineering, Applications, and Project modules.
: Satisfactory participation through the Applications module.
: Exemplary marks across all assessments' rubric criteria.
: Highest marks on all parts of the project.

These guarantees are intended to help outline expectations and help external reviewers understand what each final grade range communicates about student achievement. These guarantees do not preclude access to higher grades. Within the constraints of the course, we endeavor to provide a limited number of revision opportunities to help students work toward completion of all five modules.

> **Evaluating Assessment Approaches in Intermediate Data Programming**
>
> You are being asked to participate in a research study to find out more about how assessment approaches affect the student experience in an undergraduate Intermediate Data Programming course. You have been asked to participate in this study because you are a student in a class that is being studied or used as a control. The purpose of this study is to create knowledge that has the potential to improve the educational experience for students at the University of Washington and beyond.
>
> What will you be asked to do?
> : Your data from this class including surveys/evaluations, coursework, and course forum discussions may be analyzed. Your participation involves only agreeing to let us use your data in our analysis. You will not be required to do anything beyond normal educational practice.
> : There may be additional optional opportunities to participate in follow-up interviews or focus group discussions. These are not required, and details will be provided when they arise.
>
> What will happen to the information you provide?
> : Data from participants will be retained only for research purposes and stored using codes that provide a degree of confidentiality. Your instructor will not know whether you are participating in this study until after final grades have been posted.
>
> What can you do if you want more information?
> : Talk to the study team. Kevin Lin is the lead researcher at the University of Washington for this study and can be contacted at <kevinl@cs.uw.edu>.
> : Talk to someone else. If you want to talk with someone who is not part of the study team about the study, your rights as a research subject, or to report problems or complaints about the study, contact the UW Human Subjects Division at <hsdinfo@uw.edu> or 206-543-0098.
>
> What are my options to participate?
> : By default, you will be included in this study. No additional actions are required to participate.
> : Participation in this research, however, is optional. You may withdraw at any time without penalty by contacting Suhas Kannam at <ksuhas16@uw.edu>.
