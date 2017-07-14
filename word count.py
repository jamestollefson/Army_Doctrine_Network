# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:00:25 2017

@author: coach
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

adpdict = {'ADP 1':'adp1.txt', 'ADP 1-01':'adp1_01.txt', 'ADP 1-02':'adp1_02.txt', 'ADP 2-0':'adp2_0.txt', 'ADP 3-0':'adp3_0.txt', 'ADP 3-05':'adp3_05.txt', 'ADP 3-07':'adp3_07.txt', 'ADP 3-09':'adp3_09.txt', 'ADP 3-28':'adp3_28.txt', 'ADP 3-37':'adp3_37.txt', 'ADP 3-90':'adp3_90.txt', 'ADP 4-0':'adp4_0.txt', 'ADP 5-0':'adp5_0.txt', 'ADP 6-0':'adp6_0.txt', 'ADP 6-22':'adp6_22.txt', 'ADP 7-0':'adp7_0.txt'}
adrpdict = {'ADRP 1':'adrp1.txt', 'ADRP 1-02':'adrp1_02.txt', 'ADRP 1-03':'adrp1_03.txt', 'ADRP 2-0':'adrp2_0.txt', 'ADRP 3-0':'adrp3_0.txt', 'ADRP 4-0':'adrp4_0.txt', 'ADRP 3-05':'adrp3_05.txt', 'ADRP 3-07':'adrp3_07.txt', 'ADRP 3-09':'adrp3_09.txt', 'ADRP 3-28':'adrp3_28.txt', 'ADRP 3-37':'adrp3_37.txt', 'ADRP 3-90':'adrp3_90.txt', 'ADRP 4-0':'adrp4_0.txt', 'ADRP 5-0':'adrp5_0.txt', 'ADRP 6-0':'adrp6_0.txt', 'ADRP 6-22':'adrp6_22.txt', 'ADRP 7-0':'adrp7_0.txt'}
fmdict = {'FM 1-0':'fm1_0.txt', 'FM 1-04':'fm1_04.txt', 'FM 1-05':'fm1_05.txt', 'FM 1-06':'fm1_06.txt', 'FM 1-564':'fm1_564.txt', 'FM 2-0':'fm2_0.txt', 'FM 2-22.3':'fm2_22x3.txt', 'FM 3-01':'fm3_01.txt', 'FM 3-04':'fm3_04.txt', 'FM 3-04.120':'fm3_04x120.txt', 'FM 3-04.513':'fm3_04x513.txt', 'FM 3-05':'fm3_05.txt', 'FM 3-05.70':'fm3_05x70.txt', 'FM 3-06':'fm3_06.txt', 'FM 3-07':'fm3_07.txt', 'FM 3-09':'fm3_09.txt', 'FM 3-11':'fm3_11.txt', 'FM 3-11.9':'fm3_11x9.txt', 'FM 3-11.11':'fm3_11x11.txt', 'FM 3-12':'fm3_12.txt', 'FM 3-13':'fm3_13.txt', 'FM 3-14':'fm3_14.txt', 'FM 3-16':'fm3_16.txt', 'FM 3-18':'fm3_18.txt', 'FM 3-20.21':'fm3_20x21.txt', 'FM 3-21.10':'fm3_21x10.txt', 'FM 3-21.12':'fm3_21x12.txt', 'FM 3-21.20':'fm3_21x20.txt', 'FM 3-21.38':'fm3_21x38.txt', 'FM 3-21.91':'fm3_21x91.txt', 'FM 3-22':'fm3_22.txt', 'FM 3-22.3':'fm3_22x3.txt', 'FM 3-22.34':'fm3_22x34.txt', 'FM 3-22.65':'fm3_22x65.txt', 'FM 3-22.91':'fm3_22x91.txt', 'FM 3-23.35':'fm3_23x35.txt', 'FM 3-24':'fm3_24.txt', 'FM 3-24.2':'fm3_24x2.txt', 'FM 3-27':'fm3_27.txt', 'FM 3-34':'fm3_34.txt', 'FM 3-39':'fm3_39.txt', 'FM 3-50':'fm3_50.txt', 'FM 3-52':'fm3_52.txt', 'FM 3-53':'fm3_53.txt', 'FM 3-55':'fm3_55.txt', 'FM 3-55.93':'fm3_55x93.txt', 'FM 3-57':'fm3_57.txt', 'FM 3-61':'fm3_61.txt', 'FM 3-63':'fm3_63.txt', 'FM 3-81':'fm3_81.txt', 'FM 3-90-1':'fm3_90_1.txt', 'FM 3-90-2':'fm3_90_2.txt', 'FM 3-94':'fm3_94.txt', 'FM 3-96':'fm3_96.txt', 'FM 3-98':'fm3_98.txt', 'FM 3-99':'fm3_99.txt', 'FM 4-01':'fm4_01.txt', 'FM 4-02':'fm4_02.txt', 'FM 4-30':'fm4_30.txt', 'FM 4-40':'fm4_40.txt', 'FM 4-95':'fm4_95.txt', 'FM 6-0':'fm6_0.txt', 'FM 6-02':'fm6_02.txt', 'FM 6-02.71':'fm6_02x71.txt', 'FM 6-05':'fm6_05.txt', 'FM 6-22':'fm6_22.txt', 'FM 6-99':'fm6_99.txt', 'FM 7-0':'fm7_0.txt', 'FM 7-22':'fm7_22.txt', 'FM 7-100.1':'fm7_100x1.txt', 'FM 21-60':'fm21_60.txt', 'FM 27-10':'fm27_10.txt', 'FM 90-3':'fm90_3.txt', 'FM 90-5':'fm90_5.txt'}
atpdict = {'ATP 1-0.1':'atp1_0x1.txt', 'ATP 1-0.2':'atp1_0x2.txt', 'ATP 1-02.1':'atp1_02x1.txt', 'ATP 1-05.01':'atp1_05x01.txt', 'ATP 1-05.02':'atp1_05x02.txt', 'ATP 1-05.03':'atp1_05x03.txt', 'ATP 1-05.04':'atp1_05x04.txt', 'ATP 1-06.1':'atp1_06x1.txt', 'ATP 1-06.2':'atp1_06x2.txt', 'ATP 1-06.3':'atp1_06x3.txt', 'ATP 1-06.4':'atp1_06x4.txt', 'ATP 1-19':'atp1_19.txt', 'ATP 1-20':'atp1_20.txt', 'ATP 2-01':'atp2_01.txt', 'ATP 2-01.3':'atp2_01x3.txt', 'ATP 2-19.3':'atp2_19x3.txt', 'ATP 2-19.4':'atp2_19x4.txt', 'ATP 2-22.2-1':'atp2_22x2_1.txt', 'ATP 2-22.4':'atp2_22x4.txt', 'ATP 2-22.7':'atp2_22x7.txt', 'ATP 2-22.9':'atp2_22x9.txt', 'ATP 2-22.82':'atp2_22x82.txt', 'ATP 2-22.85':'atp2_22x85.txt', 'ATP 2-33.4':'atp2_33x4.txt', 'ATP 2-91.7':'atp2_91x7.txt', 'ATP 2-91.8':'atp2_91x8.txt', 'ATP 3-01.4':'atp3_01x4.txt', 'ATP 3-01.7':'atp3_01x7.txt', 'ATP 3-01.8':'atp3_01x8.txt', 'ATP 3-01.15':'atp3_01x15.txt', 'ATP 3-01.16':'atp3_01x16.txt', 'ATP 3-01.18':'atp3_01x18.txt', 'ATP 3-01.48':'atp3_01x48.txt', 'ATP 3-01.50':'atp3_01x50.txt', 'ATP 3-01.60':'atp3_01x60.txt', 'ATP 3-01.64':'atp3_01x64.txt', 'ATP 3-01.81':'atp3_01x81.txt', 'ATP 3-01.85':'atp3_01x85.txt', 'ATP 3-01.87':'atp3_01x87.txt', 'ATP 3-01.91':'atp3_01x91.txt', 'ATP 3-01.94':'atp3_01x94.txt', 'ATP 3-04.1':'atp3_04x1.txt', 'ATP 3-04.18':'atp3_04x18.txt', 'ATP 3-04.64':'atp3_04x64.txt', 'ATP 3-04.94':'atp3_04x94.txt', 'ATP 3-05.1':'atp3_05x1.txt', 'ATP 3-05.2':'atp3_05x2.txt', 'ATP 3-05.11':'atp3_05x11.txt', 'ATP 3-05.20':'atp3_05x20.txt', 'ATP 3-05.40':'atp3_05x40.txt', 'ATP 3-05.60':'atp3_05x60.txt', 'ATP 3-05.68':'atp3_05x68.txt', 'ATP 3-06.1':'atp3_06x1.txt', 'ATP 3-06.20':'atp3_06x20.txt', 'ATP 3-07.5':'atp3_07x5.txt', 'ATP 3-07.6':'atp3_07x6.txt', 'ATP 3-07.10':'atp3_07x10.txt', 'ATP 3-07.31':'atp3_07x31.txt', 'ATP 3-09.02':'atp3_09x02.txt', 'ATP 3-09.12':'atp3_09x12.txt', 'ATP 3-09.13':'atp3_09x13.txt', 'ATP 3-09.23':'atp3_09x23.txt', 'ATP 3-09.24':'atp3_09x24.txt', 'ATP 3-09.30':'atp3_09x30.txt', 'ATP 3-09.32':'atp3_09x32.txt', 'ATP 3-09.34':'atp3_09x34.txt', 'ATP 3-09.42':'atp3_09x42.txt', 'ATP 3-09.50':'atp3_09x50.txt', 'ATP 3-09.60':'atp3_09x60.txt', 'ATP 3-09.70':'atp3_09x70.txt', 'ATP 3-11.23':'atp3_11x23.txt', 'ATP 3-11.24':'atp3_11x24.txt', 'ATP 3-11.32':'atp3_11x32.txt', 'ATP 3-11.36':'atp3_11x36.txt', 'ATP 3-11.37':'atp3_11x37.txt', 'ATP 3-11.41':'atp3_11x41.txt', 'ATP 3-11.46':'atp3_11x46.txt', 'ATP 3-11.47':'atp3_11x47.txt', 'ATP 3-11.50':'atp3_11x50.txt', 'ATP 3-13.10':'atp3_13x10.txt', 'ATP 3-14.5':'atp3_14x5.txt', 'ATP 3-17.2':'atp3_17x2.txt', 'ATP 3-18.4':'atp3_18x4.txt', 'ATP 3-18.10':'atp3_18x10.txt', 'ATP 3-18.11':'atp3_18x11.txt', 'ATP 3-18.12':'atp3_18x12.txt', 'ATP 3-18.13':'atp3_18x13.txt', 'ATP 3-18.14':'atp3_18x14.txt', 'ATP 3-20.15':'atp3_20x15.txt', 'ATP 3-20.16':'atp3_20x16.txt', 'ATP 3-20.96':'atp3_20x96.txt', 'ATP 3-20.97':'atp3_20x97.txt', 'ATP 3-20.98':'atp3_20x98.txt', 'ATP 3-21.8':'atp3_21x8.txt', 'ATP 3-21.11':'atp3_21x11.txt', 'ATP 3-21.18':'atp3_21x18.txt', 'ATP 3-21.21':'atp3_21x21.txt', 'ATP 3-22.40':'atp3_22x40.txt', 'ATP 3-27.3':'atp3_27x3.txt', 'ATP 3-27.5':'atp3_27x5.txt', 'ATP 3-28.1':'atp3_28x1.txt', 'ATP 3-34.5':'atp3_34x5.txt', 'ATP 3-34.20':'atp3_34x20.txt', 'ATP 3-34.22':'atp3_34x22.txt', 'ATP 3-34.23':'atp3_34x23.txt', 'ATP 3-34.40':'atp3_34x40.txt', 'ATP 3-34.80':'atp3_34x80.txt', 'ATP 3-34.81':'atp3_34x81.txt', 'ATP 3-34.84':'atp3_34x84.txt', 'ATP 3-35':'atp3_35.txt', 'ATP 3-35.1':'atp3_35x1.txt', 'ATP 3-36':'atp3_36.txt', 'ATP 3-37.2':'atp3_37x2.txt', 'ATP 3-37.10':'atp3_37x10.txt', 'ATP 3-37.34':'atp3_37x34.txt', 'ATP 3-39.10':'atp3_39x10.txt', 'ATP 3-39.12':'atp3_39x12.txt', 'ATP 3-39.20':'atp3_39x20.txt', 'ATP 3-39.30':'atp3_39x30.txt', 'ATP 3-39.32':'atp3_39x32.txt', 'ATP 3-39.33':'atp3_39x33.txt', 'ATP 3-39.34':'atp3_39x34.txt', 'ATP 3-50.3':'atp3_50x3.txt', 'ATP 3-52.1':'atp3_52x1.txt', 'ATP 3-52.2':'atp3_52x2.txt', 'ATP 3-52.3':'atp3_52x3.txt', 'ATP 3-53.1':'atp3_53x1.txt', 'ATP 3-53.2':'atp3_53x2.txt', 'ATP 3-55.3':'atp3_55x3.txt', 'ATP 3-55.4':'atp3_55x4.txt', 'ATP 3-55.6':'atp3_55x6.txt', 'ATP 3-57.10':'atp3_57x10.txt', 'ATP 3-57.20':'atp3_57x20.txt', 'ATP 3-57.30':'atp3_57x30.txt', 'ATP 3-57.50':'atp3_57x50.txt', 'ATP 3-57.60':'atp3_57x60.txt', 'ATP 3-57.70':'atp3_57x70.txt', 'ATP 3-57.80':'atp3_57x80.txt', 'ATP 3-60':'atp3_60.txt', 'ATP 3-60.1':'atp3_60x1.txt', 'ATP 3-60.2':'atp3_60x2.txt', 'ATP 3-76':'atp3_76.txt', 'ATP 3-90.1':'atp3_90x1.txt', 'ATP 3-90.4':'atp3_90x4.txt', 'ATP 3-90.5':'atp3_90x5.txt', 'ATP 3-90.8':'atp3_90x8.txt', 'ATP 3-90.15':'atp3_90x15.txt', 'ATP 3-90.37':'atp3_90x37.txt', 'ATP 3-90.61':'atp3_90x61.txt', 'ATP 3-90.90':'atp3_90x90.txt', 'ATP 3-90.97':'atp3_90x97.txt', 'ATP 3-91':'atp3_91.txt', 'ATP 3-91.1':'atp3_91x1.txt', 'ATP 3-92':'atp3_92.txt', 'ATP 3-90.1':'atp3_90x1.txt', 'ATP 3-93':'atp3_93.txt', 'ATP 3-94.2':'atp3_94x2.txt', 'ATP 4-0.1':'atp4_0x1.txt', 'ATP 4-0.6':'atp4_0x6.txt', 'ATP 4-01.45':'atp4_01x45.txt', 'ATP 4-02.1':'atp4_02x1.txt', 'ATP 4-02.2':'atp4_02x2.txt', 'ATP 4-02.3':'atp4_02x3.txt', 'ATP 4-02.5':'atp4_02x5.txt', 'ATP 4-02.7':'atp4_02x7.txt', 'ATP 4-02.8':'atp4_02x8.txt', 'ATP 4-02.42':'atp4_02x42.txt', 'ATP 4-02.43':'atp4_02x43.txt', 'ATP 4-02.46':'atp4_02x46.txt', 'ATP 4-02.55':'atp4_02x55.txt', 'ATP 4-02.82':'atp4_02x82.txt', 'ATP 4-02.83':'atp4_02x83.txt', 'ATP 4-02.84':'atp4_02x84.txt', 'ATP 4-02.85':'atp4_02x85.txt', 'ATP 4-10':'atp4_10.txt', 'ATP 4-10.1':'atp4_10x1.txt', 'ATP 4-11':'atp4_11.txt', 'ATP 4-12':'atp4_12.txt', 'ATP 4-13':'atp4_13.txt', 'ATP 4-14':'atp4_14.txt', 'ATP 4-15':'atp4_15.txt', 'ATP 4-16':'atp4_16.txt', 'ATP 4-25.12':'atp4_25x12.txt', 'ATP 4-25.13':'atp4_25x13.txt', 'ATP 4-31':'atp4_31.txt', 'ATP 4-32':'atp4_32.txt', 'ATP 4-32.1':'atp4_32x1.txt', 'ATP 4-32.2':'atp4_32x2.txt', 'ATP 4-32.3':'atp4_32x3.txt', 'ATP 4-32.16':'atp4_32x16.txt', 'ATP 4-33':'atp4_33.txt', 'ATP 4-35':'atp4_35.txt', 'ATP 4-35.1':'atp4_35x1.txt', 'ATP 4-41':'atp4_41.txt', 'ATP 4-42':'atp4_42.txt', 'ATP 4-42.2':'atp4_42x2.txt', 'ATP 4-43':'atp4_43.txt', 'ATP 4-44':'atp4_44.txt', 'ATP 4-45':'atp4_45.txt', 'ATP 4-46':'atp4_46.txt', 'ATP 4-48':'atp4_48.txt', 'ATP 4-70':'atp4_70.txt', 'ATP 4-90':'atp4_90.txt', 'ATP 4-91':'atp4_91.txt', 'ATP 4-92':'atp4_92.txt', 'ATP 4-93':'atp4_93.txt', 'ATP 4-94':'atp4_94.txt', 'ATP 5-0.1':'atp5_0x1.txt', 'ATP 5-0.3':'atp5_0x3.txt', 'ATP 5-19':'atp5_19.txt', 'ATP 6-0.5':'atp6_0x5.txt', 'ATP 6-01.1':'atp6_01x1.txt', 'ATP 6-02.40':'atp6_02x40.txt', 'ATP 6-02.53':'atp6_02x53.txt', 'ATP 6-02.60':'atp6_02x60.txt', 'ATP 6-02.70':'atp6_02x70.txt', 'ATP 6-02.72':'atp6_02x72.txt', 'ATP 6-02.73':'atp6_02x73.txt', 'ATP 6-02.75':'atp6_02x75.txt', 'ATP 6-02.90':'atp6_02x90.txt', 'ATP 6-22.1':'atp6_22x1.txt', 'ATP 6-22.5':'atp6_22x5.txt', 'ATP 6-22.6':'atp6_22x6.txt'}
attpdict = {'ATTP 3-06.11':'attp3_06x11.txt', 'ATTP 3-21.50':'attp3_21x50.txt', 'ATTP 3-21.90':'attp3_21x90.txt'}

adpdict.update(adrpdict)
adpdict.update(fmdict)
adpdict.update(atpdict)
adpdict.update(attpdict)

doctrine_dict = adpdict

wordcount = 0

for title, filename in doctrine_dict.items():
    f = open(filename, 'r')
    f = f.read()
    words = f.split()
    for word in words:
        wordcount = wordcount + 1
print(wordcount)
average_length = wordcount / 331
print(average_length)
days_per_new_pub = 6.4

#the following function only accounts for the wordcount averaged over the 331 unclassified publications that
#were readily available for my analysis. Obviously the addition of the 43 unavailable documents would change the 
#answer substantially. However this algorithm is useful for making my point - to wit, it would take a very long time
#to actually read all of the Army's doctrine (to say nothing of SOPs, AR, DA Pams, command memos, mission order, training guidance
#and other necessary reading).

def time_to_read_it_all(days_per_new_pub, hours_per_day, wordcount, words_per_minute):
    """Describes the time it would take to read a given body of publications given that new publications are
    constantly being published"""
    number_of_Army_doctrinal_pubs = 331
    average_length = wordcount / number_of_Army_doctrinal_pubs
    days = 0
    time = np.round(wordcount / words_per_minute / 60 / hours_per_day, decimals=0)
    days = days + time
    new_material = np.round((time / days_per_new_pub), decimals=0)
    print('Read it all in {} days, but now there are {} new publications to go!'.format(time, new_material))
    while new_material > 0:
        wordcount = new_material * average_length
        time = np.round(wordcount / words_per_minute / 60 / hours_per_day, decimals=0)
        days = days + time
        new_material = np.round((time / days_per_new_pub), decimals=0)
        print('Read it all in {} days, but now there are {} new publications to go!'.format(time, new_material))
    print("In all it will take {} days, or {} years, to read all of the Army's doctrine and actually be current.".format(days, np.round(days / 312, decimals=1)))

time_to_read_it_all(days_per_new_pub, 1.5, wordcount, 250)

#It appears that an hours_per_day value much less than 1.05 causes the reader to NEVER catch up   