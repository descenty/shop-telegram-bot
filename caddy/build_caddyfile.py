import sys
import os
from dotenv import load_dotenv

load_dotenv()

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))

with open(script_directory + "/Caddyfile", "w") as f:
    f.write(
        f'{os.getenv("WEBHOOK_HOST")} {{reverse_proxy /* {os.getenv("WEBAPP_HOST")}:{os.getenv("WEBAPP_PORT")}}}'
    )
