### **Premise:**
My company would like a system that recommends content to users (movies, shows, music, etc). It should learn the user's tastes based on the user's ratings of the content (likes and dislikes). The expected UX should be this:
- User signs up for the app/website. They enter personal information such as name, age, location, nationality, etc. They also answer some questions about their content interests.
- The system recommends a piece of content to the user. The user views and rates the content. 
- The system learns from the user's rating of the content to improve its next recommendation.
I would like a proof-of-concept showing that such a system is possible. 

### **Objective**:
In this assignment, students will build a machine learning system focusing on integrating pre-trained models and an online dataset. The assignment emphasizes understanding the key terminology (data, model, component, system, pipeline, feedback) and applying **systems thinking** by considering interactions with users and the environment. Students will not create machine learning models from scratch but will work with a pre-trained model and dataset from an online source (e.g., Kaggle, HuggingFace).

The system should:
1. Download and preprocess data from an online source (e.g., Kaggle, HuggingFace).
2. Use a pre-trained machine learning model for inference.
3. Implement feedback loops to simulate user interactions and adjust the system’s predictions.
4. Organize the system into logical components (data ingestion, preprocessing, model integration, feedback).
5. Present the final system as a working Python program.

### **Assignment Requirements**:

1. **Data Source**: 
   - Choose a dataset from an online platform (e.g., Kaggle or HuggingFace dataset). Download and load the dataset into your system.
   - Preprocess the data to make it compatible with the model (e.g., clean the text, normalize numerical data).

2. **Pre-Trained Model**: 
   - Use a pre-trained machine learning model from an online source (e.g., [HuggingFace Models](https://huggingface.co/models) or a model hosted on Kaggle).
   - The model should be capable of performing inference (e.g., classification or regression) based on the dataset you’ve chosen.

3. **Pipeline Construction**:
   - Build a **data pipeline** that ingests, preprocesses, and passes the data to the pre-trained model for inference.
   - Implement the pipeline as a series of components (data ingestion, preprocessing, model inference, feedback) that interact with one another.

4. **Feedback Loops**:
   - Design and implement feedback loops where simulated user interaction modifies the predictions or outcomes of the model (e.g., a user provides feedback about the accuracy of predictions, leading to adjustments).
   - Incorporate this feedback to simulate iterative improvement of the model's accuracy or its interaction with user needs.

5. **System Thinking**:
   - Consider and document how your system interacts with different elements (data, model, users, environment). Use **systems thinking** to explain how feedback affects the system, how components interact, and how the system adapts to changes.

6. **Deliverables**:
   - A Python program implementing the system, with clear modularity (components, model, pipeline).
   - A short report (2-3 pages) explaining the design choices, system architecture, and feedback mechanism, emphasizing the interaction between components. 
       - Give system and feature goals, user goals, and model goals, as you understand them from the premise. Please explain how your system meets these goals.
       - Clear documentation for the pipeline and how each component connects. This includes an explanation for the choice of model and data. Please give 3 possible models and 3 possible datasets, then explain why you chose the model and dataset you used. 
