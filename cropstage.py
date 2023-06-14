import os
import sys
import subprocess

# Launch UI.py in a separate process with pythonw
ui_script = os.path.join(sys.path[0], "UI.py")
subprocess.Popen(["pythonw", ui_script])

# Exit the run_ui.py script
sys.exit()
