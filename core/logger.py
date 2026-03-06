from datetime import datetime


class Logger:

    def log(self, engine, payload):

        print(
            f"[LOG {datetime.utcnow()}] engine={engine} payload={payload}"
        )
