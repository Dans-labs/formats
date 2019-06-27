import sys
import os
import collections
import re
from itertools import chain
from shutil import rmtree

from time import sleep
from subprocess import run, Popen

import yaml

DANS_BASE = os.path.expanduser('~/github/Dans-labs')
FMT_BASE = f'{DANS_BASE}/formats'

MKDOCS_OUT = f'{FMT_BASE}/mkdocs.yml'
MKDOCS_IN = f'{FMT_BASE}/source/mkdocsIn.yml'
URLS = f'{FMT_BASE}/source/urls.list'

DOCS = f'{FMT_BASE}/docs'
SRC = f'{FMT_BASE}/source'
DATA_TYPES = 'dataTypes'
FILE_FORMATS = 'fileFormats'
EXTENSIONS = 'extensions'
YAML = f'{SRC}/data.yaml'
INDEX = f'index.md'
HELP = f'help.md'

USAGE = '''
Run `build.py` from the Terminal as follows:

```sh
python3 build.py make
python3 build.py docs
python3 build.py g commitmsg
```

`make` compiles Markdown files from the source files.

`docs` does `make` and then serves the docs locally and them shows them in your browser.

`g` does `make`, and pushes the whole site to GitHub,
where it will be published under <https://dans-labs.github.io/formats/>.
The repo itself will also be committed and pushed to GitHub.

Replace `commitmsg` by anything that is appropriate as a commit message.

'''


def readArgs():
  args = sys.argv[1:]
  if not len(args) or args[0] in {'-h', '--help', 'help'}:
    console(USAGE)
    return (False, None, [])
  arg = args[0]
  if arg not in {
      'make', 'docs', 'g',
  }:
    console(USAGE)
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


def readYaml(fileName):
  with open(fileName) as y:
    y = yaml.load(y)
  return y


def makeDocs():

  tasks = (
      (INDEX, False),
      (HELP, False),
      (DATA_TYPES, True),
      (FILE_FORMATS, True),
      (EXTENSIONS, True),
  )
  info = readYaml(YAML)
  dataTypes = info['dataTypes']
  fileFormats = info['fileFormats']
  mapping = info['mapping']
  preferred = info['preferred']
  locations = info['locations']
  wikiloc = locations['wikipedia']
  fileinfo = locations['fileinfo']

  info['extensions'] = {}
  extensions = info['extensions']

  urls = []
  config = []

  errors = []

  dataFromFile = collections.defaultdict(set)
  dataFromExt = collections.defaultdict(set)
  filesFromData = collections.defaultdict(set)
  filesFromExt = collections.defaultdict(set)
  extsFromData = collections.defaultdict(set)
  extsFromFile = collections.defaultdict(set)
  texts = {}

  linkRe = re.compile(r'\[([=:.])(\S+)\]')
  linkMap = {
      ':': 'dataTypes',
      '=': 'fileFormats',
      '.': 'extensions',
  }

  def error(msg):
    errors.append(msg)

  def readDocInfo():

    def showErrors():
      for msg in errors:
        print(f'ERROR: {msg}')
      return len(errors)

    for (dt, ffs) in mapping.items():
      if dt not in dataTypes:
        error(f'undeclared data type "{dt}"')
      for ff in ffs:
        if ff not in fileFormats:
          error(f'undeclared file format "{ff}"')
        dataFromFile[ff].add(dt)
        filesFromData[dt].add(ff)

    for dt in dataTypes:
      if dt not in filesFromData:
        error(f'unmapped data type "{dt}"')

    for (ff, fInfo) in fileFormats.items():
      dts = dataFromFile[ff]
      if not dts:
        error(f'unmapped file format "{ff}"')
        continue
      exts = fInfo.get('extensions', [])
      for ext in exts:
        extsFromFile[ff].add(ext)
        for dt in dts:
          extsFromData[dt].add(ext)
          dataFromExt[ext].add(dt)
        filesFromExt[ext].add(ff)
        extensions[ext] = {'display': f'.{ext}'}

    srcs = []
    for (task, isDir) in tasks:
      if isDir:
        with os.scandir(f'{SRC}/{task}') as it:
          for entry in it:
            name = entry.name
            if name.endswith('.md') and entry.is_file():
              srcs.append((task, name[:-3]))
      else:
        srcs.append(('', task[:-3]))

    for (kind, item) in srcs:
      if kind and item not in info[kind]:
        error(f'File {kind}/{item}.md: no {kind} {item} declared')
        continue
      kindRep = f'/{kind}' if kind else ''
      path = f'{SRC}{kindRep}/{item}.md'
      with open(path) as f:
        text = f.read()
        if kind == '':
          texts[item] = text
        else:
          info[kind][item]['text'] = text

    for t in ('header', 'footer'):
      path = f'{SRC}/{t}.md'
      if not os.path.exists(path):
        error(f'No file {t}.md')
        text = ''
      else:
        with open(path) as f:
          text = f.read()
      text1 = text.replace('<1>', '')
      text = text.replace('<1>', '../')
      texts[t] = text
      texts[f'{t}1'] = text1

    nE = showErrors()
    if nE:
      print(f'There were {nE} errors')
      return False

    with open(URLS) as f:
      for line in f:
        (acro, url) = line.split(maxsplit=1)
        urls.append(f'  {acro}: {url}')

    with open(MKDOCS_IN) as f:
      for line in f:
        config.append(line)

    print('Doc info OK')
    return True

  def transformDoc(prefix, text):
    def linkRepl(match):
      char = match.group(1)
      item = match.group(2)
      string = f'[{char}{item}]'

      kind = linkMap.get(char, None)

      if kind is None:
        error(f'Link {string}: illegal "{char}"')
        return string
      if kind not in info:
        error(f'Link {string}: unknown kind {kind}')
        return string
      if item not in info[kind]:
        error(f'Link: unknown {kind} "{item}"')
        return string

      dName = info[kind][item]['display']
      return f'[{dName}]({prefix}{kind}/{item}.md)'

    text = linkRe.sub(linkRepl, text)
    return text

  def writeDocs():
    for (task, isDir) in tasks:
      path = f'{DOCS}/{task}'
      if os.path.exists(path):
        if isDir:
          rmtree(path)
        else:
          os.unlink(path)
      if isDir:
        os.makedirs(path, exist_ok=True)

    def writeIndex():
      text = []
      text.append(texts['header1'])
      text.append(texts['index'])
      text.append(texts['footer1'])
      text = transformDoc('', '\n'.join(text))
      path = f'{DOCS}/{INDEX}'
      with open(path, 'w') as f:
        f.write(text)

    def writeHelp():
      text = []
      text.append(texts['header1'])
      text.append(texts['help'])
      text.append(texts['footer1'])
      text = transformDoc('', '\n'.join(text))
      text = text.replace('[[usage]]', USAGE)
      path = f'{DOCS}/{HELP}'
      with open(path, 'w') as f:
        f.write(text)

    def writeDataTypes():
      for (item, itemInfo) in dataTypes.items():
        text = []
        text.append(texts['header'])

        display = itemInfo['display']
        title = itemInfo['title']
        material = itemInfo.get('text', '')
        theseFormats = ', '.join(
            f'[{fileFormats[x]["display"]}](../fileFormats/{x}.md)'
            for x in sorted(filesFromData[item])
        )
        theseExtensions = ', '.join(
            f'[`{x}`](../extensions/{x}.md)'
            for x in sorted(extsFromData[item])
        )

        text.append(f'''
# {display}

**{title}**

item | info
--- | ---
formats | {theseFormats}
extensions | {theseExtensions}

{material}
''')

        text.append(texts['footer'])
        text = transformDoc('../', '\n'.join(text))
        path = f'{DOCS}/dataTypes/{item}.md'
        with open(path, 'w') as f:
          f.write(text)

    def writeFileFormats():
      for (item, itemInfo) in fileFormats.items():
        text = []
        text.append(texts['header'])

        display = itemInfo['display']
        title = itemInfo['title']
        material = itemInfo.get('text', '')
        theseTypes = ', '.join(
            f'[{dataTypes[x]["display"]}](../dataTypes/{x}.md)'
            for x in sorted(dataFromFile[item])
        )
        thisP = preferred[itemInfo.get('preferred', 'unknown')]
        thisPreferred = f'{thisP["acro"]} {thisP["title"]}'
        theseExtensions = ', '.join(
            f'[`{extensions[x]["display"]}`](../extensions/{x}.md)'
            for x in sorted(extsFromFile[item])
        )
        theseWikis = ', '.join(
            f'[`{x}`]({wikiloc}/{x})'
            for x in itemInfo['wikipedia']
        )
        theseLinks = ''.join(
            f'*   [`{x}`]({x})\n'
            for x in itemInfo['links']
        )

        text.append(f'''
# {display}

**{title}**

item | info
--- | ---
type | {theseTypes}
preferred | {thisPreferred}
extensions | {theseExtensions}
wikipedia | {theseWikis}

{material}

## See also
{theseLinks}

''')

        text.append(texts['footer'])
        text = transformDoc('../', '\n'.join(text))
        path = f'{DOCS}/fileFormats/{item}.md'
        with open(path, 'w') as f:
          f.write(text)

    def writeExtensions():
      for (item, itemInfo) in extensions.items():
        text = []
        text.append(texts['header'])

        display = itemInfo['display']
        material = itemInfo.get('text', '')
        theseTypes = ', '.join(
            f'[{dataTypes[x]["display"]}](../dataTypes/{x}.md)'
            for x in sorted(dataFromExt[item])
        )
        theseF = filesFromExt[item]
        theseFormats = ', '.join(
            f'[{fileFormats[x]["display"]}](../fileFormats/{x}.md)'
            for x in sorted(theseF)
        )
        thisFileInfo = f'[`extension/{item}`]({fileinfo}/{item})'
        exts = chain.from_iterable(extsFromFile[x] for x in theseF)
        variantExtensions = ', '.join(
            f'[`{extensions[x]["display"]}`](../extensions/{x}.md)'
            for x in sorted(exts)
            if x != item
        )

        text.append(f'''
# {display}

item | info
--- | ---
type | {theseTypes}
format | {theseFormats}
variants | {variantExtensions}
file info | {thisFileInfo}

{material}
''')

        text.append(texts['footer'])
        text = transformDoc('../', '\n'.join(text))
        path = f'{DOCS}/extensions/{item}.md'
        with open(path, 'w') as f:
          f.write(text)

    def writeConfig():
      text = []
      for line in config:
        if '[[urls]]' in line:
          text.extend(urls)
        elif '[[dataTypes]]' in line:
          for item in sorted(
              dataTypes,
              key=lambda x: dataTypes[x]['display'],
          ):
            itemInfo = dataTypes[item]
            display = itemInfo['display']
            text.append(f"    - {display}: 'dataTypes/{item}.md'\n")
        elif '[[fileFormats]]' in line:
          for item in sorted(
              fileFormats,
              key=lambda x: fileFormats[x]['display'],
          ):
            itemInfo = fileFormats[item]
            display = itemInfo['display']
            text.append(f"    - {display}: 'fileFormats/{item}.md'\n")
        elif '[[extensions]]' in line:
          for item in sorted(
              extensions,
              key=lambda x: extensions[x]['display'],
          ):
            itemInfo = extensions[item]
            display = itemInfo['display']
            text.append(f"    - {display}: 'extensions/{item}.md'\n")
        elif '[[fileFormatsDT]]' in line:
          for item in sorted(
              dataTypes,
              key=lambda x: dataTypes[x]['display'],
          ):
            itemInfo = dataTypes[item]
            display = itemInfo['display']
            text.append(f"    - {display}:\n")
            for subitem in sorted(
                filesFromData[item],
                key=lambda x: fileFormats[x]['display'],
            ):
              subitemInfo = fileFormats[subitem]
              subdisplay = subitemInfo['display']
              text.append(f"      - {subdisplay}: 'fileFormats/{subitem}.md'\n")
        else:
          text.append(line)
      with open(MKDOCS_OUT, 'w') as f:
        f.write("".join(text))

    writeIndex()
    writeHelp()
    writeDataTypes()
    writeFileFormats()
    writeExtensions()
    writeConfig()

    return True

  if not readDocInfo():
    return False
  if not writeDocs():
    return False
  return True


def main():
  (task, msg, remaining) = readArgs()
  if not task:
    return
  elif task == 'make':
    makeDocs()
  elif task == 'docs':
    if makeDocs():
      serveDocs()
  elif task == 'g':
    if makeDocs():
      shipDocs()
      commit(task, msg)


main()
