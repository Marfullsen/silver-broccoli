#!/usr/bin/env python
#-*- coding: utf-8 -*-

## You should have FFmpeg installed on your OS

import os, glob
listado = glob.glob("*.mpeg")
for audio in listado:
    os.system(f'FFmpeg -i "{audio}" -ss 00:00:04 "_{audio}"')
