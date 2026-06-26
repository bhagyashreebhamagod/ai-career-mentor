from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.resume_agent import parse_resume
from agents.skill_agent import extract_skills
from agents.career_agent import recommend_career
from agents.roadmap_agent import roadmap
from agents.interview_agent import interview


class ResumeState(TypedDict):
    file_path: str
    resume_text: str
    skills: str
    careers: str
    roadmap: str
    interview_questions: str


def parse_node(state):
    state["resume_text"] = parse_resume(state["file_path"])
    return state


def skills_node(state):
    state["skills"] = extract_skills(state["resume_text"])
    return state


def career_node(state):
    state["careers"] = recommend_career(state["skills"])
    return state


def roadmap_node(state):
    state["roadmap"] = roadmap(state["skills"])
    return state


def interview_node(state):
    state["interview_questions"] = interview(state["skills"])
    return state


builder = StateGraph(ResumeState)

builder.add_node("parser", parse_node)
builder.add_node("skills", skills_node)
builder.add_node("career", career_node)
builder.add_node("roadmap", roadmap_node)
builder.add_node("interview", interview_node)

builder.set_entry_point("parser")

builder.add_edge("parser", "skills")
builder.add_edge("skills", "career")
builder.add_edge("career", "roadmap")
builder.add_edge("roadmap", "interview")
builder.add_edge("interview", END)

workflow = builder.compile()
