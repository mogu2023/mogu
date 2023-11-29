import uuid
from datetime import datetime
from typing import Any, Callable, Dict, List, Literal, Optional, Union
from pydantic.dataclasses import dataclass
from dataclasses import field


@dataclass
class LLMConfig:
    """Data model for LLM Config for Autogen"""

    config_list: List[Any] = field(default_factory=List)
    temperature: float = 0
    cache_seed: Optional[Union[int, None]] = None
    timeout: Optional[int] = None


@dataclass
class AgentConfig:
    """Data model for Agent Config for Autogen"""

    name: str
    llm_config: Optional[LLMConfig] = None
    human_input_mode: str = "NEVER"
    max_consecutive_auto_reply: int = 10
    system_message: Optional[str] = None
    is_termination_msg: Optional[Union[bool, str, Callable]] = None
    code_execution_config: Optional[Union[bool, str, Dict[str, Any]]] = None


@dataclass
class AgentFlowSpec:
    """Data model to help flow load agents from config"""

    type: Literal["assistant", "userproxy", "groupchat"]
    config: AgentConfig = field(default_factory=AgentConfig)


@dataclass
class FlowConfig:
    """Data model for Flow Config for Autogen"""

    name: str
    sender: AgentFlowSpec
    receiver: Union[AgentFlowSpec, List[AgentFlowSpec]]
    type: Literal["default", "groupchat"] = "default"

