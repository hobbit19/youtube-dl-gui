#! /usr/bin/env python

from .version import __version__
from .Utils import (
  get_HOME,
  file_exist,
  get_os_type,
  fix_path,
  makedir
)

SETTINGS_FILENAME = 'settings'
LINUX_FILES_PATH = get_HOME() + '/.youtube-dl-gui'
WINDOWS_FILES_PATH = get_HOME() + '\\youtube-dl-gui'

class OptionsHandler():
  
  settings_abs_path = ''
  
  def __init__(self, statusBarWrite):
    self.statusBarWrite = statusBarWrite
    self.set_settings_path()
    self.load_default()
    self.load_settings()
  
  def load_settings(self):
    if not file_exist(self.get_config_path()):
      makedir(self.get_config_path())
    if file_exist(self.settings_abs_path):
      self.load_from_file()
  
  def load_default(self):
    self.savePath = get_HOME()
    self.videoFormat = "default"
    self.dashAudioFormat = "NO SOUND"
    self.clearDashFiles = False
    self.toAudio = False
    self.keepVideo = False
    self.audioFormat = "mp3"
    self.audioQuality = 5
    self.startTrack = "1"
    self.endTrack = "0"
    self.maxDownloads = "0"
    self.minFileSize = "0"
    self.maxFileSize = "0"
    self.writeSubs = False
    self.writeAllSubs = False
    self.writeAutoSubs = False
    self.embedSubs = False
    self.subsLang = "English"
    self.idAsName = False
    self.ignoreErrors = True
    self.writeDescription = False
    self.writeInfo = False
    self.writeThumbnail = False
    self.retries = "10"
    self.userAgent = ""
    self.referer = ""
    self.proxy = ""
    self.username = ""
    self.password = ""
    self.videoPass = ""
    self.updatePath = self.get_config_path()
    self.autoUpdate = False
    self.cmdArgs = ""
    self.enableLog = True
    self.writeTimeToLog = True
  
  def get_config_path(self):
    if get_os_type() == 'nt':
      return WINDOWS_FILES_PATH
    else:
      return LINUX_FILES_PATH
  
  def set_settings_path(self):
    self.settings_abs_path = self.get_config_path()
    self.settings_abs_path = fix_path(self.settings_abs_path)
    self.settings_abs_path += SETTINGS_FILENAME
  
  def read_from_file(self):
    f = open(self.settings_abs_path, 'r')
    options = f.readlines()
    f.close()
    return options
  
  def extract_options(self, options):
    opts = []
    for option in options:
      opt = option.split('=')
      if not len(opt) < 2:
	opts.append(opt[1].rstrip('\n'))
    return opts
  
  def check_settings_file_version(self, options):
    data = options.pop(0).rstrip('\n')
    name, version = data.split('=')
    if name == 'Version' and version == __version__:
      return True
    else:
      return False
  
  def load_from_file(self):
    options = self.read_from_file()
    if self.check_settings_file_version(options):
      opts = self.extract_options(options)
      try:
	self.savePath = opts[0].decode('utf8')
	self.videoFormat = opts[1]
	self.dashAudioFormat = opts[2]
	self.clearDashFiles = opts[3] in ['True']
	self.toAudio = opts[4] in ['True']
	self.keepVideo = opts[5] in ['True']
	self.audioFormat = opts[6]
	self.audioQuality = int(opts[7])
	self.startTrack = opts[8]
	self.endTrack = opts[9]
	self.maxDownloads = opts[10]
	self.minFileSize = opts[11]
	self.maxFileSize = opts[12]
	self.writeSubs = opts[13] in ['True']
	self.writeAllSubs = opts[14] in ['True']
	self.writeAutoSubs = opts[15] in ['True']
	self.embedSubs = opts[16] in ['True']
	self.subsLang = opts[17]
	self.idAsName = opts[18] in ['True']
	self.ignoreErrors = opts[19] in ['True']
	self.writeDescription = opts[20] in ['True']
	self.writeInfo = opts[21] in ['True']
	self.writeThumbnail = opts[22] in ['True']
	self.retries = opts[23]
	self.userAgent = opts[24]
	self.referer = opts[25]
	self.proxy = opts[26]
	self.username = opts[27]
	self.updatePath = opts[28].decode('utf8')
	self.autoUpdate = opts[29] in ['True']
	self.cmdArgs = opts[30]
	self.enableLog = opts[31] in ['True']
	self.writeTimeToLog = opts[32] in ['True']
      except:
	self.statusBarWrite('Error while loading settings file')
	self.load_default()
    else:
      self.statusBarWrite('Old settings file loading default settings')
      self.load_default()
    
  def save_to_file(self):
    f = open(self.settings_abs_path, 'w')
    f.write('Version='+__version__+'\n')
    f.write('SavePath='+self.savePath.encode('utf-8')+'\n')
    f.write('VideoFormat='+str(self.videoFormat)+'\n')
    f.write('DashAudioFormat='+str(self.dashAudioFormat)+'\n')
    f.write('ClearDashFiles='+str(self.clearDashFiles)+'\n')
    f.write('ToAudio='+str(self.toAudio)+'\n')
    f.write('KeepVideo='+str(self.keepVideo)+'\n')
    f.write('AudioFormat='+str(self.audioFormat)+'\n')
    f.write('AudioQuality='+str(self.audioQuality)+'\n')
    f.write('StartTrack='+str(self.startTrack)+'\n')
    f.write('EndTrack='+str(self.endTrack)+'\n')
    f.write('MaxDownloads='+str(self.maxDownloads)+'\n')
    f.write('MinFileSize='+str(self.minFileSize)+'\n')
    f.write('MaxFileSize='+str(self.maxFileSize)+'\n')
    f.write('WriteSubtitles='+str(self.writeSubs)+'\n')
    f.write('WriteAllSubtitles='+str(self.writeAllSubs)+'\n')
    f.write('WriteAutoSubtitles='+str(self.writeAutoSubs)+'\n')
    f.write('EmbedSubs='+str(self.embedSubs)+'\n')
    f.write('SubtitlesLanguage='+str(self.subsLang)+'\n')
    f.write('IdAsName='+str(self.idAsName)+'\n')
    f.write('IgnoreErrors='+str(self.ignoreErrors)+'\n')
    f.write('WriteDescription='+str(self.writeDescription)+'\n')
    f.write('WriteInfo='+str(self.writeInfo)+'\n')
    f.write('WriteThumbnail='+str(self.writeThumbnail)+'\n')
    f.write('Retries='+str(self.retries)+'\n')
    f.write('UserAgent='+str(self.userAgent)+'\n')
    f.write('Referer='+str(self.referer)+'\n')
    f.write('Proxy='+str(self.proxy)+'\n')
    f.write('Username='+str(self.username)+'\n')
    # We dont store password & videoPass for security reasons
    f.write('UpdatePath='+self.updatePath.encode('utf-8')+'\n')
    f.write('AutoUpdate='+str(self.autoUpdate)+'\n')
    f.write('CmdArgs='+str(self.cmdArgs)+'\n')
    f.write('EnableLog='+str(self.enableLog)+'\n')
    f.write('WriteTimeToLog='+str(self.writeTimeToLog)+'\n')
    f.close()
    
