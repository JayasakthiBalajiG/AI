## Report
1. Pipeline (20/25): missing explanation of component 5.
2. Choice of dataset and model (10/25): missing 3 total models and 3 total datasets. You should give 3 of each, then explain why you chose the ones you used.
3. UX and system loop (13/25): system loop not reflected in code.
4. Data preprocessing (15/25): no explanation of why data was removed.
## Code
Data pre-processing component does not anonymize user information. 
Model looks good based on the statistics, but try training with a validation set and then using a test set to make sure you are not overfitting. 
