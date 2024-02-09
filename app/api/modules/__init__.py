from fastapi import FastAPI, APIRouter

def include_api_routers(app: FastAPI | APIRouter) -> None:
    # Import APIRouters from components
    # Include the routers in the app
    
    # For example, if we have a books module
    # from .books.endpoints import router as books_router
    # app.include_router(books_router)

    from .user.endpoints import router as users_router
    app.include_router(users_router)

    from .station.endpoints import router as stations_router
    app.include_router(stations_router)

    from .train.endpoints import router as trains_router
    app.include_router(trains_router)

    from .wallet.endpoints import router as wallets_router
    app.include_router(wallets_router)

    from .ticket.endpoints import router as tickets_router
    app.include_router(tickets_router)


