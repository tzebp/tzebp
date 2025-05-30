from pathlib import Path

UPDATE = """
<meta property="og:title" content="Taurat Zabór Énjel Baso Plembang">
<meta property="og:description" content="Kitab Suci Taurat Zabór Énjél dalem baso Plembang">
<link rel="icon" type="image/x-icon" href="icons/favicon.ico">
"""

CHARSET = '<meta charset="utf-8" />\n'
PSA_MENU = 'Aktb-06-B'
PSA_BOOK = 'Aktb-04-B'
base_refs = set()

book_names = Path('./js/book-names.js')
books = book_names.read_text()
#if PSA_MENU in books:
#    books = books.replace(PSA_MENU, PSA_BOOK)
#    print('menu fixed')
#    book_names.write_text(books)

for file in Path('.').glob('*.html'):

    cons = file.read_text()
    if UPDATE in cons:
        continue
#    if PSA_MENU in cons:
#        cons = cons.replace(PSA_MENU, PSA_BOOK)
    cons = cons.replace(CHARSET, CHARSET + UPDATE)
    file.write_text(cons)
    print('Updated: ' + str(file))

print('\n'.join(base_refs))


