from flask.ext.restful import Resource
from api import api, request, abort
from api.models import Atividade
from api.serializers import AtividadeSerializer


class AtividadeListView(Resource):
    def get(self):
        atividades = Atividade.objects.all()
        return AtividadeSerializer(atividades, many=True).data

    def post(self):
        if not request.json:
            abort(400)
        atividade = Atividade(**request.json)
        atividade.save()
        return AtividadeSerializer(atividade).data, 201


class AtividadeView(Resource):
    def get(self, id):
        atividade = Atividade.objects.get_or_404(id=id)
        return AtividadeSerializer(atividade).data

    def put(self, id):
        if not request.json:
            abort(400)
        atividade = Atividade.objects.get_or_404(id=id)
        for key, element in request.json.items():
            atividade[key] = element
        atividade.save()
        return AtividadeSerializer(atividade).data, 200

    def delete(self, id):
        Atividade.objects.get_or_404(id=id).delete()
        return '', 200


class AtividadeResourceView(Resource):
    def get(self, id, resource):
        try:
            atividade = Atividade.objects.get_or_404(id=id)
            return AtividadeSerializer(atividade).data[resource]
        except KeyError:
            return 'Invalid attribute. Send me a activity valid attribute', 400

api.add_resource(AtividadeListView, '/v1/atividades',
                 endpoint='atividades_resource')
api.add_resource(AtividadeView, '/v1/atividades/<id>',
                 endpoint='atividade_detail')
api.add_resource(AtividadeResourceView, '/v1/atividades/<id>/<resource>')
