#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-07-28 20:38:38
# @Author  : Weizhong Tu (mail@tuweizhong.com)
# @Link    : http://www.tuweizhong.com
 
'''
create some records for demo database
'''
 
from myword.wsgi import *
from learn.models import Column, Word
 
 
def main():

    c = Column.objects.get_or_create(name='六级', slug='liuji')[0]
    f=open('dic.txt','r')
    for line in f.readlines():
        line.strip()
        print line
        a,b=line.split('_')
        word = Word.objects.get_or_create(
                name='{}'.format(a),
                slug='{}'.format(a),
                content='词解： {}'.format(b)
            )[0]
        word.column.add(c)

 
 
if __name__ == '__main__':
    main()
    print("Done!")