from dataclasses import dataclass
from decouple import config

@dataclass
class Settings:
    @property
    def db(self):
        return 'postgresql://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=config('USER'),
            password=config('PASSWORD'),
            host=config('HOST'),
            port=config('PORT'),
            db_name=config('DB_NAME')
        )

settings = Settings()