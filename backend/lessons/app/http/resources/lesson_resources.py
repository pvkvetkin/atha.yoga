from rest_framework.serializers import ModelSerializer

from lessons.models import Lesson, Schedule


class ScheduleResource(ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "lesson",
            "start_at",
        ]


class LessonResource(ModelSerializer):
    schedules = ScheduleResource(many=True)

    class Meta:
        model = Lesson
        fields = [
            "id",
            "name",
            "description",
            "lesson_type",
            "level",
            "single",
            "duration",
            "start_datetime",
            "deadline_datetime",
            "complexity",
            "teacher",
            "repeat_editing",
            "payment",
            "price",
            "schedules",
        ]
