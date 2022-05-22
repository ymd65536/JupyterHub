# 検証用コンフィグ

c.JupyterHub.confirm_no_ssl = True
c.JupyterHub.base_url = '/'

c.Authenticator.admin_users = {'jupyter'}
user_path = '/home/{username}/notebooks'
c.Spawner.notebook_dir = user_path
c.Spawner.default_url = user_path

# ユーザ作成
c.LocalAuthenticator.create_system_users=True
c.LocalAuthenticator.add_user_cmd = ['./add_user.sh']
