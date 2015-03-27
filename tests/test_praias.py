from api.models import Praia, Atividade
from tests.test_atividades import create_atividades
from base import BaseTestCase
import json

def create_praias(model, qnty):
    return Praia.objects.insert([Praia(**model)
                                 for x in range(qnty)])


class PraiaTestCase(BaseTestCase):
    def setUp(self):
        self.maxDiff = None
        surf_model = {
            'nome': 'Surf',
            'descricao': 'Surf e demais!'
        }
        sup_model = {
            'nome': 'Stand Up',
            'descricao': 'Stand Up e demais!'
        }
        self.sup = create_atividades(sup_model, 1)[0]
        self.sup['id'] = str(self.sup['id'])
        self.surf = create_atividades(surf_model, 1)[0]
        self.surf['id'] = str(self.surf['id'])
        self.model = {
            'nome': 'Porto da Barra',
            'descricao': 'Portao e sucesso!',
            'atividades': [self.surf['id'], self.sup['id']]
        }

    def tearDown(self):
        Praia.drop_collection()
        Atividade.drop_collection()

    def test_get_an_empty_list_of_praias(self):
        response = self.client.get('/v1/praias')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [])

    def test_get_a_list_of_praias(self):
        praias = create_praias(self.model, 6)
        response = self.client.get('/v1/praias')
        self.assertEqual(response.status_code, 200)
        for i, praia in enumerate(praias):
            praia._data.pop('atividades')
            response.json[i].pop('atividades')
            praia['id'] = str(praia['id'])
            self.assertEqual(response.json[i], praia._data)

    def test_post_a_praia_without_json(self):
        response = self.client.post('/v1/praias')
        self.assertEqual(response.status_code, 400)

    def test_post_a_praia(self):
        response = self.client.post('/v1/praias',
                                    data=json.dumps(self.model),
                                    content_type='application/json')
        response.json.pop('id')
        self.model['atividades'] = [self.surf._data, self.sup._data]
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, self.model)

    def test_update_an_praia(self):
        praia = create_praias(self.model, 1)[0]
        self.model['descricao'] = 'Nova descricao'
        response = self.client.put('/v1/praias/' + str(praia['id']),
                                   data=json.dumps(self.model),
                                   content_type='application/json')
        response.json.pop('id')
        response.json.pop('atividades')
        self.model.pop('atividades')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, self.model)

    def test_update_an_inexistent_praia(self):
        response = self.client.put('/v1/praias/12345ab',
                                   data=json.dumps(self.model),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_delete_a_inexistent_praia(self):
        response = self.client.delete('/v1/praias/12345ab')
        self.assertEqual(response.status_code, 404)

    def test_delete_a_praia(self):
        praia = create_praias(self.model, 1)[0]
        response = self.client.delete('/v1/praias/' + str(praia['id']))
        self.assertEqual(response.status_code, 200)
