from java.io import File
import org.bukkit as bukkit
server = bukkit.Bukkit.getServer()
log = server.getLogger()

from java.util.logging import Level
def info(*text):
    log.log(Level.INFO,u"[%s] "%__plugin_name__+u" ".join(map(unicode,text)))
def severe(*text):
    log.log(Level.SEVERE,u"[%s] "%__plugin_name__+u" ".join(map(unicode,text)))
def msg(player,*text):
    player.sendMessage(u"[%s] "%__plugin_name__+u" ".join(map(unicode,text)))

from org.bukkit.configuration.file import YamlConfiguration
def loadConfig(path = "config.yml"):
    if not pyplugin.isEnabled():
        severe("Plugin tried to load '%s' before plugin was initialized"%path)
        return
    return YamlConfiguration.loadConfiguration(File(pyplugin.dataFolder,path))

def addSupportedCharacters(characters):
    from java.lang import StringBuilder
    from java.lang.reflect import Field
    from java.lang.reflect import Modifier
    from net.minecraft.server import SharedConstants
    try:
        field = SharedConstants.getDeclaredField("allowedCharacters")
        field.setAccessible(True)
        modifiersField = Field.getDeclaredField("modifiers")
        modifiersField.setAccessible(True)
        modifiersField.setInt(field, field.getModifiers() & ~Modifier.FINAL)
        oldallowedchars = field.get(None)
        sb = StringBuilder()
        sb.append(oldallowedchars)
        sb.append(characters)
        field.set(None,sb.toString())
    except:
        print "Error while adding additional supported unicode characters"