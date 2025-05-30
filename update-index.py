from pathlib import Path

index = Path('./index.html')
tgt = """location.href = 'Aktb-03-FRT-2-001.html';"""
repl = """location.href = 'Aktb-05-JON-001.html';"""
text = index.read_text().replace(tgt, repl)

index.write_text(text)
