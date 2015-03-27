from flask.ext.restful import Resource
from api import api, request, abort
from api.models import Praia
from api.serializers import PraiaSerializer


class PraiaListView(Resource):
    def get(self):
        praias = Praia.objects.all()
        return PraiaSerializer(praias, many=True).data

    def post(self):
        if not request.json:
            abort(400)
        praia = Praia(**request.json)
        praia.save()
        return PraiaSerializer(praia).data, 201


class PraiaView(Resource):
    def get(self, id):
        praia = Praia.objects.get_or_404(id=id)
        return PraiaSerializer(praia).data

    def put(self, id):
        if not request.json:
            abort(400)
        praia = Praia.objects.get_or_404(id=id)
        praia = Praia(**request.json)
        praia.save()
        return PraiaSerializer(praia).data, 200

    def delete(self, id):
        praia = Praia.objects.get_or_404(id=id)
        praia.delete()
        return '', 200


class PraiaResourceView(Resource):
    def get(self, id, resource):
        try:
            praia = Praia.objects.get_or_404(id=id)
            return PraiaSerializer(praia).data[resource]
        except KeyError:
            return 'Invalid attribute. Send me a activity valid attribute', 400

api.add_resource(PraiaListView, '/v1/praias',
                 endpoint='praias_resource')
api.add_resource(PraiaView, '/v1/praias/<id>',
                 endpoint='praia_detail')
api.add_resource(PraiaResourceView, '/v1/praias/<id>/<resource>')
