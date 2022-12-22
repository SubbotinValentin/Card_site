menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': 'Проекты', 'url_name': 'projects'},
        {'title': 'Задачи', 'url_name': 'tasks'},
        {'title': 'Добавить', 'url_name': 'addpage'}
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)

        context['menu'] = menu
        return context