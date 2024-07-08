# Survey-Personalization-Based-on-Dynamic-Responses

## Objective
Customize surveys in real-time based on user responses to enhance engagement and data quality.

## How to Use
1. Ensure you have Python installed.
2. Install required libraries:
    ```sh
    pip install pandas
    pip install json
    ```
3. Run the survey personalization script:
    ```sh
    python survey_personalization.py
    ```

## Survey Data Structure
The survey data is structured in a JSON format where each question points to the next question based on user responses.

## Script Explanation
- `load_survey(file_path)`: Loads the survey data from a JSON file.
- `get_next_question(current_response, survey_data)`: Retrieves the next question based on the current response.
- `survey_flow(survey_data)`: Simulates the survey flow based on user responses.
