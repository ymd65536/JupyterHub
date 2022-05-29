import requests

protocol_name = 'http'
public_ip = ''
public_url = '{0}://{1}'.format(protocol_name,public_ip)
token = ''

# ユーザの一覧を表示
def user_list(base_url):
  r = requests.get(base_url + '/users',
  headers={
  'Authorization': 'token %s' % token,
  }
  )

  r.raise_for_status()
  res = r.json()
  print(res)

if __name__ == '__main__':

  url = '{0}/http/hub/api'.format(public_url)
  user_list(url)