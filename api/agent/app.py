from fastapi import FastAPI
from langgraph_api import add_routes
from agent.graph import graph

app = FastAPI(
    title="Deep Research Agent",
    version="1.0",
    description="A simple agent that can perform deep research on a given topic.",
)

add_routes(
    app,
    graph,
    path="/agent",
    input_schema=str,
    output_schema=str,
    config_keys=["configurable"],
)
