import streamlit as st
from openai import OpenAI
from io import BytesIO
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph

def request_gpt(input_file, prompt, model_ai):
    # Connect to Openai API
    client = OpenAI(api_key=st.secrets["key"])

    files_id = []
    for file in input_file:
        files_id.append(client.files.create(
            file=file,
            purpose='assistants').id)

    assistant = client.beta.assistants.create(
        model=model_ai,
        instructions="You are an employer in Credit Risk Modeling Department in a Bank.",
        name="Summary Assistant",
        tools=[{"type": "file_search"}]
    ).id

    # Create thread
    my_thread = client.beta.threads.create()

    attachments = [{"file_id": file_id, "tools": [{"type": "file_search"}]} for file_id in files_id]

    my_thread_message = client.beta.threads.messages.create(
        thread_id=my_thread.id,
        role="user",
        content=prompt,
        attachments=attachments
    )


    # Run
    my_run = client.beta.threads.runs.create(
        thread_id = my_thread.id,
        assistant_id = assistant,
        instructions="Your job is to Answer the user's question.",
    )

    while my_run.status in ["queued", "in_progress"]:
        keep_retrieving_run = client.beta.threads.runs.retrieve(
            thread_id=my_thread.id,
            run_id=my_run.id
        )
        print(f"Run status: {keep_retrieving_run.status}")

        if keep_retrieving_run.status == "completed":
            print("\n")

            all_messages = client.beta.threads.messages.list(
                thread_id=my_thread.id
            )

            st.header('Output:', divider='green')
            for txt in all_messages.data:
                if txt.role == 'assistant':
                    output = txt.content[0].text.value
                    # Remove patterns
                    output = re.sub(r'【.*?†source】', '', output)
                    print(output)
            break
        elif keep_retrieving_run.status == "queued" or keep_retrieving_run.status == "in_progress":
            pass
        else:
            print(f"Run status: {keep_retrieving_run.status}")
            st.write(f"Run status: {keep_retrieving_run.status}")
            break

    # # Delete file and agent
    # client.files.delete(gpt_file)
    # client.beta.assistants.delete(assistant)
    # client.beta.threads.delete(my_thread.id)

    st.markdown(body=output)
    st.stop() 


def chat_completion(model, prompt):
    client = OpenAI(api_key=st.secrets["key"])
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.markdown(body=completion.choices[0].message.content)
    st.stop()
