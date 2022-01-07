# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import django
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()
# Create your tests here.
from music.models import Artist,MusicRelease,RecordLabel


lables = 'lable'
artist = {'name':'artist','lable':'','music_release':''}
musicRelease = 'title 1'



def create_lable():
    d = RecordLabel(name=lables)
    d.save()
    return d

def create_musicRealese():
    d = MusicRelease(title=musicRelease)
    d.save()
    return d
def create_artists(lable,music):
    d = Artist(name="artist")
    d.label = lable
    d.save()
    d.music_releases.add(*music)
    d.save()
    return d

def populate():
    countLable = 0
    countRealese = 0
    lables = []
    realese = []
    while countLable<20:
        countLable+=1
        lableObj = create_lable()
        lables.append(lableObj)
        print("added lable with id:{id} name:{name}".format(id=lableObj.id,name=lableObj.name))
    while countRealese<100:
        countRealese+=1
        realeseObj = create_musicRealese()
        realese.append(realeseObj)
        print("added music realese with id:{id} name:{name}".format(id=realeseObj.id,name=realeseObj.title))

    while True:
        count = 0
        if len(lables) == 20 and len(realese) == 100:
            print("now creating artists")
            while count<20:
                p = create_artists(lables[count],realese)
                count+=1
                print("added artist realese with id:{id} name:{name}".format(id=p.id,name=p.name))
            break



        


if __name__ == '__main__':
    populate()

