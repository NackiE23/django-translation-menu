from django.db import models


class MenuItem(models.Model):
    class Meta:
        ordering = ['order']

    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_item = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='child_items')
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
