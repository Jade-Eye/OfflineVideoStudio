# UI Architecture

**Author : Mohit Singh**

PySide6 is the planned desktop UI framework. The goal is modern, exotic, polished and usable for long production sessions.

Main workspaces: Dashboard, Working Studio, Character Studio, Knowledge Studio, Training Studio, Model Lab, Sequencer and Settings.

UI must not directly control AI runtimes or database internals. Long-running generation, indexing, training and rendering must run without freezing the UI.
