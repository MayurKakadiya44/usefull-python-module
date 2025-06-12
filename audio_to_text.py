# Example 1: Podcast Transcription with Timestamps
# Scenario: You want to transcribe a 30-second clip from an English podcast and generate subtitles with timestamps.

from transformers import pipeline
import torch

# Initialize Whisper pipeline (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3",
    device=device
)

# Load audio file (e.g., WAV, MP3)
audio = "podcast_clip.wav"

# Transcribe with timestamps
result = pipe(
    audio,
    generate_kwargs={
        "task": "transcribe",
        "language": "english",
        "return_timestamps": True
    }
)

# Output transcription and timestamps
print("Transcription:", result["text"])
print("Timestamps:", result["chunks"])

# OP :
# Transcription: Welcome to our podcast on AI trends. Today, we discuss generative models.
# Timestamps: [
#     {"timestamp": [0.0, 2.5], "text": "Welcome to our podcast on AI trends."},
#     {"timestamp": [2.6, 5.0], "text": "Today, we discuss generative models."}
# ]

#=======================================
#=======================================

# Example 2: Speech Translation for a Spanish Interview
# Scenario: You have a Spanish audio interview and want to translate it to English text.



from transformers import pipeline
import torch

# Initialize Whisper pipeline
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3",
    device=device
)

# Load audio file
audio = "spanish_interview.wav"

# Translate to English
result = pipe(
    audio,
    generate_kwargs={
        "task": "translate",
        "language": "spanish"
    }
)

# Output translated text
print("Translation:", result["text"])

#=======================================
#=======================================

# Example 3: Integration with Langfuse for Monitoring
# Scenario: You’re building a voice-to-text customer support system and want to monitor Whisper’s performance using Langfuse.

from transformers import pipeline
from langfuse import get_client
import torch

# Initialize Langfuse and Whisper
langfuse = get_client()
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3", device=device)

# Process audio
audio = "customer_call.wav"
result = pipe(audio, generate_kwargs={"task": "transcribe", "language": "english"})

# Log to Langfuse
langfuse.trace(
    name="customer_support_transcription",
    input=audio,
    output=result["text"],
    metadata={"model": "whisper-large-v3", "language": "english"}
)

# Output
print("Transcription:", result["text"])
