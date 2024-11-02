class TestrailFacade:
    def __init__(self, client):
        self.client = client

    def update_run(self, body, test_run_id: int):
        return self.client.send_post(f'update_run/{test_run_id}', body)


    def get_tests(self, test_run_id: int, query: str):
        result = {
            'tests': []
        }
        one = self.client.send_get(f'get_tests/{test_run_id}{query}')
        while True:
            result['tests'].extend(one['tests'])
            links = one['_links']
            next_ = links['next']
            print(repr(links))
            if not next_:
                break
            one = self.client.send_get(next_[8:])
        return result


    def get_statuses(self):
        return self.client.send_get('get_statuses')

    @staticmethod
    def get_case_id_from_run_tests(ids: list, tests):
        for test in tests['tests']:
            ids.append(test['case_id'])

    def get_test(self, test_id: int):
        return self.client.send_get(f'get_test/{test_id}')
