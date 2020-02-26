import boto3
import os
import shutil
from subprocess import call

if not os.path.isfile('running.txt'):
  try:
    with open('running.txt', 'w') as file:
      file.write('a previously run cron job is still running...')

    local_repos = set(filter(lambda x: os.path.isdir(f'active_repos/{x}'), os.listdir('./active_repos')))

    active_repo_dict = {}
    active_repos = set()
    with open('active_repos.txt', 'r') as file:
      for line in file.readlines():
        url, name = line.strip().split(' ')
        if len(name) > 0:
          active_repos.add(name)
          active_repo_dict[name] = url

    for repo in active_repos:
      if not repo in local_repos:
        call(['git', 'clone', active_repo_dict[repo], f'active_repos/{repo}'])
      os.chdir(f'active_repos/{repo}')
      call(['git', 'pull'])
      call(['python', 'scripts/run_pipeline.py'])
      os.chdir('../..')

    repos_to_remove = local_repos - active_repos
    for repo in repos_to_remove:
      os.chdir(f'active_repos/{repo}')
      call(['git', 'pull'])
      try:
        call(['python', 'scripts/teardown.py'])
      finally:
        print('teardown complete')
      os.chdir('../..')
      shutil.rmtree(f'active_repos/{repo}')

  finally:
    os.remove('running.txt')
else:
  print('a previously run cron job is still running...')