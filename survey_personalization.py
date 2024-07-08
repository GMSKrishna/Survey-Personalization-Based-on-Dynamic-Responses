import json

# Function to load survey data from a JSON file
def load_survey(file_path):
    with open(file_path, 'r') as file:
        survey = json.load(file)
    return survey

# Function to get the next question based on the current response
def get_next_question(current_response, survey_data, question_id):
    next_question_id = survey_data[question_id]['responses'].get(current_response)
    if next_question_id:
        return next_question_id, survey_data[next_question_id]['question']
    return None, None

# Function to simulate the survey flow
def survey_flow(survey_data):
    current_question_id = "1"
    while current_question_id:
        question = survey_data[current_question_id]['question']
        print(f"Q: {question}")
        response = input("Your Response: ")
        current_question_id, next_question = get_next_question(response, survey_data, current_question_id)
        if next_question is None:
            print("Thank you for completing the survey!")
            break

# Load the survey data
survey_data = load_survey('survey_data.json')

# Simulate the survey flow
survey_flow(survey_data)
