





# import operator
# import json
# from typing import TypedDict, Literal, Optional, List, Dict, Any
# from langgraph.graph import StateGraph, END
# from agents.llm_loader import get_llm
# from agents.medical_chat_agent import get_medical_response
# from agents.rag_agent.response_generator import ResponseGenerator
# from agents.web_search.web_search_processor import WebSearchProcessor
# from agents.guardrails import LocalGuardrails
# from agents.rag_agent.document_retriever import retrieve_documents
# from langchain_core.messages import AIMessage, HumanMessage, BaseMessage

# llm = get_llm()
# rag_agent = ResponseGenerator()
# web_agent = WebSearchProcessor()
# guard = LocalGuardrails(llm)

# # ✅ Define state
# class GraphState(TypedDict):
#     input: str
#     image: Optional[bytes]
#     image_type: str
#     agent_name: str
#     response: str
#     involved_agents: List[str]
#     input_type: Literal["text", "image"]
#     bypass_guardrails: bool
#     messages: List[BaseMessage]  # 👈 Added memory

# # ✅ Node 1: Guardrails
# def guardrails_node(state: GraphState):
#     if state["input_type"] == "image":
#         return {**state, "bypass_guardrails": True}

#     is_safe, message_or_input = guard.check_input(state["input"])
#     if not is_safe:
#         return {
#             **state,
#             "bypass_guardrails": False,
#             "agent_name": "GUARDRAILS_BLOCK",
#             "response": message_or_input.content,
#             "involved_agents": state.get("involved_agents", []) + ["GUARDRAILS_BLOCK"],
#             "messages": state["messages"] + [AIMessage(content=message_or_input.content)],
#         }

#     return {**state, "bypass_guardrails": True}

# # ✅ Node 2: Image Detection
# def image_detection_node(state: GraphState):
#     if state["input_type"] != "image":
#         return state
#     return {**state, "image_type": "xray"}  # Stub detection

# # ✅ Node 3: Agent Routing
# def route_to_agent(state: GraphState):
#     if state["agent_name"] == "GUARDRAILS_BLOCK":
#         return state

#     if state["input_type"] == "image":
#         if state["image_type"] == "xray":
#             return {**state, "agent_name": "CHEST_XRAY_CLASSIFIER_AGENT"}
#         elif state["image_type"] == "lesion":
#             return {**state, "agent_name": "LESION_SEGMENTATION_AGENT"}
#         else:
#             return {**state, "agent_name": "GUARDRAILS_BLOCK"}

#     prompt = f"""
# You are a decision-making agent that decides which specialist agent should respond to the user's medical query.

# List of agents:
# - CONVERSATION_AGENT: Handles general health queries or ambiguous input.
# - RAG_AGENT: Retrieves and answers based on a medical document database.
# - WEB_SEARCH_PROCESSOR_AGENT: Searches the web for real-time or uncommon questions.

# Given the user's input: \"{state['input']}\", respond ONLY as a JSON object like: {{"agent_name": "RAG_AGENT"}}
# """
#     memory = state["messages"] + [HumanMessage(content=prompt)]

#     agent_decision = llm.invoke(memory)

#     chosen = "CONVERSATION_AGENT"  # default fallback
#     if isinstance(agent_decision, AIMessage):
#         try:
#             decision_dict = json.loads(agent_decision.content)
#             chosen = decision_dict.get("agent_name", "CONVERSATION_AGENT")
#         except json.JSONDecodeError:
#             print("⚠️ Invalid JSON from agent_decision. Defaulting to CONVERSATION_AGENT")
#             print("agent_decision.content:", repr(agent_decision.content))

#     return {**state, "agent_name": chosen}

# # ✅ Node 4: Call Agent
# def call_agent(state: GraphState):
#     if state["agent_name"] == "GUARDRAILS_BLOCK":
#         return state

#     agent_name = state["agent_name"]
#     input_text = state.get("input", "")
#     image_data = state.get("image", None)
#     messages = state["messages"] + [HumanMessage(content=input_text)]

#     if agent_name == "CONVERSATION_AGENT":
        
#         response = get_medical_response(messages)
#         output = response.content
#         messages.append(AIMessage(content=output))

#     elif agent_name == "RAG_AGENT":
#         retrieved_docs = retrieve_documents(input_text)
#         retrieval = rag_agent.generate_response(input_text, retrieved_docs)
#         if "insufficient information" in retrieval["response"].lower():
#             response = web_agent.process_web_results(input_text)
#             output = response.content
#             agent_name = "WEB_SEARCH_PROCESSOR_AGENT"
#             messages.append(AIMessage(content=output))
#         else:
#             output = retrieval["response"]
#             messages.append(AIMessage(content=output))

#     elif agent_name == "WEB_SEARCH_PROCESSOR_AGENT":
#         response = web_agent.process_web_results(input_text)
#         output = response.content
#         messages.append(AIMessage(content=output))

#     elif agent_name == "CHEST_XRAY_CLASSIFIER_AGENT":
#         output = "🫁 Detected chest X-ray. Analysis will be here."
#         messages.append(AIMessage(content=output))

#     elif agent_name == "LESION_SEGMENTATION_AGENT":
#         output = "🩺 Detected skin lesion. Segmentation pending implementation."
#         messages.append(AIMessage(content=output))

#     else:
#         output = "⚠️ Could not process your request. Please try again."
#         messages.append(AIMessage(content=output))

#     updated_agents = state.get("involved_agents", []) + [agent_name]

#     return {
#         **state,
#         "response": output,
#         "involved_agents": updated_agents,
#         "agent_name": agent_name,
#         "messages": messages
#     }

# # ✅ Graph Builder
# def build_medical_agent_graph():
#     builder = StateGraph(GraphState)
#     builder.add_node("Guardrails", guardrails_node)
#     builder.add_node("ImageDetection", image_detection_node)
#     builder.add_node("RouteAgent", route_to_agent)
#     builder.add_node("CallAgent", call_agent)

#     builder.set_entry_point("Guardrails")
#     builder.add_edge("Guardrails", "ImageDetection")
#     builder.add_edge("ImageDetection", "RouteAgent")
#     builder.add_edge("RouteAgent", "CallAgent")
#     builder.add_edge("CallAgent", END)

#     return builder.compile()

# # ✅ Instantiate the graph
# medical_agent_graph = build_medical_agent_graph()

from agents.vision_agents.image_analysis_agent import analyze_image
import os
import uuid

import json
from typing import TypedDict, Literal, Optional, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage

from agents.llm_loader import get_llm
from agents.medical_chat_agent import get_medical_response
from agents.rag_agent.response_generator import ResponseGenerator
from agents.web_search.web_search_processor import WebSearchProcessor
from agents.guardrails import LocalGuardrails
from agents.rag_agent.document_retriever import retrieve_documents

# ✅ Initialize agents
llm = get_llm()
rag_agent = ResponseGenerator()
web_agent = WebSearchProcessor()
guard = LocalGuardrails(llm)

# ✅ Define shared state
class GraphState(TypedDict):
    input: str
    image: Optional[bytes]
    image_type: str
    agent_name: str
    response: str
    involved_agents: List[str]
    input_type: Literal["text", "image"]
    bypass_guardrails: bool
    messages: List[BaseMessage]

# ✅ Node 1: Guardrails check
def guardrails_node(state: GraphState):
    if state["input_type"] == "image":
        return {**state, "bypass_guardrails": True}

    is_safe, result = guard.check_input(state["input"])
    if not is_safe:
        return {
            **state,
            "bypass_guardrails": False,
            "agent_name": "GUARDRAILS_BLOCK",
            "response": result.content,
            "involved_agents": state.get("involved_agents", []) + ["GUARDRAILS_BLOCK"],
            "messages": state["messages"] + [AIMessage(content=result.content)],
        }

    return {**state, "bypass_guardrails": True}

# ✅ Node 2: Image detection stub
def image_detection_node(state: GraphState):
    if state["input_type"] != "image":
        return state
    return {**state, "image_type": "generic", "agent_name": "IMAGE_ANALYSIS_AGENT"}

# ✅ Node 3: Agent Routing
def route_to_agent(state: GraphState):
    if state["agent_name"] == "GUARDRAILS_BLOCK" or state["input_type"] == "image":
        return state  # already routed in image detection

    prompt = f"""
You are a decision-making agent that decides which specialist agent should respond to the user's medical query.

List of agents:
- CONVERSATION_AGENT: Handles general health queries or ambiguous input.
- RAG_AGENT: Retrieves and answers based on a medical document database.
- WEB_SEARCH_PROCESSOR_AGENT: Searches the web for real-time or uncommon questions.

Given the user's input: \"{state['input']}\", respond ONLY as a JSON object like: {{"agent_name": "RAG_AGENT"}}
"""
    memory = state["messages"] + [HumanMessage(content=prompt)]
    decision = llm.invoke(memory)

    chosen = "CONVERSATION_AGENT"
    if isinstance(decision, AIMessage):
        try:
            decision_dict = json.loads(decision.content)
            chosen = decision_dict.get("agent_name", "CONVERSATION_AGENT")
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON from agent_decision:", repr(decision.content))

    return {**state, "agent_name": chosen}

# ✅ Node 4: Call the routed agent
# def call_agent(state: GraphState):
#     if state["agent_name"] == "GUARDRAILS_BLOCK":
#         return state

#     input_text = state.get("input", "")
#     messages = state["messages"] + [HumanMessage(content=input_text)]
#     agent = state["agent_name"]

#     if agent == "CONVERSATION_AGENT":
#         response = get_medical_response(messages)
#         output = response.content

#     elif agent == "RAG_AGENT":
#         retrieved_docs = retrieve_documents(input_text)
#         result = rag_agent.generate_response(input_text, retrieved_docs)
#         output = result["response"]

#         if "insufficient information" in output.lower():
#             fallback = web_agent.process_web_results(input_text)
#             output = fallback.content
#             agent = "WEB_SEARCH_PROCESSOR_AGENT"

#     elif agent == "WEB_SEARCH_PROCESSOR_AGENT":
#         response = web_agent.process_web_results(input_text)
#         output = response.content

#     elif agent == "IMAGE_ANALYSIS_AGENT":
#         output = "🩻 Image received. Performing analysis..."  # Placeholder for model inference

#     else:
#         output = "⚠️ Could not process your request."

#     messages.append(AIMessage(content=output))
#     updated_agents = state.get("involved_agents", []) + [agent]

#     return {
#         **state,
#         "response": output,
#         "involved_agents": updated_agents,
#         "agent_name": agent,
#         "messages": messages,
#     }

def call_agent(state: GraphState):
    if state["agent_name"] == "GUARDRAILS_BLOCK":
        return state

    input_text = state.get("input", "")
    messages = state["messages"] + [HumanMessage(content=input_text)]
    agent = state["agent_name"]

    if agent == "CONVERSATION_AGENT":
        response = get_medical_response(messages)
        output = response.content

    elif agent == "RAG_AGENT":
        retrieved_docs = retrieve_documents(input_text)
        result = rag_agent.generate_response(input_text, retrieved_docs)
        output = result["response"]

        if "insufficient information" in output.lower():
            fallback = web_agent.process_web_results(input_text)
            output = fallback.content
            agent = "WEB_SEARCH_PROCESSOR_AGENT"

    elif agent == "WEB_SEARCH_PROCESSOR_AGENT":
        response = web_agent.process_web_results(input_text)
        output = response.content

    elif agent == "IMAGE_ANALYSIS_AGENT":
        try:
            # 🔽 Save uploaded image to temp file
            temp_filename = f"temp_{uuid.uuid4().hex}.png"
            with open(temp_filename, "wb") as f:
                f.write(state["image"])

            # 🔍 Analyze image using your image agent
            output = analyze_image(temp_filename)

            # 🧹 Cleanup
            os.remove(temp_filename)
        except Exception as e:
            output = f"❌ Image analysis failed: {str(e)}"

    else:
        output = "⚠️ Could not process your request."

    messages.append(AIMessage(content=output))
    updated_agents = state.get("involved_agents", []) + [agent]

    return {
        **state,
        "response": output,
        "involved_agents": updated_agents,
        "agent_name": agent,
        "messages": messages,
    }


# ✅ Build the graph
def build_medical_agent_graph():
    builder = StateGraph(GraphState)
    builder.add_node("Guardrails", guardrails_node)
    builder.add_node("ImageDetection", image_detection_node)
    builder.add_node("RouteAgent", route_to_agent)
    builder.add_node("CallAgent", call_agent)

    builder.set_entry_point("Guardrails")
    builder.add_edge("Guardrails", "ImageDetection")
    builder.add_edge("ImageDetection", "RouteAgent")
    builder.add_edge("RouteAgent", "CallAgent")
    builder.add_edge("CallAgent", END)

    return builder.compile()

# ✅ Compile the final graph
medical_agent_graph = build_medical_agent_graph()
