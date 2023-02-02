from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes.employee import employee as employeeRoute
from routes.beneficiary import beneficiary as beneficiaryRoute
from database.manager import engine
import models.employeeModel
import models.beneficiaryModel
from fastapi.middleware.cors import CORSMiddleware

models.employeeModel.Base.metadata.create_all(bind=engine)
models.beneficiaryModel.Base.metadata.create_all(bind=engine)

main = FastAPI(
    title="API KSP backend",
    description="Api from employee and beneficiary",
    version="1.0"
)

main.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

main.include_router(employeeRoute.router, tags=["Employee"])
main.include_router(beneficiaryRoute.router, tags=["Beneficiary"])

@main.get("/", tags=["root"])
async def root():
    return RedirectResponse(url="/docs/")