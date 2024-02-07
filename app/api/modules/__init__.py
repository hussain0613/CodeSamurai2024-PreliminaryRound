from fastapi import FastAPI

def include_api_routers(app: FastAPI) -> None:
    # Import APIRouters from components
    # Include the routers in the app
    
    # For example, if we have a books module
    from .books.endpoints import router as books_router
    app.include_router(books_router)

