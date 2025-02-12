from database import TasksOrm, new_session
from schemas import STaskAdd
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, task: STaskAdd):
        # Создание сессии через контекстный менеджер
        async with new_session() as session:
            task_dict = task.model_dump()  # Преобразуем схему в словарь

            task_orm = TasksOrm(**task_dict)  # Создаем ORM объект
            session.add(task_orm)  # Добавляем в сессию
            await session.commit()  # Сохраняем в БД
            return task_orm.id  # Возвращаем id добавленной задачи

    @classmethod
    async def find_all(cls):
        # Создание сессии через контекстный менеджер
        async with new_session() as session:
            query = select(TasksOrm)  # Создаем запрос на выборку всех задач
            result = await session.execute(query)  # Выполняем запрос
            task_models = result.scalars().all()  # Получаем все задачи как объекты
            return task_models  # Возвращаем список задач