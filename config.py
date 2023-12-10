import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

class Configuration:
    OS_NAME = ''
    BINARIES_DIR = ''
    OS_SPECIFIC_STATS = ''

class MacOSConfiguration(Configuration):
    OS_NAME = 'macos_arm64'
    BINARIES_DIR = f'{curr_dir}/binaries/macos_arm64'
    OS_SPECIFIC_STATS = '/usr/bin/time -l'

config = MacOSConfiguration()
