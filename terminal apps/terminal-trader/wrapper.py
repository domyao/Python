import requests

class Markit:
    def __init__(self):
        # ?input=
        self.lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json"
        # ?symbol=
        self.quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json"


    def company_search(self, string):
        look_up = self.lookup_url + '?input=' + string
        r = requests.get(look_up)

        if r.status_code != 200:
            return ['ServerBusy']

        return r.json()


    def get_quote(self, string):
        quote = self.quote_url + '?symbol=' + string
        q = requests.get(quote)

        if q.status_code != 200:
            return {'ServerBusy': True}

        return q.json()


if __name__ == '__main__':
    MI = Markit()
