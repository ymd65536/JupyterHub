import requests

protocol_name = 'http'
public_ip = ''
public_url = '{0}://{1}'.format(protocol_name,public_ip)
token = ''

def delete_token_user_api(base_url,user_name,token_id):
  r = requests.delete(base_url + '/users/{0}/tokens/{1}'.format(user_name,token_id),
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
    delete_token_user_api(url,'jupyter','a39')
  except Exception as e:
    print(e)
