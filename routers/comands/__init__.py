from aiogram import Router
from .quadratic import router as quadratic_equations_router
from .arithmetic import router as arithmetic_router


router = Router()

router.include_router(quadratic_equations_router)
router.include_router(arithmetic_router)
