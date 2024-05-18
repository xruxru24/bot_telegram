from aiogram import Router
from .comands import router as command_router

router = Router()


router.include_router(command_router)
