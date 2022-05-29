import requests

protocol_name = 'http'
public_ip = ''
public_url = '{0}://{1}'.format(protocol_name,public_ip)
token = ''

def get_token_user_api(base_url,user_name):
  r = requests.post(base_url + '/users/{0}/tokens'.format(user_name),
    headers={
      'Authorization': 'token %s' % token,
      },
      json={
        "user_name":user_name,
        "password":"passowrd"
      }
  )
  r.raise_for_status()
  res = r.json()
  print(res)

if __name__ == '__main__':

  url = '{0}/http/hub/api'.format(public_url)
  try:
    get_token_user_api(url,'jupyter')
  except Exception as e:
    print(e)
