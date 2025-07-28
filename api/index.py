from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langgraph_api import add_routes
from agent.graph import graph

app = FastAPI(
    title="Deep Research Agent",
    version="1.0",
    description="A simple agent that can perform deep research on a given topic.",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ownsearch-new.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


add_routes(
    app,
    graph,
    path="/agent",
    input_schema=str,
    output_schema=str,
    config_keys=["configurable"],
)
