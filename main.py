import logging
import subprocess
import distutils.spawn
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

class SystemManagementDirect(Extension):
  def __init__(self):
    logger.info('Loading Gnome Settings Extension')
    super(SystemManagementDirect, self).__init__()
    self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):
  def on_event(self, event, extension):
    keyword = event.get_keyword()

    # Find the keyword id using the keyword (since the keyword can be changed by users)
    for id, kw in extension.preferences.items():
      if kw == keyword:
        self.on_match(id)
        return HideWindowAction()

  def on_match(self, id):
    if id == 'lock-screen':
      subprocess.Popen(['loginctl', 'lock-session'])
    if id == 'suspend':
      subprocess.Popen(['systemctl', 'suspend', '-i'])
    if id == 'shutdown':
      subprocess.Popen(['systemctl', 'poweroff', '-i'])
    if id == 'restart':
      subprocess.Popen(['systemctl', 'reboot', '-i'])
    if id == 'hibernate':
      subprocess.Popen(['systemctl', 'hibernate'])

SystemManagementDirect().run()
