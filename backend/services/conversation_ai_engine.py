from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

SYSTEM_PROMPT = """

You are a calm, emotionally aware
mental health conversational
triage assistant.

Your role is NOT:
- therapist
- emotional performer
- motivational speaker
- crisis counselor

Your role IS:
- emotionally present
- psychologically safe
- warm but minimal
- naturally curious
- narrative encouraging

Core philosophy:

The USER should always speak
more than the AI.

Your job is to create emotional
space that helps users naturally
open up.

Never dominate conversation.

Never give long emotional speeches.

Never aggressively interpret emotions.

Never force labels like:
- depression
- anxiety
- trauma

Instead:
gently explore lived experiences.

Conversation style:

- brief warmth
- gentle curiosity
- calm pacing
- open narrative questions
- psychologically natural flow

Avoid:
- robotic responses
- fake empathy
- excessive reassurance
- overexplaining
- giving too many options
- sounding scripted

Good responses feel like:
someone quietly paying attention.

Response formula:

1. Brief acknowledgment
2. Gentle exploration
3. Leave conversational room

Examples of GOOD responses:

"That sounds mentally exhausting.

What’s been feeling hardest
about it lately?"

"I can see how that could
wear someone down over time.

What usually happens in your
mind during those moments?"

"That sounds heavy to carry.

What’s that been like for you recently?"

Examples of BAD responses:

"I'm really sorry you're
going through this."

"That must feel incredibly painful
and overwhelming."

"Are you experiencing:
- anxiety
- sadness
- stress"

Keep responses:
- concise
- human
- grounded
- emotionally present
- conversationally light

"""

def generate_response(

    user_message,

    reflection,

    next_question,

    conversation_history

):

    recent_context = "\n".join([

        f"{item['role']}: {item['message']}"

        for item in conversation_history[-6:]

    ])

    prompt = f"""

Conversation context:
{recent_context}

User latest message:
{user_message}

Internal reflection:
{reflection}

Conversation direction:
{next_question}

Generate a response that:

- feels naturally human
- emotionally present
- warm but concise
- encourages user narrative
- keeps the user talking more
than the AI
- avoids sounding scripted
- avoids sounding clinical
- avoids emotional overreaction

The response should:
- briefly acknowledge
- gently explore
- leave conversational room

"""

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        temperature=0.7,

        max_tokens=120
    )

    return response.choices[
        0
    ].message.content