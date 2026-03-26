Question : 

Answer:

“In our ESG reporting platform, one challenge we faced was with the final report generation API. Initially, the backend sent all survey responses to the frontend, and the frontend built the PDF report using React. Because the response data was large, this API became very slow and the report generation process was inefficient.

To solve this, we moved the report generation to the backend. I used HTML templates with Jinja in Django to construct the report directly on the server by injecting the final survey responses into the template. Then we converted that HTML into a PDF using wkhtmltopdf and sent it via email to the user and internal team.

This significantly reduced API response time and simplified the report generation workflow.”




##########################################################################################################




Challenge 2 – Questionnaire Scoring Logic (Interview Answer)

You can say this:

“Another challenge in the ESG reporting platform was designing the questionnaire scoring model.
The system had two types of questions — range-based questions and non-range questions.

For range questions, the score depended on numeric ranges like 0–15, 16–50, 51–75, etc., and each range had different marks. The ranges and scores could vary for every question, and sometimes the score could even be negative.

For non-range questions, options could be things like Yes/No/Maybe or Agree/Strongly Agree, and each option also had a different score.

To make this flexible, instead of creating many rigid columns in the database, we stored the scoring configuration in a JSON field in the Question model. This allowed us to dynamically define ranges or option scores per question without changing the schema.

Then during answer submission, the backend evaluated the user response against this configuration and calculated the score accordingly. This design made the questionnaire system much more flexible and scalable for different ESG survey formats.”



    ANSWER_TYPE = [
        ("Yes/No", "Yes/No"),
        ("Yes/No/NA", "Yes/No/NA"),
        ("Range", "Range"),
    ]




##############################################################################################################



Why did you choose JSONField instead of creating separate tables?

Answer:

“Because each question could have a different scoring structure. Some questions had numeric ranges while others had fixed options like Yes/No. Using a JSON field allowed us to store flexible configurations per question without creating multiple relational tables and complex joins. It also made it easier to update scoring rules without changing the database schema.”


#############################################################################################################


Challenge 3 – Handling Dependent Questions (Interview Answer)

You can say something like this:

“Another challenge in the ESG questionnaire system was handling dependent questions. Some questions should only appear based on the answer of another question.

For example, if a question asks ‘Do you track carbon emissions?’ and the user selects Yes, then additional related questions should appear. If the answer is No, those dependent questions should not be shown.

To implement this, we stored the dependency configuration in a JSON field in the Question model, where each question could define which other questions depend on it and under what condition they should be shown.

In the backend API, when fetching questions for a user, we evaluated the user's previous answers and dynamically filtered the question list using Django query conditions. This ensured that only the relevant dependent questions were returned to the frontend.”




###############################################################################################################


“Where is this logic executed?”

Good answer:

“The logic runs in the backend while fetching questions. We check the user's answers and filter the queryset accordingly before sending it to the frontend.”