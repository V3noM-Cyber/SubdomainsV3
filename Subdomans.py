 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#code by v3nom

import os
import sys
import time
from colorama import Fore, Back, Style
import re
import requests
import argparse

version = 1.2



def parse_args():
        
        parser = argparse.ArgumentParser()
        parser.add_argument('--domain', '--domain', type=str, required=True, help="Target domain.")
        parser.add_argument('-o', '--output', type=str, help="Output file.")
        return parser.parse_args()

def banner():
        global version
        b =Fore.GREEN+"""
                    .:.        .:,
                   xM;           XK.
                  dx'            .lO.
                 do                ,0.
             .c.lN'      ,  '.     .k0.:'
              xMMk;d;''cOM0kWXl,',locMMX.
              .NMK.   :WMMMMMMMx    dMMc
               lMMO  lWMMMMMMMMMO. lMMO
                cWMxxMMMMMMMMMMMMKlWMk
                 .xWMMMMMMMMMMMMMMM0,
                   .,OMd,,,;0MMMO,.
             .l0O.VXVXOX.VXVX0MOVXVX.0Kd,
            lWMMO0VXVX0OX.VXVXlVXVX.VXNMMO
           .MMX;.N0VXVX00X.VXVXVX0.0M:.OMMl
          .OXc  ,MMOVXVX0VX .VXVX00MMo  ,0X'
          0x.  :XMMMkVXVX.XO.VXVXdMMMWo.  :X'
         .d  'NMMMMMMkVXVX..VXVX0.XMMMMWl  ;c
            'NNoMMMMMMxVXVXVXVXVX0.XMMk0Mc
           .NMx OMMMMMMdVXVXVXlVXVX.NW.;MMc
          :NMMd .NMMMMMMdVXVXdMd,,,,oc ;MMWx
          .0MN,  'XMMMMMMoVXoMMMMMMWl   0MW,
           .0.    .xWMMMMM:lMMMMMM0,     kc
            ,O.     .:dOKXXXNKOxc.      do
             '0c        -V3n0m-       ,Ol
               ;.                     :.
# Coded By V3nom Cyber    -@V3nom 
  """.format(v=version)
        print(b)
        os.system("hostname")
        os.system("date")
        print("============================================")
        
def clear_url(target):
        return re.sub('.*www\.','',target,1).split('/')[0].strip()

def save_subdomains(subdomain,output_file):
        with open(output_file,"a") as f:
                f.write(subdomain + '\n')
                f.close()
os.system("xdg-open https://t.me/V3noM_Cyber")
def main():
        banner()
        args =parse_args()

        subdomains = []
        target = clear_url(args.domain)
        output = args.output

        req = requests.get("\040\150\164\164\160\163\072\057\057\143\162\164\056\163\150\057\077\161\075\045\056\173\144\157\155\141\151\156\175\046\157\165\164\160\165\164\075\152\163\157\156".format(domain=target))

        if req.status_code != 200:
                print("[X] Information not available!")
                exit(1)

        for (key,value) in enumerate(req.json()):
                subdomains.append(value['name_value'])


        print(Fore.YELLOW+"\n[-] ---- TARGET: {domain} ---- [-] \n".format(domain=target))

        subdomains = sorted(set(subdomains))

        for subdomain in subdomains:
                print(Fore.WHITE+"[-]  {s} :".format(s=subdomain))
                if output is not None:
                        save_subdomains(subdomain,output)

        print("\n\n[!]  Your work is successful ")


main()