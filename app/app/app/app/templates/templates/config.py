class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///iraqi_policy_simulation.db'  # SQLite for local storage
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIMULATION_API_URL = 'http://api_to_fetch_simulation_data.com'
