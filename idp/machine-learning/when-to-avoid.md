---
title: When to Avoid Using Machine Learning
---

# When to Avoid Using Machine Learning

**Feedback loops** in machine learning can be powerful tools for improving model performance and adaptability. However, they also carry inherent risks and potential dangers that need to be carefully managed. When not properly controlled, feedback loops can lead to unintended consequences and detrimental outcomes. Here are some of the dangers associated with feedback loops in ML:

### Bias Amplification
Feedback loops can amplify biases present in training data. If a model makes biased predictions due to biased training data, positive feedback can reinforce these biases. For example, if a hiring algorithm is biased against certain demographics, the algorithm's biased recommendations might be acted upon, which can lead to discrimination.

### Overfitting
Positive feedback loops can lead to overfitting, where a model becomes overly specialized to the training data and performs poorly on new, unseen data. As the model makes predictions and receives reinforcement for correct outputs, it may start memorizing the training examples rather than learning generalizable patterns.

![Overfitting](../static/avoid_ml_overfitting.png)

### Algorithmic Polarization:
Feedback loops can unintentionally drive algorithms to amplify existing opinions and create echo chambers. For example, in recommendation systems, if a user's preferences are reinforced by positive feedback, they might only receive content that aligns with their current views, leading to a skewed perspective.

### Ethical and Social Implications:
Feedback loops can perpetuate discriminatory or unethical practices. For instance, if a model is exposed to biased data and the feedback reinforces biased predictions, it can contribute to systemic inequalities.

### Privacy and Security Concerns:
When dealing with sensitive data or applications that require a high level of security, using ML could introduce vulnerabilities. ML models can leak information through various mechanisms, so careful consideration is necessary when privacy is a concern.


While feedback loops offer great potential for enhancing machine learning systems, the dangers associated with them necessitate cautious and responsible development, monitoring, and management. By addressing these risks, the benefits of feedback loops can be harnessed while minimizing unintended consequences.
