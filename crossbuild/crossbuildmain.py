
import sys
import os
import argparse
import subprocess

class CommandLineParser:
    def __init__(self):
        self.term_width = 100
        self.formater = lambda prog: argparse.HelpFormatter(prog, max_help_position=int(self.term_width / 2), width=self.term_width)
        self.commands = {}
        self.hidden_commands = []
        self.parser = argparse.ArgumentParser(prog='cbuild', formatter_class=self.formater)
        self.parser.add_argument('command', nargs='?')

    def run(self, args):
        # If first arg is not a known command, assume user wants to run the setup
        # command.
        known_commands = list(self.commands.keys()) + ['-h', '--help']
        options = self.parser.parse_args(args)
        try:
            return options.run_func(options)
        except Exception:
            return 2

def is_tool(name):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            return False
    return True

def run(original_args, mainfile):
	if is_tool('ls'):
		print("ls found")
	else:
		print("ls not found")

	args = original_args[:]
	return CommandLineParser().run(args)

def main():
    # Always resolve the command path so Ninja can find it for regen, tests, etc.
    if 'cbuild.exe' in sys.executable:
        assert(os.path.isabs(sys.executable))
        launcher = sys.executable
    else:
        launcher = os.path.realpath(sys.argv[0])
    return run(sys.argv[1:], launcher)

if __name__ == '__main__':
    sys.exit(main())