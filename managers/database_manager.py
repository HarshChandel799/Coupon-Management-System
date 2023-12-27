import os
import logging
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up a logger
logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler("app.log")

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


class DatabaseManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
            cls._instance.initialize()  # Initialize the instance when it's created.
        return cls._instance

    def initialize(self):
        # Initialize the database connection
        MONGO_DB_CONNECTION_STRING = os.getenv("MONGO_DB_CONNECTION_STRING")
        
        # Create a connection using MongoClient
        try:
            self.client = MongoClient(MONGO_DB_CONNECTION_STRING)
            self.db = self.client["test"]
            self.coupon_data_collection = self.db["coupon_data"]
            logger.info("Successfully connected to the database")
        except Exception as e:
            logger.error(f"Failed to connect to the database: {str(e)}")


    def get_coupons(self):
        result = list(self.coupon_data_collection.find({},{"_id":0}))
        return 200, result
    
    def delete_coupon(self, coupon_id):
        update = self.coupon_data_collection.delete_one(
            { "coupon_name": coupon_id }
        )
        if update: 
            return 200
        else :
            return 400
    
    def create_coupon(self,coupon_name,validity):
        self.coupon_data_collection.insert_one({
            "coupon_name":coupon_name,
            "validity":validity
        })
        return 200