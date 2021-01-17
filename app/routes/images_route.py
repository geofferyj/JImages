from fastapi import File, UploadFile, APIRouter, Body
from fastapi.encoders import jsonable_encoder
from PIL import Image, ExifTags


from database import (
    add_image,
    delete_image,
    get_user_images,
    get_image,
)
from models import (
    ErrorResponseModel,
    ResponseModel,
    ImageModel,
    UserModel,
)
router = APIRouter()

@router.post("/uploadfile/")
async def upload_one(file: UploadFile = File(...)):
    return {"filename": file.filename}

@router.post("/add-image/", response_description="Image added")
async def add_image_info(file: UploadFile = File(...)):
    img = Image.open(file.file)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    return ResponseModel(exif, "image added successfully.")