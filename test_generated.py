# import google.generativeai as genai
# import datetime
# import os

# # Configure Gemini API
# genai.configure(api_key="AIzaSyAVfg0QElVVa0TqxXZqW6rbwMu5UTcRryY")
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Hardcoded test description
# test_description = (
#     # "Write a Python pytest function to test the /api/payments endpoint of a payment API. "
#     # "Send a POST request with amount=100, currency='USD', card_number='4111111111111111'. "
#     # "Assert that the response status code is 201 and the JSON contains status='success'."
#     # "Verify that a user can log in successfully with a valid username and password. The API should respond with status code 200 and a JSON field 'token' containing a JWT."
#     "Ensure that when the password field is omitted in a login request, the response is a 400 Bad Request with an error message 'Password is required'."
# )

# # Send the description to Gemini and get test code
# prompt = (
#     "You are a Python test automation engineer. "
#     "Generate a single Pytest test function (using requests library) for the following test case description. "
#     "Assume BASE_URL is defined as the API base URL. "
#     "Only return code, do not explain.\n\n"
#     f"Test case: {test_description}\n"
# )
# response = model.generate_content(prompt)
# test_code = response.text.strip()

# # Timestamped file name
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# filename = f"test_generated_{timestamp}.py"

# # Output directory
# output_directory = "generated_tests"
# os.makedirs(output_directory, exist_ok=True)
# output_path = os.path.join(output_directory, filename)

# # Prepend imports & BASE_URL to test file
# with open(output_path, "w", encoding="utf-8") as out_file:
#     out_file.write("import requests\nBASE_URL = 'http://localhost:8080'\n\n")
#     out_file.write(test_code + "\n")

# print(f"Test code generated and saved to: {output_path}")





import google.generativeai as genai
import datetime
import os

# Configure Gemini API
genai.configure(api_key="")
model = genai.GenerativeModel("gemini-1.5-flash")

# Path to the source code file you want to generate tests for
source_code_file = "source_code.py"  # Change this to your source file path

# Read the source code
try:
    with open(source_code_file, "r", encoding="utf-8") as file:
        source_code = file.read()
except FileNotFoundError:
    print(f"Error: Source code file '{source_code_file}' not found.")
    exit(1)

# Send the source code to Gemini and get test code
prompt = (
    "You are a Python test automation engineer. "
    "Analyze the following Python code and generate comprehensive Pytest test functions for it. "
    "Create test cases that cover different scenarios including edge cases, valid inputs, invalid inputs, and error conditions. "
    "Use the pytest framework and include appropriate assertions. "
    "If the code contains functions, test each function separately. "
    "If the code contains classes, test the class methods and initialization. "
    "Only return the test code, do not explain.\n\n"
    f"Source code to test:\n{source_code}\n"
)

response = model.generate_content(prompt)
test_code = response.text.strip()

# Remove code block markers if present
if test_code.startswith("```python"):
    test_code = test_code[9:]
if test_code.endswith("```"):
    test_code = test_code[:-3]

# Timestamped file name
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# filename = f"test_generated_{timestamp}.py"

source_filename_without_ext = os.path.splitext(os.path.basename(source_code_file))[0]
filename = f"{source_filename_without_ext}_test.py"

# Output directory
output_directory = "generated_tests"
os.makedirs(output_directory, exist_ok=True)
output_path = os.path.join(output_directory, filename)

# Prepend imports to test file
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write("import pytest\n")
    out_file.write("import sys\n")
    out_file.write("import os\n")
    out_file.write(f"sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))\n")
    out_file.write(f"from {os.path.splitext(os.path.basename(source_code_file))[0]} import *\n\n")
    out_file.write(test_code + "\n")

print(f"Test code generated and saved to: {output_path}")
print(f"Generated tests for source file: {source_code_file}")
