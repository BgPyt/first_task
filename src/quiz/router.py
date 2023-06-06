from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from src.quiz.models import Quiz
from src.quiz.shemes import Questions
from aiohttp import ClientSession
from src.database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

app = APIRouter()


async def get_last_question(session: AsyncSession):
    stmt = select(Quiz)
    result = await session.execute(stmt)
    return result.all()


@app.post('/question')
async def question(item: Questions, session: AsyncSession = Depends(get_async_session)):
    last: [Quiz] = [j for i in await get_last_question(session) for j in i]
    async with ClientSession() as client:
        quantity = item.questions_num
        added_object = []
        while True:
            response = await client.get(f"https://jservice.io/api/random?count={quantity}")
            for obj in await response.json():
                ModelQuiz = Quiz(
                    text_question=obj['question'],
                    text_answer=obj['answer'],
                )
                if ModelQuiz not in last and ModelQuiz not in added_object:
                    added_object.append(ModelQuiz)
                    quantity -= 1
                else:
                    continue
            if not quantity:
                break

    session.add_all(added_object)
    await session.commit()

    try:
        last = last[-1]
        return last.text_question
    except IndexError:
        return []



















