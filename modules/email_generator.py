# import openai

# openai.api_key = "YOUR_OPENAI_API_KEY"

# def generate_email(command):
#     prompt = f"Extract recipient name and create a professional email from: '{command}'"
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     content = response.choices[0].message.content.strip()
#     lines = content.split('\n')
#     recipient = lines[0].split(":")[-1].strip()
#     subject = lines[1].split(":")[-1].strip()
#     body = "\n".join(lines[2:]).strip()
#     return recipient, subject, body

import requests
from . import contact_lookup

def generate_email(command):
    prompt = f"""Extract the recipient name, subject, and generate a professional email based on the following command:
    
    \"\"\"{command}\"\"\"
    Please Follow strictyl format.
    Format:
    Recipient: <name>
    Subject: <subject>
    Body:
    <email body>
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2", "prompt": prompt, "stream": False}
    )
    
    # content = response.json()['response'].strip()
    
    # lines = content.split('\n')
    # print("Content:-",content)
    # print()
    # recipient_name = lines[0].split(":", 1)[-1].strip()
    # print()
    # print("Name is ",recipient_name)
    # print()
    # recipient_email = contact_lookup.get_email(recipient_name)
    # subject = lines[1].split(":", 1)[-1].strip()
    # body = "\n".join(lines[3:]).strip()
    # content = response.json()['response'].strip()
    # print("Content:-", content)
    # print()

    # lines = content.splitlines()
    # recipient_name = ""
    # subject = ""
    # body = ""

    # # Step 1: Extract recipient name
    # for line in lines:
    #     if line.lower().startswith("recipient:"):
    #         recipient_name = line.split(":", 1)[1].strip()
    #         break

    # print(f"Name is: {recipient_name}")
    # print()

    # # Step 2: Extract email using contact_lookup
    # # recipient_email = contact_lookup.get_email(recipient_name)

    # # Step 3: Extract subject
    # for line in lines:
    #     if line.lower().startswith("subject:"):
    #         subject = line.split(":", 1)[1].strip()
    #         break
    # print("Subject is : ",subject)
    # print()
    # # Step 4: Extract email body (lines after "Body:" or after Subject line)
    # body_start_index = 0
    # for i, line in enumerate(lines):
    #     if line.strip().lower().startswith("body:"):
    #         body_start_index = i + 1
    #         break
    # else:
    #     # fallback if "Body:" is not mentioned
    #     body_start_index = lines.index(subject) + 1 if subject in lines else 3

    # body = "\n".join(lines[body_start_index:]).strip()
    # print("Body is :-",body)

    # return recipient_name, recipient_email, subject, body



    content = response.json()['response'].strip()
    print("Content:-", content)
    print()

    lines = content.splitlines()
    recipient_name = ""
    subject = ""
    body = ""

    # Extract recipient name
    for i, line in enumerate(lines):
        if line.lower().startswith("recipient:"):
            recipient_name = line.split(":", 1)[1].strip()
            recipient_line_idx = i
            break

    

    # Extract email using contact_lookup
    recipient_email = contact_lookup.get_email(recipient_name)

    # Extract subject
    for i, line in enumerate(lines):
        if line.lower().startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
            subject_line_idx = i
            break

    

    # Body starts after subject line
    body_start_index = subject_line_idx + 1
    body = "\n".join(lines[body_start_index:]).strip()

    # OPTIONAL: Remove duplicate "Subject:" line in body, if exists
    if body.lower().startswith("subject:"):
        body = "\n".join(lines[body_start_index + 1:]).strip()

    print(f"\nName is: {recipient_name}")
    print(f"\nSubject is : {subject}")
    print(f"\nBody is :-\n{body}")

    return recipient_name, recipient_email, subject, body


