import requests

protocol_name = 'http'
public_ip = ''
public_url = '{0}://{1}'.format(protocol_name,public_ip)
token = ''

def stop_server_api(base_url,user_name):
  r = requests.delete(base_url + '/users/{0}/server'.format(user_name),
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
    stop_server_api(url,'nonadmin')
  except Exception as e:
    print(e)