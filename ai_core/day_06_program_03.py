from dataclasses import dataclass, field


@dataclass
class SimpleAgent:
    name: str
    tools: list[str] = field(default_factory=list)

    def add_tool(self, tool_name: str) -> None:
        cleaned_tool_name = tool_name.strip()

        if not cleaned_tool_name:
            raise ValueError("Tool name cannot be empty.")

        self.tools.append(cleaned_tool_name)


research_agent = SimpleAgent("Research Agent")
support_agent = SimpleAgent("Support Agent")

research_agent.add_tool("web_search")

print(research_agent)
print(support_agent)