from django.apps import AppConfig


class EmprestimosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emprestimos'

    def ready(self):
        import emprestimos.signals