# Message codes by name
MESSAGE_TYPE_DICT = {
    'vlogInformation': [4],
    'loopDetectors': [5,6],
    'otherInputs': [7,8],
    'intPhaseCycle': [9,10],
    'overigeUitgangenGUS': [11,12],
    'extSignalState': [13,14],
    'otherOutputsWUS': [15,16],
    'desiredProgramStatus': [17,18],
    'actualProgramStatus': [19,20],
    'thermometer': [23,24],
    'instructionVariables': [32],
    'OVEmergencyServiceInfo': [34]
}
# The below message types only exist for the timestamp of their creation
WIPED_MESSAGES = ['instructionVariables', 'OVEmergencyServiceInfo']