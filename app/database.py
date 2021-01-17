import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://jimage_admin:jdTgKNcr5kDmn6FZ@jimagerepo.of3dv.mongodb.net/jimages_db?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client.jimages_db

users = db.get_collection("users")
images = db.get_collection("images")


def result_to_dict(result):
    for item in result:
        print(item)

# Get all user Images
async def get_user_images():
    images = []
    async for student in images.find():
        images.append(result_to_dict(student))
    return images


# Add a new image into to the database
async def add_image(image_info: dict) -> dict:
    image = await images.insert_one(image_info)
    new_image = await images.find_one({"_id": image.inserted_id})
    return result_to_dict(new_image)


# get an image by it's id
async def get_image(id: str) -> dict:
    image = await images.find_one({"_id": ObjectId(id)})
    if image:
        return result_to_dict(image)


# Update a student with a matching ID
# async def update_user(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         updated_student = await student_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_student:
#             return True
#         return False


# Delete an image
async def delete_image(id: str):
    image = await images.find_one_and_delete({"_id": ObjectId(id)})
    return True