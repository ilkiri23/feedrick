import typing as t
from collections.abc import Mapping
# from functools import partial
from sqlalchemy import select, insert, update, delete, and_
from sqlalchemy.orm import Session

from .models import Base

type ConditionOperator = t.Literal['like', '==', '>', '<', '>=', '<=']

type Condition = tuple[str, ConditionOperator, t.Any]

class BaseRepository[TModel: Base]:
    model: type[TModel]

    def __init__(self, session: Session) -> None:
        self.session = session

    def _apply_condition(self, *args: t.Any):
        ...

    def get(self, item_id: int) -> TModel:
        stmt = select(self.model).where(self.model.id == item_id)
        result = self.session.scalars(stmt).one()
        return result

    def get_many(self) -> list[TModel]:
        stmt = select(self.model)
        result = self.session.scalars(stmt).all()
        return list(result)

    def create(self, item: Mapping[str, t.Any]) -> TModel:
        stmt = (
            insert(self.model)
            .values(**item)
            .returning(self.model)
        )
        result = self.session.scalars(stmt).one()
        return result

    def create_many(self, items: list[Mapping[str, t.Any]]) -> list[TModel]:
        stmt = (
            insert(self.model)
            .values(items)
            .returning(self.model)
        )
        result = self.session.scalars(stmt).all()
        return list(result)

    def update(self, item_id: int, changes: Mapping[str, t.Any]) -> TModel:
        stmt = (
            update(self.model)
            .values(changes)
            .where(self.model.id == item_id)
            .returning(self.model)
        )   
        result = self.session.scalars(stmt).one()
        return result

    def update_many(self):
        pass

    def delete(self, item_id: int) -> TModel:
        stmt = (
            delete(self.model)
            .where(self.model.id == item_id)
            .returning(self.model)
        )
        result = self.session.scalars(stmt).one()
        return result

    def delete_many(self, conds: list[Condition] | None = None):
        pass
        # stmt = delete(self.model)
        # if conds:
        #     stmt = stmt.where(and_(*[self._apply_condition(*cond) for cond in conds]))
        # return list(self.session.scalars(stmt.returning(self.model)).all())

