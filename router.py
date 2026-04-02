from aiogram import Router, types, F
from aiogram.filters import Command
from config import GROQ_TOKEN, DEV_ID
from groq import AsyncGroq
from sexualPrompt import prompt

router = Router()
client = AsyncGroq(api_key=GROQ_TOKEN)
aiPrompt = prompt

# @router.message(Command("start"))
# async def start_command_handler(message: types.Message) -> None:
#     await message.answer("Привет")

@router.message()
async def ai_chat_handler(message: types.Message) -> None:
    if message.from_user.id != DEV_ID:
        return
    text = message.text
    chat_completion = await client.chat.completions.create(
        #
        # Required parameters
        #
        messages=[
            # Set an optional system message. This sets the behavior of the
            # assistant and can be used to provide specific instructions for
            # how it should behave throughout the conversation.
            {
                "role": "system",
                "content": aiPrompt
            },
            # Set a user message for the assistant to respond to.
            {
                "role": "user",
                "content": text,
            }
        ],

        # The language model which will generate the completion.
        # model="llama-3.1-8b-instant",
        model="llama-3.3-70b-versatile",
        # model="openai/gpt-oss-120b",

        #
        # Optional parameters
        #

        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become
        # deterministic and repetitive.
        temperature=0.82,

        # The maximum number of tokens to generate. Requests can use up to
        # 2048 tokens shared between prompt and completion.
        max_completion_tokens=500,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=0.9,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )
    try:
        await message.answer(chat_completion.choices[0].message.content)
    except Exception as e:
        print(f"Ошибка: {e}")
        await message.answer("Произошла ошибка")