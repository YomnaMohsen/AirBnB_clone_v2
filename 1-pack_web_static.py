 #!/usr/bin/python3
"""a Fabric script that generates a .tgz archive 
    from the contents of the web_static folder"""
    

from fabric.api import local
from datetime import datetime
    
def do_pack():
    """generates .tgz file"""
    try:
        local('mkdir -p versions')
        dt = datetime.utcnow()
        f_name = "web_static_{}{}{}{}{}{}.tgz".format(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
        local("tar cf versions/{} web_static".format(f_name))
        return "versions/"        
    except Exception:
        return None   
      