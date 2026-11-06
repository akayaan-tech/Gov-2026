import json, urllib.parse, re
photos=json.load(open('work/photos_b64.json'))
mp=json.load(open('work/map.json'))
lines=[]
for pid,b64 in photos.items():
    title=mp.get(pid,{}).get('title') or ''
    src='https://en.wikipedia.org/wiki/'+urllib.parse.quote(title.replace(' ','_')) if title else 'Wikimedia Commons'
    lines.append(f"  // {src}\n  '{pid}': 'data:image/jpeg;base64,{b64}',")
block="{\n"+"\n".join(lines)+"\n}"
tpl=open('work/template.html').read()
assert '/*PHOTOS*/{}' in tpl
open('index.html','w').write(tpl.replace('/*PHOTOS*/{}', block, 1))
print('built', len(open('index.html').read()), 'bytes')
