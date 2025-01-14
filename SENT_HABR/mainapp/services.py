def get_all_articles(queryset):
    """Возвращает все неудаленные и опубликованные статьи, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, is_published=True)


def get_articles_by_section(queryset, section_slug):
    """Возвращает все неудаленные и опубликованные статьи из раздела section_slug, отсортированные по дате изменения"""
    return queryset.filter(is_active=True, is_published=True, section__slug=section_slug)
