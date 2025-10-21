class DBRouter():
    def db_for_read(self, model, **hints):
        '''
        Direciona operações de leitura para 
        o banco de dados DBMTCars quando a tabela
        for MTCars.
        '''
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def db_for_write(self, model, **hints):
        '''
        Direciona operações de escrita para
        o banco de dados DBMTCars quando a tabela
        for MTCars.
        '''
        if model._meta.db_table == 'MTCars':
            return 'DBMTCars'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.db_table == 'MTCars' or \
           obj2._meta.db_table == 'MTCars':
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        '''
        Garante que a tabela MTCars seja criada
        apenas no banco de dados DBMTCars.
        '''
        if app_label == 'exemplo':
            return db == 'DBMTCars'
        return None
        