import sys
import os

from time import sleep
from subprocess import run, Popen

DANS_BASE = os.path.expanduser('~/github/Dans-labs')
FMT_BASE = f'{DANS_BASE}/formats'

HELP = f'''
python3 build.py command

command:

-h
--help
help  : print help and exit

docs  : serve docs locally
g     : push to github, code and docs

For g you need to pass a commit message as well.
'''


def readArgs():
  args = sys.argv[1:]
  if not len(args) or args[0] in {'-h', '--help', 'help'}:
    console(HELP)
    return (False, None, [])
  arg = args[0]
  if arg not in {
      'g', 'docs',
  }:
    console(HELP)
    return (False, None, [])
  if arg in {'g'}:
    if len(args) < 2:
      console('Provide a commit message')
      return (False, None, [])
    return (arg, args[1], args[2:])
  return (arg, None, [])


def console(msg, error=False, newline=True):
  msg = msg[1:] if msg.startswith('\n') else msg
  msg = msg[0:-1] if msg.endswith('\n') else msg
  target = sys.stderr if error else sys.stdout
  nl = '\n' if newline else ''
  target.write(f'{msg}{nl}')
  target.flush()


def commit(task, msg):
  run(['git', 'add', '--all', '.'])
  run(['git', 'commit', '-m', msg])
  run(['git', 'push', 'origin', 'master'])


def shipDocs():
  run(['mkdocs', 'gh-deploy'])


def serveDocs():
  proc = Popen(['mkdocs', 'serve'])
  sleep(3)
  run('open http://127.0.0.1:8000', shell=True)
  try:
    proc.wait()
  except KeyboardInterrupt:
    pass
  proc.terminate()


def main():
  (task, msg, remaining) = readArgs()
  if not task:
    return
  elif task == 'docs':
    serveDocs()
  elif task == 'g':
    shipDocs()
    commit(task, msg)


main()
