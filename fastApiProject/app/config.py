import json
from typing import Any

class Config:
    def __init__(self, config_path: str = 'local.settings.json'):
        with open(config_path, 'r') as f:
            config = json.load(f)
        self.dbkey: str = config['Values']['dbkey']
        self.DBURI: str = config['Values']['DBURI']
        self.DBName: str = config['Values']['DBName']
        self.jwt_key: str = config['JwtSettings']['Key']
        self.jwt_issuer: str = config['JwtSettings']['Issuer']
        self.jwt_audience: str = config['JwtSettings']['Audience']  # Keep it as a single string

config = Config()
