from pathlib import Path
import json,re
root=Path(__file__).resolve().parents[1]
s=(root/'DESIGN.md').read_text();t=json.loads(s.split('---',2)[1])
css=['/* Generado desde DESIGN.md con scripts/build-tokens.py. */',':root{']
for group in ['colors','spacing','rounded']:
 for key,value in t[group].items():css.append(f'  --{group}-{key}: {value};')
for key,scale in t['typography'].items():
 for prop,value in scale.items():css.append(f'  --type-{key}-{re.sub(r"([A-Z])",lambda m:"-"+m[1].lower(),prop)}: {value};')
css+=['  --red:var(--colors-primary); --hover:var(--colors-primary-hover); --pressed:var(--colors-primary-pressed);','  --black:var(--colors-text); --white:var(--colors-background); --gray:var(--colors-surface); --muted:var(--colors-muted); --line:var(--colors-line);',"  --display:var(--type-display-font-family),'Arial Narrow',Impact,sans-serif;", "  --text:var(--type-body-font-family),Avenir,'Segoe UI',Arial,sans-serif;",'  --mono:var(--type-label-font-family),monospace; --header:80px;','}']
(root/'tokens.css').write_text('\n'.join(css)+'\n')
