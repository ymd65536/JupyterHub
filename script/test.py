import requests
token = '{token}'

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

def create_api_user(base_url,api_user_name):
  r = requests.post(base_url + '/users/' + api_user_name,
  headers={
    'Authorization': 'token %s' % token,
    }
  )
  r.raise_for_status()
  res = r.json()
  print(res)

def create_multiple_users(base_url):

  user_data = """
  {
  \"usernames\": [
    \"aaa\"
  ],
  \"admin\":\"true\"
  }
  """

  r = requests.post(base_url + '/users',user_data,
  headers={
    'Accept':'application/json',
    'Content-Type':'application/json',
    'Authorization': 'token %s' % token
    }
  )
  print(user_data)
  r.raise_for_status()
  res = r.json()
  print(res)

if __name__ == '__main__':

  url = 'http://{ip}/http/hub/api'
  # user_list(url)
  # create_api_user(url,'test')
  create_multiple_users(url)
