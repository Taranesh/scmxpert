# pylint: disable=no-name-in-module
# pylint: disable=too-few-public-methods
"""
this class has signup schema
"""
import random
import string
import os
import datetime as dt
from typing import Dict, List, Optional
import pymongo
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
from fastapi.logger import logger
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import FastAPI, Form, Request, HTTPException, status, Depends, Response, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2, OAuth2PasswordRequestForm
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from config.config import SETTING
from models.models import User
from routers.user import get_current_user_from_token


load_dotenv()

APP = APIRouter(tags=["creating shipment api's"])

APP.mount("/static", StaticFiles(directory="static"), name="static")

TEMPLATES = Jinja2Templates(directory="templates")

CLIENT = SETTING.CLIENT

DATA_STREAM = SETTING.DATA_STREAM
# --------------------------------------------------------------------------
# Data stream Page
# --------------------------------------------------------------------------
# A Data stream page that only logged in users can access.
@APP.get("/datastream", response_class=HTMLResponse)
def stream_page(request: Request, user: User = Depends(get_current_user_from_token)):
    """
    A route function that handles HTTP GET requests to "/datastream".
    This function fetches data from a MongoDB collection called "DATA_STREAM".
    The data is then passed to the "Devicedata.html" template for rendering.
    Args:
    request (Request): A `Request` object representing the incoming HTTP request.
    user (User, optional): An optional `User` object representing the current user.
    Returns:
    A `TemplateResponse` object that renders the "Devicedata.html" template
    with the given request context. The response's `Content-Type` header is
    set to "text/html".
    """
    # Code to fetch data from MongoDB and render template
    # ...
    try:
        streaming_data = []
        all_shipments = DATA_STREAM.find({})
        for i in all_shipments:
            streaming_data.append(i)
        context = {
            "user": user,
            "streaming_data":streaming_data,
            "request": request
        }
        return TEMPLATES.TemplateResponse("datastream.html", context)
    except Exception as e:
        error_msg = f"An error occurred while trying to retrieve data from the database: {str(e)}"
        return HTTPException(status_code=500, detail=error_msg)
