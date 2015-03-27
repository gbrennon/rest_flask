from api import ma


class AtividadeSerializer(ma.Schema):
    id = ma.String()

    class Meta:
        additional = ('nome', 'descricao', '_links')

    _links = ma.Hyperlinks({
        'self': ma.URLFor('atividade_resource', id='<id>'),
        'collection': ma.URLFor('atividades_resource')
    })


class PraiaSerializer(ma.Schema):
    id = ma.String()
    atividades = ma.Nested(AtividadeSerializer, many=True)

    class Meta:
        additional = ('nome', 'descricao', '_links')

    _links = ma.Hyperlinks({
        'self': ma.URLFor('praia_detail', id='<id>'),
        'collection': ma.URLFor('praias_resource')
    })