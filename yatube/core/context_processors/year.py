def year(request):
    """Добавляет в контекст переменную year с приветствием."""
    return {
        'year': '2025',
        }