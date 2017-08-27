# encoding: utf-8
import codecs
import random
import os


def get_path(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)


def output_html():
    img_list = []
    for path_name in get_path("C:\\Users\\HUI\\Desktop\\hb_waterfall\\images"):
        img_list.append(path_name)

    img_list = [path for path in img_list if (path.endswith('jpeg') or path.endswith('png') or path.endswith('gif'))]
    img_num = len(img_list)

    fout = codecs.open('output.html', 'w', encoding='utf-8')
    fout.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>mmjpg_crawed</title>
    <link rel="stylesheet" href="style.css">
    <script src="waterfall.js"></script>
</head>
<body>
<div id="main">
''')
    i = 1
    while (i < 31):
        num = random.randint(0, img_num)
        img_path = img_list[num]
        fout.write('''    
        <div class="box">
            <div class="pic">
        ''')
        fout.write("        <img src=\"%s\">" % img_path)
        fout.write('''
            </div>
        </div>
        ''')
        i += 1

    fout.write('''
    </div>
    </body>
    </html>
    ''')
    fout.close()


if __name__ == '__main__':
    output_html()
