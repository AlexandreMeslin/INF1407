class DBRouter():
    def db_for_read(self, model, **hints):
        '''
        Decide de qual banco ler dados de um modelo.
        
        :param self: Description
        :param model: Description
        :param hints: Description
        '''
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None
    
    def db_for_write(self, model, **hints):
        '''
        Decide de qual banco escrever dados de um modelo.
        
        :param self: Description
        :param model: Description
        :param hints: Description
        '''
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        '''
        Define se dois modelos podem ter relação (FK, M2M).
        
        :param self: Description
        :param obj1: Description
        :param obj2: Description
        :param hints: Description
        '''
        if obj1._meta.db_table == 'MTCars' or \
           obj2._meta.db_table == 'MTCars':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        '''
        Define se um modelo pode ser migrado para um banco de dados específico.
        
        :param self: Description
        :param db: Nome do banco de dados.
        :param app_label: Nome do app Django onde o modelo está definido.
        :param model_name: Nome do modelo (opcional).
        :param hints: Dicas internas do ORM (ex: instance, relation)
        '''
        if app_label == 'MeuSite':
            return db == 'DBMTCars'
        return None
