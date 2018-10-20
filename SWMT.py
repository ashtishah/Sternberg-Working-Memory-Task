""" SWMT: Execute this file to run the Sternberg 
    Working Memory Task.
    
    Authors:
        Ashti M. Shah
        Hannah Grotzinger
        """

from __future__ import absolute_import, division, print_function
from psychopy import core, data, event, gui, logging, visual
import matplotlib.pyplot as plt
import matplotlib # Only needed to determine Matplotlib version number
import numpy as np
import os
import sys
import pandas as pd
import csv

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

print (_thisDir)

# Store info about the experiment session
expName = 'SWMT'
expInfo = {'participant' : '',
            'K Code' : '',
            'run' : ['Scanner', 'Practice', 'Backup']}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

if expInfo['run'] == 'Scanner':
    expRun = {'Which run?' : ['1', '2']}
    dlg2 = gui.DlgFromDict(dictionary=expRun, title='Run1or2')
    if not dlg2.OK:
        core.quit()  # User pressed cancel
elif expInfo['run'] == 'Backup':
    expBlock = {'Block?' : ['2', '4']}
    dlg3 = gui.DlgFromDict(dictionary=expBlock, title='Block')
    if not dlg3.OK:
        core.quit()  # User pressed cancel

if not dlg.OK:
    core.quit()  # User pressed cancel
expInfo['date'] = data.getDateStr()  # Add a simple timestamp
expInfo['expName'] = expName
kCode = expInfo['K Code']
expInfo['participant'] = str(expInfo['participant'])

from SWMTTools import *

k=0
# Set Up K Value
if kCode == 'AGH':
    k = 3 
if kCode == 'IHJ':
    k = 4
if kCode == 'OST':
    k = 5
if kCode == 'NBU':
    k = 6
if kCode == 'DQL':
    k = 7
"""
# Create filename
if expInfo['run'] == 'Scanner':
    filename = os.path.join(_thisDir, 'tfMRI_output',
        '%s_%s_%s_%s' % (expInfo['participant'], expInfo['expName'],
                        expRun['Which run?'], expInfo['date']))
elif expInfo['run'] == 'Practice':
    filename = os.path.join('/Users', 'gablab', 'Desktop', 'Practice',
        '%s_%s_%s' % (expInfo['participant'], expInfo['expName'],
                        expInfo['date']))
else:
    filename = os.path.join(_thisDir, 'tfMRI_output', 'backup',
        '%s_%s_%s_%s' % (expInfo['participant'], expInfo['expName'],
                        expBlock['Block?'], expInfo['date']))

# Save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # This outputs to the screen
"""

filename = (expInfo['participant'], expInfo['expName'],
                        expRun['Which run?'], expInfo['date'])
# Stimuli specific to each trial and run type
if expInfo['run'] != 'Practice':
    # These are the same for each k value
    jitteredTimes1 = [9, 11, 11, 9, 9, 10, 9, 11, 10, 10, 10, 5]
    jitteredTimes2 = [10, 10, 11, 10, 9, 11, 10, 9, 11, 11, 5]
    jitteredTimes3 = [10, 9, 9, 10, 11, 11, 10, 11, 10, 10, 5]
    jitteredTimes4 = [9, 11, 10, 10, 10, 11, 9, 10, 11, 11, 5]
    if k==3:
        encodeLetters1 = [['R', 'F', 'B', 'Q'], ['J', 'M'], ['Q', 'B', 'G'],
            ['X', 'G', 'J'], ['G', 'B', 'H', 'Q'], ['S', 'R', 'M'], ['L', 'M'],
            ['Q', 'L', 'F'], ['R', 'B'], ['W', 'X', 'Q'], ['N', 'F'], ['N', 'R']]
        encodeLetters2 = [['H', 'N', 'M'], ['M', 'L', 'G', 'W'],
            ['X', 'F', 'H', 'M'], ['F', 'N', 'B', 'Q'], ['L', 'B', 'G', 'H'],
            ['H', 'J', 'F'], ['R', 'L'], ['G', 'N'], ['F', 'H', 'G', 'M'],
            ['R', 'H'], ['G', 'J', 'F', 'B']]
        encodeLetters3 = [['F', 'W', 'J', 'S'], ['R', 'Q'],
            ['Q', 'B', 'N', 'M'], ['R', 'X', 'B', 'F'], ['L', 'F'],
            ['G', 'R', 'J', 'N'], ['X', 'R'], ['G', 'H', 'W'], ['H', 'F', 'M'],
            ['S', 'L', 'J'], ['H', 'B', 'J']]
        encodeLetters4 = [['W', 'N', 'S', 'G'], ['M', 'G', 'J'], ['G', 'L'],
            ['N', 'M', 'S', 'J'], ['H', 'B', 'Q'], ['F', 'X', 'B'], ['M', 'N'],
            ['L', 'F'], ['Q', 'N', 'M'], ['W', 'J'], ['X', 'S', 'J', 'H']]
        retrievalLetters1 = [['B'], ['G'], ['G'], ['H'], ['G'], ['M'], ['M'],
            ['Q'], ['R'], ['F'], ['N'], ['H'],]
        retrievalLetters2 = [['N'], ['W'], ['Q'], ['S'], ['B'], ['H'], ['F'],
            ['G'], ['Q'], ['H'], ['L']]
        retrievalLetters3 = [['F'], ['M'], ['N'], ['Q'], ['L'], ['N'], ['R'],
            ['S'], ['W'], ['J'], ['F']]
        retrievalLetters4 = [['B'], ['H'], ['G'], ['J'], ['B'], ['L'], ['S'],
            ['L'], ['G'], ['J'], ['J']]
    if k == 4:
        encodeLetters1 = [['L', 'F'], ['L', 'B', 'G', 'H'], ['N', 'F'],
            ['N', 'R'], ['F', 'H', 'G', 'M'], ['F', 'B', 'N', 'H', 'G'],
            ['X', 'H', 'L', 'N', 'R'], ['R', 'F', 'B', 'Q'], ['X', 'R'],
            ['M', 'N'], ['F', 'W', 'J', 'S'], ['W', 'B', 'M', 'G', 'N']]
        encodeLetters2 = [['L', 'R', 'F', 'J', 'N'], ['R', 'L', 'H', 'N', 'Q'],
            ['N', 'M', 'S', 'F', 'G'], ['R', 'H'], ['R', 'B'],
            ['W', 'N', 'S', 'G'], ['G', 'J', 'F', 'B'],
            ['J', 'N', 'Q', 'B', 'F'], ['W', 'J'], ['J', 'Q', 'H', 'X', 'B'],
            ['N', 'M', 'S', 'J']]
        encodeLetters3 = [['Q', 'B', 'N', 'M'], ['G', 'R', 'J', 'N'],
            ['H', 'L', 'M', 'R', 'S'], ['R', 'L'], ['L', 'F', 'X', 'W', 'B'],
            ['J', 'M'], ['Q', 'W', 'J', 'R', 'B'], ['L', 'M'],
            ['G', 'B', 'H', 'Q'], ['M', 'S', 'W', 'X', 'J'], ['R', 'Q']]
        encodeLetters4 = [['L', 'F'], ['G', 'N'], ['X', 'F', 'H', 'M'],
            ['M', 'L', 'G', 'W'], ['R', 'X', 'B', 'F'],
            ['L', 'X', 'J', 'W', 'S'], ['G', 'L'], ['F', 'N', 'B', 'Q'],
            ['N', 'R', 'Q', 'L', 'J'], ['X', 'S', 'J', 'H'],
            ['L', 'F', 'H', 'S', 'N']]
        retrievalLetters1 = [['F'], ['G'], ['F'], ['J'], ['G'], ['X'], ['H'],
            ['Q'], ['X'], ['G'], ['J'], ['M']]
        retrievalLetters2 = [['J'], ['M'], ['M'], ['H'], ['R'], ['X'], ['J'],
            ['R'], ['J'], ['Q'], ['N']]
        retrievalLetters3 = [['M'], ['N'], ['X'], ['L'], ['W'], ['M'], ['R'],
            ['N'], ['G'], ['S'], ['F']]
        retrievalLetters4 = [['L'], ['Q'], ['W'], ['W'], ['M'], ['J'], ['L'],
            ['F'], ['H'], ['B'], ['L']]
    if k == 5:
        encodeLetters1 = [['X', 'R'], ['N', 'M', 'S', 'F', 'G'],
            ['N', 'Q', 'G', 'F', 'L', 'J'], ['X', 'H', 'L', 'N', 'R'],
            ['N', 'W', 'X', 'G', 'R', 'B'], ['F', 'N', 'Q', 'L', 'G', 'S'],
            ['G', 'N'], ['R', 'L', 'H', 'N', 'Q'], ['J', 'M'],
            ['X', 'W', 'F', 'H', 'J', 'G'], ['G', 'L'],
            ['Q', 'H', 'J', 'G', 'W', 'F']]
        encodeLetters2 = [['L', 'M'], ['R', 'B'], ['N', 'R', 'Q', 'L', 'J'],
            ['L', 'F'], ['H', 'L', 'M', 'R', 'S'],
            ['X', 'M', 'L', 'F', 'N', 'R'], ['M', 'N'],
            ['L', 'R', 'F', 'J', 'N'], ['L', 'X', 'J', 'W', 'S'],
            ['G', 'J', 'H', 'M', 'W', 'X'], ['W', 'G', 'L', 'M', 'B', 'F']]
        encodeLetters3 = [['M', 'S', 'W', 'X', 'J'], ['L', 'F', 'X', 'W', 'B'],
            ['W', 'J', 'X', 'B', 'Q', 'M'], ['W', 'J'],
            ['R', 'X', 'B', 'G', 'L', 'Q'], ['H', 'W', 'R', 'N', 'Q', 'M'],
            ['R', 'Q'], ['L', 'F'], ['J', 'Q', 'H', 'X', 'B'], ['N', 'F'],
            ['W', 'B', 'M', 'G', 'N']]
        encodeLetters4 = [['N', 'R'], ['F', 'B', 'N', 'H', 'G'],
            ['J', 'M', 'G', 'R', 'L', 'X'], ['R', 'H'],
            ['B', 'H', 'X', 'N', 'J', 'W'], ['W', 'Q', 'N', 'S', 'L', 'M'],
            ['R', 'L'], ['L', 'F', 'H', 'S', 'N'],
            ['X', 'M', 'B', 'L', 'F', 'S'], ['Q', 'W', 'J', 'R', 'B'],
            ['J', 'N', 'Q', 'B', 'F']]
        retrievalLetters1 = [['X'], ['S'], ['G'], ['M'], ['N'], ['F'], ['Q'],
            ['Q'], ['B'], ['B'], ['G'], ['B']]
        retrievalLetters2 = [['M'], ['B'], ['J'], ['L'], ['H'], ['M'], ['N'],
            ['B'], ['S'], ['W'], ['W']]
        retrievalLetters3 = [['W'], ['X'], ['R'], ['J'], ['S'], ['S'], ['Q'],
            ['L'], ['N'], ['N'], ['H']]
        retrievalLetters4 = [['F'], ['G'], ['B'], ['R'], ['R'], ['R'], ['B'],
            ['H'], ['F'], ['R'],['W']]
    if k == 6:
        encodeLetters1 = [['W', 'J'], ['J', 'N', 'G', 'X', 'L', 'Q', 'F'],
            ['N', 'W', 'X', 'G', 'R', 'B'], ['N', 'R'],
            ['S', 'N', 'Q', 'F', 'J', 'X', 'W'], ['B', 'H', 'X', 'N', 'J', 'W'],
            ['R', 'H'], ['G', 'J', 'H', 'M', 'W', 'X'], ['G', 'L'],
            ['R', 'X', 'B', 'G', 'L', 'Q'], ['F', 'W', 'G', 'S', 'X', 'H', 'R'],
            ['G', 'N', 'S', 'L', 'M', 'F', 'J']]
        encodeLetters2 = [['G', 'N'], ['R', 'Q'],
            ['Q', 'W', 'H', 'L', 'N', 'R', 'G'],
            ['J', 'Q', 'F', 'W', 'B', 'H', 'M'], ['X', 'M', 'L', 'F', 'N', 'R'],
            ['N', 'Q', 'G', 'F', 'L', 'J'], ['Q', 'G', 'S', 'N', 'J', 'R', 'M'],
            ['L', 'F'], ['X', 'W', 'J', 'B', 'H', 'S', 'L'],
            ['X', 'M', 'B', 'L', 'F', 'S'], ['R', 'L']]
        encodeLetters3 = [['L', 'G', 'S', 'X', 'J', 'N', 'W'],
            ['X', 'W', 'F', 'H', 'J', 'G'], ['Q', 'H', 'J', 'G', 'W', 'F'],
            ['J', 'M', 'G', 'R', 'L', 'X'], ['L', 'M'],
            ['W', 'J', 'X', 'B', 'Q', 'M'], ['J', 'L', 'B', 'X', 'S', 'G', 'R'],
            ['X', 'R'], ['M', 'N'], ['J', 'B', 'W', 'X', 'F', 'N', 'L'],
            ['M', 'X', 'H', 'W', 'B', 'L', 'G']]
        encodeLetters4 = [['W', 'Q', 'N', 'S', 'L', 'M'],
            ['G', 'M', 'N', 'Q', 'S', 'H', 'L'],
            ['B', 'S', 'J', 'M', 'L', 'H', 'R'], ['F', 'N', 'Q', 'L', 'G', 'S'],
            ['L', 'F'], ['R', 'B'], ['N', 'F'], ['J', 'M'],
            ['H', 'W', 'R', 'N', 'Q', 'M'], ['G', 'X', 'N', 'L', 'Q', 'J', 'M'],
            ['W', 'G', 'L', 'M', 'B', 'F']]
        retrievalLetters1 = [['W'], ['J'], ['N'], ['G'], ['J'], ['N'], ['N'],
            ['H'], ['L'], ['X'], ['L'], ['J']]
        retrievalLetters2 = [['G'], ['R'], ['H'], ['W'], ['R'], ['G'], ['G'],
            ['W'], ['L'], ['X'], ['J']]
        retrievalLetters3 = [['G'], ['B'], ['W'], ['G'], ['M'], ['F'], ['X'],
            ['B'], ['F'], ['J'], ['N']]
        retrievalLetters4 = [['H'], ['M'], ['X'], ['S'], ['L'], ['B'], ['F'],
            ['B'], ['W'], ['X'], ['B']]
    if k == 7:
        encodeLetters1 = [['G', 'L'], ['L', 'M'],
            ['J', 'B', 'W', 'X', 'F', 'N', 'L'],
            ['B', 'S', 'J', 'M', 'L', 'H', 'R'],
            ['M', 'X', 'H', 'W', 'B', 'L', 'G'],
            ['S', 'B', 'F', 'G', 'X', 'N', 'H', 'L'], ['N', 'R'],
            ['S', 'N', 'F', 'L', 'H', 'M', 'W', 'Q'], ['W', 'J'],
            ['L', 'R', 'M', 'J', 'N', 'B', 'S', 'W'],
            ['Q', 'G', 'S', 'N', 'J', 'R', 'M'],
            ['H', 'R', 'S', 'X', 'F', 'N', 'Q', 'W']]
        encodeLetters2 = [['W', 'B', 'J', 'R', 'X', 'M', 'F', 'N'], ['R', 'L'],
            ['G', 'M', 'N', 'Q', 'S', 'H', 'L'],
            ['F', 'W', 'B', 'R', 'G', 'N', 'J', 'M'],
            ['J', 'L', 'B', 'X', 'S', 'G', 'R'], ['R', 'Q'], ['N', 'F'],
            ['J', 'Q', 'F', 'W', 'B', 'H', 'M'],
            ['N', 'G', 'F', 'X', 'S', 'L', 'M', 'H'], ['L', 'F'],
            ['F', 'W', 'G', 'S', 'X', 'H', 'R']]
        encodeLetters3 = [['J', 'M'], ['W', 'B', 'L', 'F', 'R', 'M', 'S', 'N'],
            ['M', 'N'], ['S', 'X', 'Q', 'H', 'W', 'G', 'N', 'R'],
            ['L', 'H', 'Q', 'N', 'S', 'W', 'B', 'F'],
            ['G', 'X', 'N', 'L', 'Q', 'J', 'M'],
            ['X', 'W', 'J', 'B', 'H', 'S', 'L'],
            ['J', 'B', 'R', 'M', 'W', 'S', 'G', 'F'],
            ['G', 'L', 'R', 'H', 'F', 'W', 'M', 'B'],
            ['Q', 'W', 'H', 'L', 'N', 'R', 'G'], ['X', 'R']]
        encodeLetters4 = [['L', 'G', 'S', 'X', 'J', 'N', 'W'],
            ['S', 'N', 'Q', 'F', 'J', 'X', 'W'],
            ['J', 'N', 'G', 'X', 'L', 'Q', 'F'],
            ['L', 'F'], ['H', 'G', 'S', 'M', 'B', 'Q', 'J', 'F'], ['R', 'B'],
            ['G', 'N'], ['M', 'G', 'F', 'L', 'N', 'S', 'B', 'Q'],
            ['G', 'N', 'S', 'L', 'M', 'F', 'J'], ['R', 'H'],
            ['J', 'H', 'W', 'M', 'G', 'L', 'B', 'Q']]
        retrievalLetters1 = [['X'], ['L'], ['H'], ['S'], ['W'], ['G'], ['R'],
            ['L'], ['W'], ['W'], ['S'], ['B']]
        retrievalLetters2 = [['X'], ['R'], ['S'], ['F'], ['M'], ['H'], ['N'],
            ['J'], ['L'], ['S'], ['W']]
        retrievalLetters3 = [['J'], ['S'], ['R'], ['N'], ['Q'], ['J'], ['Q'],
            ['M'], ['W'], ['L'], ['F']]
        retrievalLetters4 = [['Q'], ['F'], ['Q'], ['L'], ['S'], ['B'], ['N'],
            ['S'], ['F'], ['R'], ['J']]

# Determine which run-specific stimuli and variables to use; run task
if expInfo['run'] == 'Practice':
    demo() # Displays instructions
    print_experimenter()
    encodeLetters = [['A','G','F'], ['H', 'R', 'K','Y'],
                    ['E', 'B','D','Q','H','W']]
    jitteredTimes = [3, 3, 3]
    run_task(encodeLetters, retrievalLetters, jitteredTimes, filename, 'null')
elif expInfo['run'] == 'Scanner':
    if expRun['Which run?'] == '1':
        print_experimenter()
        print_trigger()
        run_task((encodeLetters1 + encodeLetters2), (retrievalLetters1 +
                    retrievalLetters2), (jitteredTimes1 + jitteredTimes2),
                    filename, 12)
    elif expRun['Which run?'] == '2':
        print_experimenter()
        print_trigger()
        run_task((encodeLetters3 + encodeLetters4), (retrievalLetters3 +
                    retrievalLetters4), (jitteredTimes3 + jitteredTimes4),
                    filename, 11)
elif expInfo['run'] == 'Backup':
    print_experimenter()
    print_trigger()
    if expBlock['Block?'] == '2': # If you need to run block 2 only
        run_task(encodeLetters2, retrievalLetters2, jitteredTimes2, filename,
                11)
    elif expBlock['Block?'] == '4': # If you need to run block 4 only
        run_task(encodeLetters4, retrievalLetters4, jitteredTimes4, filename,
                'null')

#logging.flush()
