import uuid as uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django_jsonform.models.fields import JSONField

User = get_user_model()

SCENARIO_STATUS = [
    (0, 'Не автоматизирован'),
    (1, 'Автоматизирован'),
    (2, 'Пропущен'),
    (3, 'Не актуален'),
]
class FeatureTest(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    level = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=False, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('feature_list', kwargs={'feature_slug': self.slug})


class TestCase(models.Model):
    SCENARIO_SCHEMA_JSON = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://example.com/product.schema.json",
        "title": "Test case scenario",
        "description": "Scenario for QA",
        "type": "object",
        "properties": {
            "pred_step": {
                "title": "Предусловие",
                "type": "string",
            },
            "steps": {
                "type": "array",
                "title": "Шаги",
                "items": {
                    "type": "object",
                    "keys": {
                        "step": {
                            "type": "string",
                             "title": "Шаг",
                        },
                        "expectedResult": {
                            "type": "string",
                            "title": "Ожидаемый результат",
                        }
                    }
                }
            }
        }
    }
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Название сценария')
    status = models.PositiveSmallIntegerField(default=0, choices=SCENARIO_STATUS, verbose_name='Статус')
    test_body = JSONField(schema=SCENARIO_SCHEMA_JSON, verbose_name='Шаги')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    last_update_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test')
    feature = models.ForeignKey(
        FeatureTest,
        help_text='Группа, к которой будет относиться пост',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='tests'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tests', kwargs={'feature_slug': self.slug})

    def get_name(self):
        return self.name


class Comment(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, )
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    scenario_public = models.ForeignKey(TestCase, related_name="commented_post", on_delete=models.CASCADE, null=True)
    # testrun_public = models.OneToOneField(TestRun, related_name='+', on_delete=CASCADE, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'title={self.text}, pk={self.pk}, author={self.author}'


class History(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.text


