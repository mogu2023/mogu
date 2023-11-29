import autogen
from datamodle import AgentFlowSpec, LLMConfig, AgentConfig, FlowConfig
from atoms import GroupView, ControlRowView
from dash import html
from feffery_antd_components import AntdSlider, AntdSelect, AntdModal
import dash

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(__name__,
                external_scripts=external_script)
app.scripts.config.serve_locally = True


USER_PROXY_INSTRUCTIONS = """If the request has been addressed sufficiently, summarize the answer and end with the word TERMINATE. Otherwise, ask a follow-up question.
        """

llm_config = LLMConfig(
        config_list=[{"model": "gpt-4"}],
        temperature=0,
    )

assistant_spec = AgentFlowSpec(
        type="assistant",
        config=AgentConfig(
            name="primary_assistant",
            system_message=autogen.AssistantAgent.DEFAULT_SYSTEM_MESSAGE,
            llm_config=llm_config,
        ),
    )

userproxy_spec = AgentFlowSpec(
        type="userproxy",
        config=AgentConfig(
            name="user_proxy",
            human_input_mode="NEVER",
            system_message=USER_PROXY_INSTRUCTIONS,
            code_execution_config={
                # "work_dir": work_dir,
                "use_docker": False,
            },
            max_consecutive_auto_reply=10,
            llm_config=llm_config,
            is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
        ),
    )

flow_config = FlowConfig(
        name="default",
        sender=userproxy_spec,
        receiver=assistant_spec,
        type="default",
)


def FlowView(title, flowSpec):
    return html.Div(
        [
            html.Div(title, className='text-accent'),
            GroupView(
                title=flowSpec.config.name, className='mb-4',
                children=[
                    ControlRowView(
                        title='Max Consecutive Auto Reply',
                        className='mt-4',
                        description='Max consecutive auto reply messages before termination.',
                        value=flowSpec.config.max_consecutive_auto_reply,
                        control=AntdSlider(min=2, max=30, defaultValue=flowSpec.config.max_consecutive_auto_reply, step=1)

                    )
                ]
            )
        ],
    )


def AgentsControlView(flowConfig):
    return html.Div(
            [
                html.Div(flowConfig.name, className='mb-2'),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    FlowView(title='sender', flowSpec=flowConfig.sender)
                                )
                            ],
                            className='w-1/2'
                        )
                    ],
                    className='flex gap-3'
                )
            ]
        )


def AgentsView():
    return html.Div(
        [
            html.Div(
                [
                    html.Div('Agents', className='font-semibold pb-2 border-b'),
                    html.Div('Select or create an agent workflow.', className='text-xs mt-2 mb-2 pb-1'),
                    html.Div(
                        [
                            html.Div('Default Agent'),
                            html.Div(
                                AgentsControlView(flow_config), 
                                className='flex-1')
                        ],
                        className='text-xs text-secondary mt-2 flex'
                    )
                ],
                className='h-full  mb-4'
            )
        ]
    )