import openai
from django.conf import settings

prompt = """
As an experienced export accountant, you've specialized in extracting relevant data from messy invoice texts.

Given a messy text, extract the following information in JSON format:

- vendor_name
- gstin
- state_code
- state_name
- invoice_date (in YYYY-MM-DD format)
- invoice_no
- po_no
- tax_percent
- taxable_amount
- total_amount
- file_path
- result

The messy text will be provided within double curly brackets: {{{}}}

Ensure the the date you extract is in YYYY-MM-DD format and its a valid date otherwise the DB will throw error while inserting. This is very important. if the date is not in right format or not extractable them make it null or None. but dont extract invalid date. till will lead to a big error
Ensure the extracted JSON data is enclosed within "```json" and "```" delimiters, as the following code is used to parse the response:

```python
message_content = response.get("choices", )[0].get("message").get("content")
data = json.loads(message_content.split("```json\n")[1].split("\n```")[0])
"""

openai.api_key = settings.OPENAI_API_KEY

class Chatbot:
    def __init__(self):
        self.model = settings.MODEL

    def generate_response(self, user_input):
        message = prompt.replace("{}", user_input)
        msg = [{"role": "user", "content": message}]
        completion = openai.ChatCompletion.create(model=self.model, messages=msg)
        return completion
