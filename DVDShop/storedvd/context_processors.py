from .models import Section


def add_default_data(request):
    # Контекст для вывода меню на всех страницах
    sections = Section.objects.order_by('title').all()
    return {'sections': sections}
