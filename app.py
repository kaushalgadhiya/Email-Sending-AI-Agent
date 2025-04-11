import streamlit as st
from modules import speech_to_text, email_generator, user_confirmation, send_email, feedback


st.title("📧 Voice Controlled Email Sender")

if st.button("🎤 Start Recording"):
    with st.spinner("Listening..."):
        command = speech_to_text.capture_voice()
    st.success(f"You said: {command}")

    with st.spinner("Generating email..."):
        recipient_name, recipient_email, subject, body = email_generator.generate_email(command)

    st.subheader("✉️ Generated Email")
    st.write(f"To: {recipient_name} \n Subject: {subject}\n{body}")

    # if user_confirmation.ask_for_confirmation():
    with st.spinner("Sending email..."):
        result = send_email.send_email(recipient_name, recipient_email, subject, body)

    feedback.show_result(result)
   
