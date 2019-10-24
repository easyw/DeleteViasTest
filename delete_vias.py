#!/usr/bin/env python
# error -> Segmentation fault (core dumped)
# Application: Pcbnew
# Version: 5.99.0-unknown-3fffd04~100~ubuntu18.04.1, release build
# Libraries:
#     wxWidgets 3.0.4
#     libcurl/7.58.0 OpenSSL/1.1.1 zlib/1.2.11 libidn2/2.0.4 libpsl/0.19.1 (+libidn2/2.0.4) nghttp2/1.30.0 librtmp/2.3
# Platform: Linux 4.15.0-51-generic x86_64, 64 bit, Little endian, wxGTK
# Build Info:
#     Build date: Oct 21 2019 11:53:42
#     wxWidgets: 3.0.4 (wchar_t,wx containers,compatible with 2.8) GTK+ 3.22
#     Boost: 1.65.1
#     OpenCASCADE Community Edition: 6.9.1
#     Curl: 7.58.0
#     Compiler: GCC 7.4.0 with C++ ABI 1011
# 
# Build settings:
#     KICAD_SCRIPTING=ON
#     KICAD_SCRIPTING_MODULES=ON
#     KICAD_SCRIPTING_PYTHON3=ON
#     KICAD_SCRIPTING_WXPYTHON=ON
#     KICAD_SCRIPTING_WXPYTHON_PHOENIX=ON
#     KICAD_SCRIPTING_ACTION_MENU=ON
#     BUILD_GITHUB_PLUGIN=ON
#     KICAD_USE_OCE=ON
#     KICAD_USE_OCC=OFF
#     KICAD_SPICE=ON

# Application: Pcbnew
# Version: (5.99.0-249-g3fffd042d), release build
# Libraries:
#     wxWidgets 3.0.4
#     libcurl/7.66.0 OpenSSL/1.1.1d (Schannel) zlib/1.2.11 brotli/1.0.7 libidn2/2.2.0 libpsl/0.21.0 (+libidn2/2.1.1) nghttp2/1.39.2
# Platform: Windows 8 (build 9200), 64-bit edition, 64 bit, Little endian, wxMSW
# Build Info:
#     Build date: Oct 20 2019 21:06:10
#     wxWidgets: 3.0.4 (wchar_t,wx containers,compatible with 2.8)
#     Boost: 1.71.0
#     OpenCASCADE Community Edition: 6.9.1
#     Curl: 7.66.0
#     Compiler: GCC 9.2.0 with C++ ABI 1013
# 
# Build settings:
#     KICAD_SCRIPTING=ON
#     KICAD_SCRIPTING_MODULES=ON
#     KICAD_SCRIPTING_PYTHON3=OFF
#     KICAD_SCRIPTING_WXPYTHON=ON
#     KICAD_SCRIPTING_WXPYTHON_PHOENIX=OFF
#     KICAD_SCRIPTING_ACTION_MENU=ON
#     BUILD_GITHUB_PLUGIN=ON
#     KICAD_USE_OCE=ON
#     KICAD_USE_OCC=OFF
#     KICAD_SPICE=ON

import sys
import os
from pcbnew import *
import wx
import pcbnew

# Python plugin stuff
class DeleteVias(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "DeleteVias Test Plugin"
        self.category = "Modify PCB"
        self.description = "DeleteVias Test Plugin"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'delete_vias.png')
        
    def Run(self):
        pcb = pcbnew.GetBoard() 
        tracks=pcb.GetTracks()
        for track in tracks:
            if track.Type() == pcbnew.PCB_VIA_T:
                pcb.RemoveNative(track)
        pcbnew.Refresh()
