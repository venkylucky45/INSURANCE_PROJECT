# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# # Routers
# from src.api.routers.segment import router as segment_router
# from src.api.routers.risk import router as risk_router
# from src.api.routers.recommend import router as recommend_router
# from src.api.routers.genai import router as genai_router


# def create_app():

#     app = FastAPI(
#         title="Travel Insurance Segmentation & Recommendation API",
#         description="ML + GenAI powered Travel Insurance Intelligence System",
#         version="1.0.0"
#     )

#     # CORS (optional)
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=["*"],
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"],
#     )

#     # Register Routers
#     app.include_router(segment_router, prefix="/segmentation", tags=["Segmentation"])
#     app.include_router(risk_router, prefix="/risk", tags=["Risk Prediction"])
#     app.include_router(recommend_router, prefix="/recommend", tags=["Recommendation"])
#     app.include_router(genai_router, prefix="/genai", tags=["GenAI RAG"])

#     @app.get("/")
#     def root():
#         return {
#             "message": "Travel Insurance Recommendation System API is running",
#             "modules_available": [
#                 "Segmentation",
#                 "Risk Prediction",
#                 "Recommendation Engine",
#                 "GenAI RAG Assistant"
#             ]
#         }

#     return app


# app = create_app()
