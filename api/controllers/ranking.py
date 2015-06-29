from flask.ext.restful import Resource
from api import api
from flask import request, abort
from api.models import Ranking
from api.serializers import RankingSerializer


class RankingListView(Resource):
    def get(self):
        rankings = Ranking.objects.all()
        return RankingSerializer(rankings, many=True).data

    def post(self):
        if not request.json:
            abort(400)
        ranking = Ranking(**request.json)
        ranking.save()
        return RankingSerializer(ranking).data, 201


class RankingView(Resource):
    def get(self, id):
        ranking = Ranking.objects.get_or_404(id=id)
        return RankingSerializer(ranking).data

    def put(self, id):
        if not request.json:
            abort(400)
        ranking = Ranking.objects.get_or_404(id=id)
        for key, element in request.json.items():
            ranking[key] = element
        ranking.save()
        return RankingSerializer(ranking).data, 200

    def delete(self, id):
        Ranking.objects.get_or_404(id=id).delete()
        return '', 200


class RankingResourceView(Resource):
    def get(self, id, resource):
        try:
            ranking = Ranking.objects.get_or_404(id=id)
            return RankingSerializer(ranking).data[resource]
        except KeyError:
            return 'Invalid attribute. Send me a activity valid attribute',
        400

api.add_resource(RankingListView, '/api/v1/rankings',
                 endpoint='rankings_resource')
api.add_resource(RankingView, '/api/v1/rankings/<id>',
                 endpoint='ranking_detail')
api.add_resource(RankingResourceView, '/api/v1/rankings/<id>/<resource>')
