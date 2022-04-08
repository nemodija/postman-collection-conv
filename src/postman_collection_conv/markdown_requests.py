# -*- coding: utf-8 -*-

import json
from argparse import ArgumentParser

class Postman:
  def __init__(self, collection_path, environment_path = None):
    if environment_path:
      with open(environment_path, 'r') as f:
        self.environment = json.loads(f.read())

    with open(collection_path, 'r') as f:
      collection_str = f.read()
      if hasattr(self, 'environment'):
        for param in list(filter(lambda x: x.get('enabled'), self.environment.get('values'))):
          collection_str = collection_str.replace('{{{{{}}}}}'.format(param.get('key')), param.get('value'))
      self.collection = json.loads(collection_str)

    self.case_layer_level = 6

  def convert(self):
    ret = []
    ret.append('# {}'.format(self.collection.get('info').get('name')))
    ret.append('')

    ret.extend(
      self.make_table_markdown(
        self.requests(self.collection.get('item'))))

    return ret

  def requests(self, items, name = None):
    ret = []
    for item in items:
      if ('request' in item):
        request_body = item.get('request').get('body')
        json_str = json.dumps(json.loads(request_body.get('raw'))) if \
          request_body and \
          request_body.get('mode') == 'raw' and \
          request_body.get('options').get('raw').get('language') == 'json' else ''
        ret.append([
          '{} / {}'.format(name, item.get('name')),
          '`{}`'.format(item.get('request').get('method')),
          item.get('request').get('url').get('raw'),
          json_str
        ])

      else:
        ret.extend(self.requests(
          item.get('item', []),
          item.get('name') if name is None else '{} / {}'.format(name, item.get('name'))
        ))

    return ret

  def make_table_markdown(self, table_list):
    ret = []
    if table_list:
      ret.append('|Case|Method|Url|Body|')
      ret.append('|--|--|--|--|')
      for name, method, url, body in table_list:
        ret.append('|{}|{}|{}|{}|'.format(name, method, url, body))
    return ret

def get_option():
  argparser = ArgumentParser()
  argparser.add_argument('-c', '--collection', required=True)
  argparser.add_argument('-e', '--environment')
  return argparser.parse_args()

def main():
  args = get_option()
  postman = Postman(args.collection, args.environment)
  print('\n'.join(postman.convert()))

if __name__ == "__main__":
  main()
