import csv
import logging
import os
from abc import ABC, abstractmethod
from core.models import Uf, Municipio, Estabelecimento

logging.basicConfig(level=logging.INFO)

class IBGEImporter:
    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')

    def process(self):
        logging.info(f'{self.__class__.__name__} processando...')

        with open('core/data/municipios_ibge.csv', 'r') as arquivo_csv:
            self.data = csv.DictReader(arquivo_csv, delimiter=',')
            for coluna in self.data:
                uf, created = Uf.objects.get_or_create(cod=coluna['UF'], name=coluna['Nome_UF'])
                
                logging.info(f'{self.__class__.__name__} UF {uf.name} importado!')
                
                municipio, created = Municipio.objects.get_or_create(cod_uf=uf, cod=coluna['Codigo_Municipio'], name=coluna['Nome_Municipio'])
                
                logging.info(f'{self.__class__.__name__} Municipio {municipio.name} importado!')

class EstabelecimentoImporter:
    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')

    def process(self):
        logging.info(f'{self.__class__.__name__} processando...')

        with open('core/data/estabelecimentos_saude.csv', 'r') as arquivo_csv:
            self.data = csv.DictReader(arquivo_csv, delimiter=',')
            for coluna in self.data:
                municipio = Municipio.objects.get(pk=coluna['CO_MUNICIPIO_GESTOR'])

                estabelecimento, created = Estabelecimento.objects.get_or_create(
                    co_unidade = coluna['CO_UNIDADE'],
                    co_cnes = coluna['CO_CNES'],
                    nu_cnpj = coluna['NU_CNPJ_MANTENEDORA'],
                    no_razao_social = coluna['NO_RAZAO_SOCIAL'],
                    no_fantasia = coluna['NO_FANTASIA'],
                    nu_latitude = coluna['NU_LATITUDE'],
                    nu_longitude = coluna['NU_LONGITUDE'],
                    no_logradouro = coluna['NO_LOGRADOURO'],
                    nu_endereco = coluna['NU_ENDERECO'],
                    no_complemento = coluna['NO_COMPLEMENTO'],
                    no_bairro = coluna['NO_BAIRRO'],
                    co_cep = coluna['CO_CEP'],
                    co_municipio_gestor = municipio)
                
                logging.info(f'{self.__class__.__name__} Estabelecimento {estabelecimento.no_fantasia} importado!')
                
        
class ImportingManager(object):
    IMPORTERS = [IBGEImporter, EstabelecimentoImporter]

    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')
        self.importers = []
        self.initialize_importers()

    def initialize_importers(self):
        logging.info(f'{self.__class__.__name__} instanciando importers...')
        for importer_cls in self.IMPORTERS:
            importer = importer_cls()
            self.importers.append(importer)

    def process(self):
        logging.info(f'{self.__class__.__name__} processando os dados...')
        for importer in self.importers:
            importer.process()