from fastapi import APIRouter, UploadFile
import aiofiles

router = APIRouter(
    prefix='/images',
    tags=['Загрузка картинок']
)


@router.post('/hotels')
async def add_hotel_image(name: int, file_to_upload: UploadFile):
    async with aiofiles.open(f'app/static/images/{name}.webp', 'wb+') as file_object:
        file = await file_to_upload.read()
        await file_object.write(file)
