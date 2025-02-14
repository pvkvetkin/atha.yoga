from typing import Optional

from django.db.models import QuerySet, Prefetch

from core.app.repositories.base_repository import BaseRepository
from core.models import User, QuestionnaireTeacher, QuestionnaireTeacherStatuses


class UserRepository(BaseRepository):
    model = User

    def store(self, user: User) -> None:
        user.save()

    def find_user_by_email(self, email: str) -> Optional[User]:
        return User.objects.filter(email=email).first()

    def find_by_id(self, id_: int, fetch_rels: bool = False) -> Optional[User]:
        query = self.model.objects.filter(pk=id_)
        if fetch_rels:
            query = self.fetch_relations(queryset=query)
        return query.first()

    def fetch_relations(self, queryset: QuerySet[User]) -> QuerySet[User]:
        """
        Append attributes to each user in queryset: \n
        - **public_teacher_profiles**: All teacher profiles with `ACCEPTED` status
        """
        return queryset.prefetch_related(
            Prefetch(
                "teacher_profiles",
                QuestionnaireTeacher.objects.filter(
                    status=QuestionnaireTeacherStatuses.ACCEPTED.value
                ),
                to_attr="public_teacher_profiles",
            )
        )
