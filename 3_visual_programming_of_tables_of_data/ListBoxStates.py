import os
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

from typing import List


DATA_FILE = os.path.join(os.getcwd(), '3_visual_programming_of_tables_of_data', 'States.txt')


class State:
    def __init__(self, stateString: str):
        self._tokens = stateString.split(',')
        self._statename = ''
        if len(self._tokens) > 3:
            self._statename = self._tokens[0]
            self._abbrev = self._tokens[1]
            self._founded = self._tokens[2]
            self._capital = self._tokens[3]

    def getStateName(self):
        return self._statename

    def toString(self):
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

        i = 0
        self._states = []
        while i < len(self.contents):
            if len(self.contents[i]) > 0:
                self._states.append(State(self.contents[i]))
                i += 1

    def getText(self):
        return self.contents

    def getStateList(self):
        return self._states


class BuildUI:
    def __init__(self, root, slist):
        self.states: List[State] = slist
        self.listbox = Listbox(root, selectmode=SINGLE)
        self.listbox.bind('<<ListboxSelect>>', self.onselect)

        self.listbox.grid(column=0, row=0, rowspan=4, padx=10)

        self.entry = Entry(root)
        self.entry.grid(column=0, row=4, pady=4)
        self.entry.focus_set()
        self.entry.bind('<Key>', self.keyPress)

        for state in self.states:
            self.listbox.insert(END, state.getStateName())

        self.lbstate = Label('')
        self.lbabbrev = Label(root, text='', foreground='red')
        self.lbcapital = Label('')
        self.lbfounded = Label('')
        self.lbstate.grid(column=2, row=0, sticky=W)
        self.lbabbrev.grid(column=2, row=1, sticky=W)
        self.lbcapital.grid(column=2, row=2, sticky=W)
        self.lbfounded.grid(column=2, row=3, sticky=W)

        scrollBar = Scrollbar(root)
        scrollBar.config(command=self.listbox.yview)

        scrollBar.grid(row=0, column=1, rowspan=4, sticky='NS')
        self.listbox.config(yscrollcommand=scrollBar.set)

    def onselect(self, evt):
        index = self.listbox.curselection()
        i = int(index[0])
        state = self.states[i]
        self.loadLabels(state)

    def loadLabels(self, state):
        self.lbstate.config(text=state.getStateName())
        self.lbcapital.config(text=state.getCapital())
        self.lbabbrev.config(text=state.getAbbrev())
        self.lbfounded.config(text=state.getFounded())

    def keyPress(self, evt):
        char = self.entry.get().upper()
        i = 0
        found = False

        while(not found) and (i < len(self.states)):
            found = self.states[i].getStateName().startswith(char)
            if not found:
                i += 1

        if found:
            state = self.states[i]
            self.listbox.select_clear(0, END)
            self.listbox.select_set(i)
            self.listbox.see(i)
            self.loadLabels(state)


def main():
    sl = StateList(DATA_FILE)
    root = Tk()
    root.geometry('300x200')
    bdui = BuildUI(root, sl.getStateList())

    root.title('State List')
    root.mainloop()


if __name__ == '__main__':
    print(os.getcwd())
    main()
