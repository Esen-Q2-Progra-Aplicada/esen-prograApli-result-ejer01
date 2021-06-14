from flask_restful import Resource, reqparse
from logic.empresa_logic import EmpresaLogic


class Empresa(Resource):
    def __init__(self):
        self.empresa_put_args = self.createParser()
        self.logic = EmpresaLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("nombre", type=str, help="nombre de la empresa")
        args.add_argument("contactoEmail", type=str, help="contacto de la empresa")
        args.add_argument("ingresos", type=int, help="ingresos de la empresa")
        args.add_argument("egresos", type=int, help="egresos de la empresa")
        return args

    def head(self, id):
        pass

    def get(self, id):
        result = self.logic.getEmpresaById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def post(self, id):
        result = self.logic.getEmpresaById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def put(self, id):
        empresa = self.empresa_put_args.parse_args()
        rows = self.logic.insertEmpresa(empresa)
        return {"rowsAffefcted": rows}, 200

    def patch(self, id):
        empresa = self.empresa_put_args.parse_args()
        rows = self.logic.updateEmpresa(id, empresa)
        return {"rowsAffefcted": rows}, 200

    def delete(self, id):
        rows = self.logic.deleteEmpresa(id)
        return {"rowsAffefcted": rows}, 200
