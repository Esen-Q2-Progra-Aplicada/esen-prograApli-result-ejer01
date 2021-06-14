from core.pyba_logic import PybaLogic


class EmpresaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def getEmpresaById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from empresa where id={id};"
        result = database.executeQuery(sql)
        return result

    def insertEmpresa(self, empresa):
        database = self.createDatabaseObj()
        sql = (
            f"INSERT INTO `empresadb`.`empresa`"
            + f"(`id`,`nombre`,`contacto_email`,`ingresos`,`egresos`) "
            + f"VALUES(0, '{empresa['nombre']}', '{empresa['contactoEmail']}', "
            + f"{empresa['ingresos']}, {empresa['egresos']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateEmpresa(self, id, empresa):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE `empresadb`.`empresa` "
            + f"SET `nombre` = '{empresa['nombre']}', `contacto_email` = '{empresa['contactoEmail']}', "
            + f"`ingresos` = {empresa['ingresos']}, `egresos` = {empresa['egresos']} "
            + f"WHERE `id` = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteEmpresa(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from empresa where id={id};"
        rows = database.executeNonQueryRows(sql)
        return rows
