from typing import Any, List

from sqlalchemy.orm.session import Session

from framework.models.example_poc import ResourceModel
from framework.repositories.base import BaseRepository


class ResourceRepository(BaseRepository):

    model_class = ResourceModel
    RUNNING_STATUS = 'running'
    COMPLETE_STATUS = 'complete'

    @property
    def session(self) -> Session:
        return self.context.session

    def find_all(self) -> List[Any]:
        return self.session.query(self.model_class).all()

    def find_by_unique_key(self, dag_id: str,
                           resource_id: str) -> ResourceModel:
        return self.session.query(self.model_class).filter(
            self.model_class.dag_id == dag_id,
            self.model_class.resource_id == resource_id).one_or_none()
