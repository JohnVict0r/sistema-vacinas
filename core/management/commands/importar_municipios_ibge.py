from django.core.management import BaseCommand

from core.process import ImportingManager

class Command(BaseCommand):
    help = 'Importar dados dos municipios do IBGE'

    def handle(self, *args, **options):
        manager = ImportingManager()
        try:
            manager.process()
            self.stdout.write(self.style.SUCCESS('Municipios capturados!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Algum erro ocorreu!'))
            raise e