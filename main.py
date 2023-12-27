import os
import logging
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from setup.setup_ngrok import setup_ngrok

import route_tasks.coupon_tasks as ct


app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a file handler
file_handler = logging.FileHandler("app.log", mode="w")

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)


@app.get("/get_coupons")
def get_coupons_data():
    try :
        resp_code, data = ct.get_coupon_data()
        if resp_code == 200 :
            return JSONResponse(content={"data": data}, status_code=200) 
        else :
            raise HTTPException(status_code = resp_code)
    except HTTPException as e : 
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)
    

@app.delete("/delete_coupon")
def delete_coupon(coupon_name: str):
    try :
        resp_code = ct.delete_coupon(coupon_name)
        if resp_code == 200 :
            return JSONResponse(content={"coupon_name": coupon_name}, status_code=200) 
        else :
            raise HTTPException(status_code = resp_code)
    except HTTPException as e : 
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)
    
@app.post("/create_coupon")
def create_coupon(request_body:dict):
    try :
        resp_code = ct.create_coupon(request_body)
        if resp_code == 200 :
            return JSONResponse(content={"data": "inserted successfully"}, status_code=200) 
        else :
            raise HTTPException(status_code = resp_code)
    except HTTPException as e : 
        return JSONResponse(content={"detail": e.detail}, status_code=e.status_code)
    

if __name__ == "__main__":
    # Setup Ngrok if no BASE_URL (Used for local development)
    # BASE_URL = os.getenv("BASE_URL")
    # if not BASE_URL:
    #     logger.info("")
    #     logger.info("---------------- Ngrok Setup ----------------")
    #     ngrok_url = setup_ngrok(app)

    #     # Log the Ngrok URL
    #     logger.info(f"Ngrok URL: {ngrok_url}")

    # logger.info("")
    # logger.info("---------------- FastAPI Setup ----------------")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload = True)
