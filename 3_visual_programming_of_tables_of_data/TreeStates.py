import os
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *


DATA_FILE = os.path.join(os.getcwd(), '3_visual_programming_of_tables_of_data', 'States.txt')


class State:
    def __init__(self, stateString):
        stateST = stateString.rstrip()
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
        i = 0
        self._states = []
        while i < len(self.contents):
            if len(self.contents[i]) > 0:
                self.state = State(self.contents[i])
                self._states.append(self.state)
                i += 1

    def getText(self):
        return self.contents

    def getStateList(self):
        return self._states


class BuildUI:
    def __init__(self, root, slist):
        root.geometry('350x200')
        self.states = slist
        self.tree = Treeview(root)

        self.tree['columns'] = ('abbrev', 'capital', 'founded')
        self.tree.column('#0', width=100, minwidth=100, stretch=NO)
        self.tree.column('abbrev', width=50, minwidth=50, stretch=NO)
        self.tree.column('capital', width=100, minwidth=100, stretch=NO)
        self.tree.column('founded', width=70, minwidth=60, stretch=NO)

        self.tree.heading('#0', text='Name')
        self.tree.heading('abbrev', text='Abbrev')
        self.tree.heading('capital', text='Capital')
        self.tree.heading('founded', text='Founded')
        style = ttk.Style()
        style.configure('Treeview.Heading', font=(None, 10, 'bold'))

        i = 1
        for state in self.states:
            self.tree.insert('', i, text=state.getStateName(), values=(
                state.getAbbrev(),
                state.getCapital(),
                state.getFounded()))
            i += 1

        self.tree.pack(side=TOP, fill=X)


def main():
    sl = StateList(DATA_FILE)
    root = Tk()
    root.geometry('300x200')
    bdui = BuildUI(root, sl.getStateList())

    root.title('State List')
    root.mainloop()


if __name__ == '__main__':
    main()
