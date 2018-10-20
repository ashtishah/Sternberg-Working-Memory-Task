""" SWMTTools 
    
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
import serial

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Setup the Window
win = visual.Window(
    fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)

#Initialize Background Image for Experiment
Background1 = visual.ImageStim(
    win=win, name='ScreenSetUp',
    image='Backgrounds/Slide3.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
#Initialize Image for Off State
Background2 = visual.ImageStim(
    win=win, name='FocalPoint',
    image='Backgrounds/FocalPoint.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
#Initialize Images for Demo
Slide1 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide1.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide2 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide2.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide3 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide5.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide4 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide6.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide5 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide7.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide6 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide8.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)
Slide7 = visual.ImageStim(
    win=win, name='Background1',
    image='Backgrounds/Slide9.tiff', mask=None, pos=(0,0), size=(2,2),
    color=1, colorSpace='rgb', flipHoriz=False, flipVert=False, texRes=128,
    interpolate=True, depth=0.0)

# Create text objects
experimenter = visual.TextStim(win, text="Waiting for the experimenter.",
    pos=(0,0), colorSpace='rgb', color=1, height=0.1, wrapWidth=1.5, depth=0.0)

trigger = visual.TextStim(win, text="Waiting for the scanner.",
    pos=(0,0), colorSpace='rgb', color=1, height=0.1, wrapWidth=1.5, depth=0.0)

lastSlide = visual.TextStim(win, text='Thanks!',
    pos=(0,0), colorSpace='rgb', color=1, height=0.1, wrapWidth=1.5, depth=0.0)

textHashTop = visual.TextStim(win, text='#  #  #  #  #  #  #  #',
        colorSpace='rgb', color=1, height=0.1, wrapWidth=1.5, depth=0.0)

def wait_keys():
    """ Shortcut for instructions key press """
    event.waitKeys(keyList=['1', '2', '3', '4', 'space'])
    if event.getKeys(keyList=['escape']):
            core.quit()

def demo():
    """ Displays instructions """
    Slide1.draw()
    win.flip()
    wait_keys()

    Slide2.draw()
    win.flip()
    wait_keys()

    Slide3.draw()
    win.flip()
    wait_keys()

    Slide4.draw()
    win.flip()
    wait_keys()

    Slide5.draw()
    win.flip()
    wait_keys()

    Slide6.draw()
    win.flip()
    wait_keys()

    Slide7.draw()
    win.flip()
    wait_keys()

def print_experimenter():
    """ Displays experimenter text """
    experimenter.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    if event.getKeys(keyList=['escape']):
            core.quit()

def print_trigger():
    """ Displays scanner text """
    trigger.draw()
    win.flip()
    event.waitKeys(keyList=['num_add', '+', 'equal', 'space'])
    if event.getKeys(keyList=['escape']):
            core.quit()

def print_last_slide():
    """ Displays thanks text """
    lastSlide.draw()
    win.flip()
    event.waitKeys(keyList=['1', '2', '3', '4', 'space'])
    core.quit()

def encode(load):
    """ Displays encode letters within correct number of text hashes.

    Parameters
    ----------
    load : string of letters to be displayed

    Local Variables
    ---------------
    textDisplayEncode : creates text hash and letter sequence
    visTextDisplayEncode : sets display for hash text sequence
    """
    Background1.draw()
    textDisplayEncode = ""
    if len(load) == 2:
        textDisplayEncode = '#  #  #  [ %s ] #  #  #'%" ".join(load)
    if len(load) == 3:
        textDisplayEncode = '#  #  [ %s ] #  #  #'%" ".join(load)
    if len(load) == 4:
        textDisplayEncode = '#  #  [ %s ] #  #'%" ".join(load)
    if len(load) == 5:
        textDisplayEncode = '#  #  [ %s ]  #'%" ".join(load)
    if len(load) == 6:
        textDisplayEncode = '#  [ %s ]  #'%" ".join(load)
    if len(load) == 7:
        textDisplayEncode = '#  [ %s ] '%" ".join(load)
    if len(load) == 8:
        textDisplayEncode = ' '.join(load)
    visTextDisplayEncode = visual.TextStim(win=win, text=textDisplayEncode,
        color=1, colorSpace='rgb', height=0.10, pos=(0,0.65))
    visTextDisplayEncode.draw()
    if event.getKeys(keyList=['escape']):
            core.quit()

def maintenance():
    """ Displays background slide """
    Background1.draw()
    textHashTop.pos = (0,0.65)
    textHashTop.draw()
    if event.getKeys(keyList=['escape']):
            core.quit()

def retrieval(letter):
    """ Displays retrieval letter within text hashes.

    Parameters
    ----------
    letter : letter to be displayed

    Local Variables
    ---------------
    visTextDisplayRetrieval : sets display for hash text sequence
    """
    Background1.draw()
    visTextDisplayRetrieval = visual.TextStim(win=win,
        text='#  #  #  #  [ %s ]  #  #  #'%" ".join(letter),
        color=1, colorSpace='rgb', height=0.10, pos=(0,0.65))
    visTextDisplayRetrieval.draw()
    if event.getKeys(keyList=['escape']):
            core.quit()

def correct_y_or_n(encodeLetters, retrievalLetters):
    """ Determines if the retrieval letter is in the list of encode letters.

    Parameters
    ----------
    encodeLetters : list of lists letters to be displayed and memorized
    retrievalLetters : list of letters that each correlate to a specific
                        list within encodeLetters
    Local Variables
    --------------
    CorrectResponse : empty list to add correct answers to
    """
    CorrectResponse = []
    for x in range (0, len(encodeLetters)):
       for y in range(0, len(encodeLetters[x])):
            if encodeLetters[x][y] == retrievalLetters[x][0]:
                CorrectResponse.append('yes')
       if len(CorrectResponse) != x+1:
            CorrectResponse.append('no')
    return CorrectResponse

def hit_or_miss(CorrectResponse, SubjectKeyResponse):
    """ Determines if the subject response is a hit, miss, or false alarm.

    Parameters
    ----------
    CorrectResponse : list of whether the answer is yes or no
    SubjectKeyResponse : list of keys the participant pressed during retrieval

    Local Variables
    ---------------
    HitOrMiss : empty list to add hit, miss, or false alarm to
    """
    HitOrMiss = []
    for x in range(0, len(SubjectKeyResponse)):
        if CorrectResponse[x] == SubjectKeyResponse[x]:
            HitOrMiss.append('Hit')
        elif CorrectResponse[x] == 'no' and SubjectKeyResponse[x] == 'yes':
            HitOrMiss.append('False Alarm')
        else:
            HitOrMiss.append('Miss')
    return HitOrMiss

def hit_or_miss_stats_overall(CorrectResponse, SubjectKeyResponse,
                            ReactionTime):
    """ Calculates hit, miss, or false alarms for overall run and calculates
        overall statistics.

    Parameters
    ----------
    CorrectResponse : list of whether the answer is yes or no
    SubjectKeyResponse : list of keys the participant pressed during retrieval
    ReactionTime : list of reaction times for each key press during retrieval

    Local Variables
    ---------------
    df_HitOrMissStatsOverall : dataframe to store stats
    """
    numHits = 0
    numMisses = 0
    numFalseAlarm = 0
    rxnTimeSum = 0
    not0 = 0
    for x in range(0, len(SubjectKeyResponse)):
        if ReactionTime[x] != 0.0:
            rxnTimeSum += ReactionTime[x]
            not0 += 1
        if CorrectResponse[x] == SubjectKeyResponse[x]:
            numHits += 1
        elif CorrectResponse[x] == 'no' and SubjectKeyResponse[x] == 'yes':
            numFalseAlarm += 1
        else:
            numMisses += 1

    total_sum = numHits + numMisses + numFalseAlarm
    accuracy = numHits*100.0/total_sum
    false_alarm_rate = numFalseAlarm*100.0/total_sum
    avg_rxn_time = rxnTimeSum/not0
    df_HitOrMissStatsOverall = pd.DataFrame([numHits, numMisses, numFalseAlarm,
        accuracy, false_alarm_rate, avg_rxn_time]).T
    return df_HitOrMissStatsOverall

def return_load_size(encodeLetters):
    """ Determines load size for each list within encodeLetters.

    Parameters
    ----------
    encodeLetters : list of lists of letters to display and be memorized

    Local Variables
    ---------------
    LoadSize : empty list to store load sizes of each trial
    """
    LoadSize = []
    for x in range(0, len(encodeLetters)):
        LoadSize.append(len(encodeLetters[x]))
    return LoadSize

def sort_by_loads_hit_or_miss(HitOrMiss, RxnTime):
    """ Calculates statistics for each load size.

    Parameters
    ----------
    HitOrMiss : list of participant responses per trial
    RxnTime : list of reaction times per trial

    Local Variables
    ---------------
    numHits : running total number of hits
    numMisses : running total number of misses
    numFalseAlarm : running total number of false alarms
    rxnTimeSum : running total sum of all reaction times
    not0 : running total number of answered trials
    """
    numHits = 0
    numMisses = 0
    numFalseAlarm = 0
    rxnTimeSum = 0
    not0 = 0

    for x in range(0, len(HitOrMiss)):
        if RxnTime[x] != 0.0:
            rxnTimeSum += RxnTime[x]
            not0 += 1.0
        if HitOrMiss[x] == 'Hit':
            numHits += 1
        elif HitOrMiss[x] == 'False Alarm':
            numFalseAlarm += 1
        elif HitOrMiss[x] == 'Miss':
            numMisses += 1

    if numHits == 0 and rxnTimeSum == 0:
        return [0, 0, 0, 0, 0]
    else:
        total_sum = numHits + numMisses + numFalseAlarm
        accuracy = numHits*100.0/total_sum
        false_alarm_rate = numFalseAlarm*100.0/total_sum
        avg_rxn_time = rxnTimeSum/not0
        return [numHits, numMisses, numFalseAlarm,
            accuracy, false_alarm_rate, avg_rxn_time]

def sort_by_loads(LoadSize, SubjectHitOrMiss, ReactionTime, filename):
    """ Appends hits, misses, or false alarms for each load size.

    Parameters
    ----------
    LoadSize : list of load sizes
    SubjectHitorMiss : list of subject hits, misses, or false alarms
    ReactionTime : list of reaction times per trial
    filename : name of file for saving data

    Local Variables
    ---------------
    HitOrMissX : lists of hits, misses, or false alarms for each load size
    RxnTimeX : list of reaction times for each load size
    """
    HitOrMiss2 = []
    RxnTime2 = []
    HitOrMiss3 = []
    RxnTime3 = []
    HitOrMiss4 = []
    RxnTime4 = []
    HitOrMiss5 = []
    RxnTime5 = []
    HitOrMiss6 = []
    RxnTime6 = []
    HitOrMiss7 = []
    RxnTime7 = []
    HitOrMiss8 = []
    RxnTime8 = []

    for x in range(0, len(LoadSize)):
        if LoadSize[x] == 2:
            HitOrMiss2.append(SubjectHitOrMiss[x])
            RxnTime2.append(ReactionTime[x])
        if LoadSize[x] == 3:
            HitOrMiss3.append(SubjectHitOrMiss[x])
            RxnTime3.append(ReactionTime[x])
        if LoadSize[x] == 4:
            HitOrMiss4.append(SubjectHitOrMiss[x])
            RxnTime4.append(ReactionTime[x])
        if LoadSize[x] == 5:
            HitOrMiss5.append(SubjectHitOrMiss[x])
            RxnTime5.append(ReactionTime[x])
        if LoadSize[x] == 6:
            HitOrMiss6.append(SubjectHitOrMiss[x])
            RxnTime6.append(ReactionTime[x])
        if LoadSize[x] == 7:
            HitOrMiss7.append(SubjectHitOrMiss[x])
            RxnTime7.append(ReactionTime[x])
        if LoadSize[x] == 8:
            HitOrMiss8.append(SubjectHitOrMiss[x])
            RxnTime8.append(ReactionTime[x])

    df_HitOrMiss2Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss2,
                                                                RxnTime2))
    df_HitOrMiss3Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss3,
                                                                RxnTime3))
    df_HitOrMiss4Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss4,
                                                                RxnTime4))
    df_HitOrMiss5Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss5,
                                                                RxnTime5))
    df_HitOrMiss6Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss6,
                                                                RxnTime6))
    df_HitOrMiss7Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss7,
                                                                RxnTime7))
    df_HitOrMiss8Stats = pd.DataFrame(sort_by_loads_hit_or_miss(HitOrMiss8,
                                                                RxnTime8))
    percentAccuracy = [df_HitOrMiss2Stats.iloc[3,0],
                    df_HitOrMiss3Stats.iloc[3,0], df_HitOrMiss4Stats.iloc[3,0],
                    df_HitOrMiss5Stats.iloc[3,0], df_HitOrMiss6Stats.iloc[3,0],
                    df_HitOrMiss7Stats.iloc[3,0], df_HitOrMiss8Stats.iloc[3,0]]
    percentFalseAlarm = [df_HitOrMiss3Stats.iloc[4,0],
                    df_HitOrMiss4Stats.iloc[4,0], df_HitOrMiss5Stats.iloc[4,0],
                    df_HitOrMiss6Stats.iloc[4,0], df_HitOrMiss7Stats.iloc[4,0]]
    df_DataSummary = pd.concat([df_HitOrMiss2Stats, df_HitOrMiss3Stats,
                            df_HitOrMiss4Stats, df_HitOrMiss5Stats,
                            df_HitOrMiss6Stats, df_HitOrMiss7Stats,
                            df_HitOrMiss8Stats], axis=1)
    header = ['load_size_2', 'load_size_3', 'load_size_4', 'load_size_5',
            'load_size_6', 'load_size_7', 'load_size_8']
    rows = ['total_hits', 'total_misses', 'total_falsealarm',
            'percent_accuracy', 'percent_falsealarm', 'avg_rxn_time']
    df_DataSummary.index = rows
    df_DataSummary.to_csv('{}_LoadSummary.csv'.format(filename), index=True,
                        header=header)
"""
Uncomment this code to send an Aux trigger to the NIRS machine.

class SerialPortTriggerHandler(object):
    def __init__(self, *args, **kwargs):
        self.port = serial.Serial(*args, **kwargs)
    
    def write(self, data):
        self.port.write(str(data))
    
    def __exit__(self):
        self.port.close()
    
    def __del__(self):
        self.port.close()

trigger_handler = SerialPortTriggerHandler('COM3')
"""
def run_task(encodeLetters, retrievalLetters, jitteredTimes, filename, slide):
    """ Runs the main function and calls input from SWMT.py and runs statistics.

    Parameters
    ---------
    encodeLetters : array of letters to be displayed,
    retrievalLetters : target or distractor letters
    jitteredTimes : time between each event
    filename : name of file that the results will be saved in
    slide : int point at which to start new block

    Local Variables
    --------------
    clock : PsychoPy internal clock
    running_clock : clock recording running time at start of each trial
    trial_clock : clock recording length of each trial minus fixation time
    outfile : filename abbrevation to simplify saving
    SubjectResponses : Records all of the keys pressed and the times at which
                    they were pressed during the Retrieval phase. This resets
                    every time there is a new task
    SubjectKeyResponse : Records whether the subject responded 'yes', 'no',
                        or 'null' (no response)
    ReactionTime : Records the subjects reaction time
    df_SubjectKeyResponse : Data Frame which saves SubjectKeyResponse
    df_ReactionTime : Data Frame which saves ReactionTime
    CorrectResponse : List of what the correct response should be
    df_CorrectResponse : Data Frame which saves CorrectResponse
    SubjectHitorMiss : List of whether the subjects response was a Hit, Miss,
                    or FalseAlarm
    df_SubjectHitorMiss : Data Frame which saves SubjectHitorMiss
    HitOrMissStats : List which returns [numHits, numMisses, numFalseAlarm]
                    for the whole experiment
    df_HitOrMissStats : Data Frame which saves HitOrMissStats
    """
    clock = core.Clock()
    running_clock = core.Clock()
    trial_clock = core.Clock()

    outfile = "{}.csv".format(filename)

    SubjectResponses = []
    SubjectKeyResponse = []
    ReactionTime = []
    CorrectResponse = correct_y_or_n(encodeLetters, retrievalLetters)
    SubjectHitOrMiss = []
    TrialTime = []
    RunningTime = []
    load_type = []

    df_SubjectKeyResponse = pd.DataFrame([SubjectKeyResponse]).T
    df_ReactionTime = pd.DataFrame([ReactionTime]).T
    df_CorrectResponse = pd.DataFrame([CorrectResponse]).T
    df_SubjectHitOrMiss = pd.DataFrame([SubjectHitOrMiss]).T
    #trigger_handler.write('5')
    core.wait(1)
    #trigger_handler.write('0')

    # Loop that will run through the entire task, each load at a time.
    for x in range (0, len(encodeLetters)):
        if x == slide:
            print_experimenter()
            print_trigger()
            running_clock.reset()
        # Encode : 4s, Maintainenance : 8s, Retrieval : 4s
        trial_clock.reset()
        running_time = running_clock.getTime()
        RunningTime.append(running_time)
        encode(encodeLetters[x])
        win.flip()
        core.wait(4)
        #trigger_handler.write('5')
        maintenance()
        win.flip()
        core.wait(8)
        #trigger_handler.write('0')
        retrieval(retrievalLetters[x])
        win.flip()
        clock.reset()
        SubjectResponses = [[('null', 0.0)]]

        # Record the subjects responses (key and time stamp)
        while clock.getTime() < 4:
            keyPressed = event.getKeys(keyList=['z', 'slash'],
                                        timeStamped=clock)
            if keyPressed:
                SubjectResponses.append(keyPressed)

        trial_time = trial_clock.getTime()
        TrialTime.append(trial_time)

        load_length = return_load_size(encodeLetters)
        l = load_length[x]
        a = min(load_length)
        b = max(load_length)
        if l == a:
            load_type.append('low')
        elif l == b:
            load_type.append('high')
        else:
            load_type.append('med')
        #trigger_handler.write('5')
        # Display Jittered State
        Background2.draw()
        win.flip()
        core.wait(jitteredTimes[x])
        #trigger_handler.write('0')

        # Add reaction time to ReactionTime and response to SubjectsKeyResponse
        ReactionTime.append(SubjectResponses[-1][0][1])
        if SubjectResponses[-1][0][0] == 'slash':
            SubjectKeyResponse.append('yes')
        elif SubjectResponses[-1][0][0] == 'z':
            SubjectKeyResponse.append('no')
        else:
            SubjectKeyResponse.append('null')

        # Add Subject Response and Times to data frame
        df_SubjectKeyResponse = pd.DataFrame([SubjectKeyResponse]).T
        df_ReactionTime = pd.DataFrame([ReactionTime]).T
        df_TrialTime = pd.DataFrame([TrialTime]).T
        df_RunningTime = pd.DataFrame([RunningTime]).T
        df_LoadType = pd.DataFrame([load_type]).T

        # Categorize whether subjects response was a Hit, Miss, or False Alarm
        SubjectHitOrMiss = hit_or_miss(CorrectResponse, SubjectKeyResponse)
        df_SubjectHitOrMiss = pd.DataFrame([SubjectHitOrMiss]).T
        header_cols = ['subj_response', 'corr_response', 'hit_miss_false_alarm',
                    'reaction_time', 'trial_dur', 'running_time', 'loadsize']
        df_DataSummary = pd.concat([df_SubjectKeyResponse, df_CorrectResponse,
                                df_SubjectHitOrMiss, df_ReactionTime,
                                df_TrialTime, df_RunningTime, df_LoadType],
                                axis=1)
        df_DataSummary.to_csv(outfile, index=False, header=header_cols)

    # Calculate overall stats for the whole task and save to dataframe
    df_HitOrMissStatsOverall = hit_or_miss_stats_overall(CorrectResponse,
                                            SubjectKeyResponse, ReactionTime)
    df_DataSummary = pd.concat([df_SubjectKeyResponse, df_CorrectResponse,
                    df_SubjectHitOrMiss, df_ReactionTime, df_TrialTime,
                    df_RunningTime, df_LoadType, df_HitOrMissStatsOverall],
                    axis=1)
    header_cols = ['subj_response', 'corr_response', 'hit_miss_false_alarm',
                'reaction_time', 'trial_dur', 'running_time', 'loadsize',
                'total_hits', 'total_misses', 'total_falsealarm',
                'percent_accuracy', 'percent_falsealarm', 'avg_rxn_time']
    df_DataSummary.to_csv(outfile, index=True, header=header_cols)

    #Calculate overall stats for whole task by load size
    LoadSize = return_load_size(encodeLetters)
    df_HitOrMissStatsByLoad = sort_by_loads(LoadSize, SubjectHitOrMiss,
                            ReactionTime, filename)
    print_last_slide()
