import requests

protocol_name = 'http'
public_ip = ''
public_url = '{0}://{1}'.format(protocol_name,public_ip)
token = ''

def list_tokens_api(base_url,user_name):
  r = requests.get(base_url + '/users/{0}/tokens'.format(user_name),
    headers={
      'Authorization': 'token %s' % token,
      }
    )
  r.raise_for_status()
  res = r.json()
  print(res)

if __name__ == '__main__':

  url = '{0}/http/hub/api'.format(public_url)
  try:
    list_tokens_api(url,'jupyter')
  except Exception as e:
    print(e)
