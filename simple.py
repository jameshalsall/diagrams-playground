from diagrams import Diagram
from diagrams.onprem.container import Docker
from diagrams.onprem.database import Postgresql
from diagrams.onprem.network import Traefik

with Diagram("Web Service", show=False):
    Traefik("lb") >> Docker("web") >> Postgresql("userdb")
