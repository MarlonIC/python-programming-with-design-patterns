import os
from tkinter import *
from tkinter.ttk import *


DATA_FILE = os.path.join(os.getcwd(), '3_visual_programming_of_tables_of_data', 'States.txt')


class State:
    def __init__(self, stateString):
        self._tokens = stateString.split(',')
        self._statename = ''
        if len(self._tokens) > 3:
            self._statename = self._tokens[0]
            self._abbrev = self._tokens[1]
            self._founded = self._tokens[2]
            self._capital = self._tokens[3]

    def getStateName(self):
        return self._statename

    def getCapital(self):
        return self._capital

    def getAbbrev(self):
        return self._abbrev

    def getFounded(self):
        return self._founded


class StateList:
    def __init__(self, stateFile):
        with open(stateFile) as self.fobj:
            self.contents = self.fobj.readlines()

        self._states = []
        for st in self.contents:
            if len(st)>0:
                self.state = State(st)
                self._states.append(self.state)

    def getText(self):
        return self.contents

    def getStateList(self):
        return self._states


class BuildUI:
    def __init__(self, root, slist):
        self.states = slist
        names = []
        for s in self.states:
            names.append(s.getStateName())

        self.combo = Combobox(root, values=names)
        self.combo.current(0)
        self.combo.bind('<<ComboboxSelected>>', self.onselect)
        self.combo.grid(column=0, row=0, rowspan=8, padx=10)

        self.lbstate = Label(text='')
        self.lbabbrev = Label(text='', foreground='red')
        self.lbcapital = Label(text='')
        self.lbfounded = Label(text='')

        self.lbstate.grid(column=2, row=0, sticky=NW)
        self.lbabbrev.grid(column=2, row=1, sticky=NW)
        self.lbcapital.grid(column=2, row=2, sticky=NW)
        self.lbfounded.grid(column=2, row=3, sticky=NW)

    def onselect(self, evt):
        index = self.combo.current()
        state = self.states[index]
        self.loadLabels(state)

    def loadLabels(self, state):
        self.lbstate.config(text=state.getStateName())
        self.lbcapital.config(text=state.getCapital())
        self.lbabbrev.config(text=state.getAbbrev())
        self.lbfounded.config(text=state.getFounded())


def main():
    sl = StateList(DATA_FILE)
    root = Tk()
    root.geometry('300x200')
    bdui = BuildUI(root, sl.getStateList())

    root.title('State List')
    root.mainloop()


if __name__ == '__main__':
    main()
