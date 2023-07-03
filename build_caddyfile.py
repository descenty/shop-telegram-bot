import os
from dotenv import load_dotenv

load_dotenv()

with open("Caddyfile", "w") as f:
    f.write(
        f'{os.getenv("WEBHOOK_HOST")} {{\n\treverse_proxy /* {os.getenv("WEBAPP_HOST")}:{os.getenv("WEBAPP_PORT")}\n}}'
    )
