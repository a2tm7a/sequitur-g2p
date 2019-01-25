import subprocess
from subprocess import Popen, PIPE, STDOUT

class G2P:
    def __init__(self, model):
        self.model = model

    def train(self):
        raise NotImplementedError("Not available right now")
    """
    Input should be lower case
    """
    def get_phoneme(self, word):
        # os.system()
        cmd = "python g2p.py --model " + self.model + " --word " + word
        proc = Popen(cmd.split(' '), stdout=PIPE, stderr=PIPE)
        (output, error) = proc.communicate()
        output = str(output, 'utf-8')
        return output.split('\t')[1].replace('\n','')
