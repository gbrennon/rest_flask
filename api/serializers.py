from api import ma


class RankingSerializer(ma.Schema):
    class Meta:
        additional = ('nome', 'email', 'avatar', 'pontos', '_links')

    _links = ma.Hyperlinks({
        'self': ma.URLFor('ranking_detail', id='<id>'),
        'collection': ma.URLFor('rankings_resource')
    })
