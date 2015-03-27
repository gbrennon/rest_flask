from api.models import Atividade
from base import BaseTestCase
import json


def create_atividades(model, qnty):
    return Atividade.objects.insert([Atividade(**model)
                                     for x in range(qnty)])


class AtividadeTestCase(BaseTestCase):
    def setUp(self):
        self.model = {
            'nome': 'Surf',
            'descricao': 'E um esporte muito radical!'
        }

    def tearDown(self):
        Atividade.drop_collection()

    def test_get_an_empty_list_of_atividades(self):
        response = self.client.get('/v1/atividades')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_post_an_atividade_without_json(self):
        response = self.client.post('/v1/atividades')
        self.assertEqual(response.status_code, 400)

    def test_post_an_atividade(self):
        response = self.client.post('/v1/atividades',
                                    data=json.dumps(Atividade(**self.model).
                                                    _data),
                                    content_type='application/json')
        response.json.pop('id')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, self.model)

    def test_get_an_invalid_atividade(self):
        response = self.client.get('/v1/atividades/12345ab')
        self.assertEqual(response.status_code, 404)

    def test_get_an_atividade(self):
        ativ = create_atividades(self.model, 1)[0]
        response = self.client.get('/v1/atividades/' + str(ativ['id']))
        response.json.pop('id')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.model)

    def test_update_an_atividade_without_json(self):
        ativ = create_atividades(self.model, 1)[0]
        self.model['descricao'] = 'Nova descricao'
        response = self.client.put('/v1/atividades/' + str(ativ['id']))
        self.assertEqual(response.status_code, 400)

    def test_update_an_inexistent_atividade(self):
        response = self.client.put('/v1/atividades/12345ab',
                                   data=json.dumps(Atividade(**self.model).
                                                   _data),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_update_an_atividade(self):
        ativ = create_atividades(self.model, 1)[0]
        self.model['descricao'] = 'Nova descricao'
        response = self.client.put('/v1/atividades/' + str(ativ['id']),
                                   data=json.dumps(Atividade(**self.model).
                                                   _data),
                                   content_type='application/json')
        response.json.pop('id')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.model)

    def test_delete_an_inexistent_atividade(self):
        response = self.client.delete('/v1/atividades/12345ab')
        self.assertEqual(response.status_code, 404)

    def test_delete_an_atividade(self):
        ativ = create_atividades(self.model, 1)[0]
        response = self.client.delete('/v1/atividades/' + str(ativ['id']))
        self.assertEqual(response.status_code, 200)
