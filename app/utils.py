from models.llm_handler import LLM

def transcribe_voice(audio_file):
    # Stub for OpenAI Whisper API (or other speech-to-text API)
    return "Transcribed text from audio."

def evaluate_answer(answer, question):
    llm = LLM()
    score, feedback = llm.evaluate_answer(question, answer)
    return score, feedback
