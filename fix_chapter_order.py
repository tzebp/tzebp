from pathlib import Path
import json




def fix_chapters(file):
    text = file.read_text()
    output = []
    for line in text.split('\n'):
        if 'var chapters = ' in line:
            cpts = json.loads(line.strip().replace('var chapters = ', '').strip()[:-1].replace('start:', '"start":').replace('end:', '"end":'))
            
            out = json.dumps(sorted(cpts, key=lambda x:x['start'])).replace('"start":', 'start:').replace('"end":', 'end:')
            print(out)
            output.append('var chapters = ' + out)
        else:
            output.append(line.strip())
    file.write_text('\n'.join(output))

        



for file in Path('.').glob('*.html'):
    print(fix_chapters(file))


