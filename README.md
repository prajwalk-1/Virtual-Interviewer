# AI-Powered Virtual Interviewer

## **Overview**
AI-Powered Virtual Interviewer is an application designed to conduct mock interviews for job seekers across various domains. It generates domain-specific questions, evaluates answers, and provides constructive feedback on communication and technical skills. The platform is interactive and provides real-time feedback, scores, and improvement tips, empowering users to refine their interview skills.

---

## **Features**
- **Domain-Specific Question Generation**: Leverages an LLM (Large Language Model) to generate relevant and dynamic questions based on the selected domain.
- **Answer Evaluation**: Provides scores and feedback for user answers, assessing both technical accuracy and communication skills.
- **Real-Time Feedback**: Offers immediate suggestions to improve the user’s responses.
- **Voice Input (Optional)**: Users can submit answers through speech, with transcription via OpenAI’s Whisper API.
- **User-Friendly Interface**: Built with Streamlit for an interactive and seamless experience.

---

## **Tech Stack**
- **Backend**:
  - Large Language Model (LLM) for question generation and evaluation.
  - LangChain for context management and conversational logic.
- **Frontend**: Streamlit for UI development.
- **Optional Tools**:
  - OpenAI Whisper API for voice-to-text transcription.

---

## **Installation**
### **Prerequisites**
1. Python 3.10 or higher installed.
2. Access to OpenAI API keys (for LLM and Whisper API).
3. Pip for managing dependencies.

### **Steps**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/prajwalk-1/Virtual-Interviewer.git
   cd Virtual-Interviewer
   ```

2. **Install Dependencies**:
   Use the `requirements.txt` file to install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**:
   Create an `.env` file in the project root and add your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   WHISPER_API_KEY=your_whisper_api_key
   ```

4. **Run the Application**:
   Start the Streamlit server.
   ```bash
   streamlit run main.py
   ```

![img 1](https://github.com/user-attachments/assets/cf4c631e-f72b-408b-87be-bdc04ece134c)

![img 2](https://github.com/user-attachments/assets/8ad50f49-233d-455f-9a19-d60a88bf2831)

![3](https://github.com/user-attachments/assets/7aa08144-3c73-4cef-924e-e7b82b679c26)

![4](https://github.com/user-attachments/assets/3804eb76-dd07-4cf0-9f47-a041f79b4540)


---

## **Project Structure**
```
virtual_interviewer/
├── app/
│   ├── utils.py         # Helper functions (e.g., transcription, evaluation)
│   ├── feedback.py      # Feedback generation logic
│   ├── question_bank.py # Question generation logic
├── models/
│   └── llm_handler.py   # Large Language Model interaction
├── main.py              # Entry point for the application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .env                 # Environment variables (not included in the repo)
```

---

## **Usage**
1. Open the application in your browser after running it.
2. Select a domain (e.g., Software Development, Marketing).
3. Answer questions displayed on the screen or use the microphone for voice input.
4. Receive immediate feedback on your responses, including scores and improvement tips.
5. Repeat for as many questions or sessions as desired.

---

## **Dependencies**
- [LangChain](https://pypi.org/project/langchain/)
- [Streamlit](https://pypi.org/project/streamlit/)
- [OpenAI](https://pypi.org/project/openai/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## **Future Enhancements**
- Add support for more domains.
- Improve scoring metrics with advanced LLM models.
- Implement a progress tracker for long-term user improvement.
- Add gamification elements like badges and rankings.
