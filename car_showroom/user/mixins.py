class SoftDeleteMixin:

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class SerializerChooseMixin:
    default_serializer_class = None
    allow_serializer_class = {
        "retrieve": None,
        "update": None,
        "create": None,
        "list": None,
    }

    def get_serializer_class(self):
        return self.allow_serializer_class.get(self.action, self.default_serializer_class)
