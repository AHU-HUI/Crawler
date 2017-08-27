# encoding: utf-8
import codecs
import random
import os

def get_path(path):
    for home, dirs, files in os.walk(path):
        for filename in files:
            yield os.path.join(home, filename)

def output_html():
    fout = codecs.open('waterfall.js', 'w', encoding='utf-8')
    fout.write('''function waterfall(parent, sclass) {
    var oParent = document.getElementById(parent);
    var aBox = document.getElementsByClassName(sclass);
    var boxwidth = aBox[0].offsetWidth;
    var documentwidth = document.documentElement.clientWidth;
    var cnum = Math.floor(documentwidth/boxwidth);
    oParent.style.width = boxwidth * cnum + 'px';
    var aBoxHeight = new Array();
    for(var i = 0; i < aBox.length; i++) {
        if(i < cnum) {
            aBox[i].style.top = 0 + 'px';
            aBox[i].style.left = boxwidth * i + 'px';
            aBoxHeight.push(aBox[i].offsetHeight);
        }
        else {
            var minHeight = Math.min.apply(null, aBoxHeight);
            var minIndex = getIndex(aBoxHeight, minHeight);
            aBox[i].style.position = 'absolute';
            aBox[i].style.top = minHeight + 'px';
            aBox[i].style.left = aBox[minIndex].offsetLeft + 'px';
            aBoxHeight[minIndex] += aBox[i].offsetHeight;
        }
    }
}
function getIndex(arr, value) {
    for(var i in arr) {
        if(arr[i] == value) return i;
    }
}
window.onload = function() {
    waterfall('main', 'box');
}
function checkScrollside(sClass) {
    var aBox = document.getElementsByClassName(sClass);
    var lastImgIn = aBox[aBox.length-1].offsetTop + Math.floor(aBox[aBox.length-1].offsetHeight/2);
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var documentHeight = document.documentElement.clientHeight || document.body.clientHeight;
    return (lastImgIn < scrollTop + documentHeight);
}
window.onscroll = function() {
    if(checkScrollside('box')) {
        var oParent = document.getElementById('main');
            for(var i = 0; i < dataInit.data.length; i++) {
            var oBox = document.createElement('div');
            oBox.className = 'box';
            var oPic = document.createElement('div');
            oPic.className = 'pic';
            var oImg = document.createElement('img');
            oImg.src = dataInit.data[i].src;
            oPic.appendChild(oImg);
            oBox.appendChild(oPic);
            oParent.appendChild(oBox);
        }
        waterfall('main', 'box');
    }
}

window.onresize = function() {
    waterfall('main', 'box');
}

var dataInit = {
    'data':[
        {'src':'img/1.jpg'}
''')

    img_list = []
    for path_name in get_path("C:\\Users\\HUI\\Desktop\\hb_waterfall\\images"):
        path_name = path_name.replace('\\','\\\\')
        print(path_name)
        img_list.append(path_name)

    img_list = [path for path in img_list if (path.endswith('jpeg') or path.endswith('png') or path.endswith('gif'))]
    img_num = len(img_list)

    i = 0
    while (i < 50):
        num = random.randint(0,img_num)
        img_path = img_list[num]
        fout.write("        ,{'src':\'%s\'}\n" % img_path)
        i += 1

    fout.write('''    ]
};''')
    fout.close()


if __name__ == '__main__':
    output_html()
